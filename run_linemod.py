# Copyright (c) 2023, NVIDIA CORPORATION.  All rights reserved.
#
# NVIDIA CORPORATION and its licensors retain all intellectual property
# and proprietary rights in and to this software, related documentation
# and any modifications thereto.  Any use, reproduction, disclosure or
# distribution of this software and related documentation without an express
# license agreement from NVIDIA CORPORATION is strictly prohibited.

"""
This script is designed to run pose estimation using the FoundationPose model 
on the LINEMOD dataset, a popular dataset used for 6D object pose estimation. 
The script processes individual frames of RGB-D images, extracts the necessary 
information (like masks, camera intrinsics, and object poses), and then estimates 
the object pose for each frame using FoundationPose.


Key Requirements for FoundationPose Model to Predict:
To run FoundationPose for pose estimation, the following is required:

  - Object Mesh (3D model): Either the ground-truth mesh or a reconstructed mesh.
  - Camera Intrinsics (K Matrix): These must be extracted for each frame.
  - Object Mask: A binary mask that highlights the region where the object is present.
  - RGB and Depth Images: For each frame, the pose estimation uses both RGB and depth data.
  - Ground Truth Pose (optional): Only needed if you want to compare or evaluate the accuracy of predictions.
"""



"""
datareader.py and estimater.py handle reading the data and estimating the pose using FoundationPose.
Utils contains helper functions related to the model or data processing.
"""
from Utils import *
import os,sys
from datareader import *
from estimater import *
code_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(f'{code_dir}/mycpp/build')
import yaml



def get_mask(reader, i_frame, ob_id, detect_type):
  """
  This function extracts the object mask for a given frame and object ID. 
  Depending on the detection type (box, mask, or detected), it processes 
  the mask differently:

  box: Extracts a bounding box around the object.
  mask: Uses the binary mask for the object.
  detected: Loads a pre-generated mask file from disk.

  The mask will be used later in the pipeline to constrain where the model looks for the object.
  """
  if detect_type=='box':
    mask = reader.get_mask(i_frame, ob_id)
    H,W = mask.shape[:2]
    vs,us = np.where(mask>0)
    umin = us.min()
    umax = us.max()
    vmin = vs.min()
    vmax = vs.max()
    valid = np.zeros((H,W), dtype=bool)
    valid[vmin:vmax,umin:umax] = 1
  elif detect_type=='mask':
    mask = reader.get_mask(i_frame, ob_id)
    if mask is None:
      return None
    valid = mask>0
  elif detect_type=='detected':
    mask = cv2.imread(reader.color_files[i_frame].replace('rgb','mask_cosypose'), -1)
    valid = mask==ob_id
  else:
    raise RuntimeError
  return valid



def run_pose_estimation_worker(reader, i_frames, est: FoundationPose = None, debug=0, ob_id=None, device='cuda:0'):
  """
  Sets up the environment for running pose estimation (e.g., selecting the GPU, setting up the rendering context).

  Loops through each frame and:
    - Reads the color and depth images for the frame.
    - Extracts the camera intrinsics (K matrix) and the object mask.
    - Calls the FoundationPose model to estimate the 6D pose of the object in that frame.
    - If debug is enabled, it exports the transformed mesh for visualization.

  The final result is stored in a nested dictionary (NestDict), with the pose estimates for each object in each frame.
  """
  result = NestDict()
  torch.cuda.set_device(device)
  est.to_device(device)
  est.glctx = dr.RasterizeCudaContext(device=device)
  debug_dir = est.debug_dir

  for i, i_frame in enumerate(i_frames):
      logging.info(f"{i}/{len(i_frames)}, i_frame:{i_frame}, ob_id:{ob_id}")
      video_id = reader.get_video_id()
      color = reader.get_color(i_frame)
      depth = reader.get_depth(i_frame)
      id_str = reader.id_strs[i_frame]
      H, W = color.shape[:2]

      # Limit to processing only object ID 1 (or another desired object ID)
      if ob_id != 1:
        continue  # Skip other objects

      # Extract the K matrix for the current frame as a NumPy array
      frame_key = str(i_frame).zfill(6)  # Ensure the frame number is zero-padded to match the dictionary keys
      if frame_key not in reader.K:
          logging.error(f"K matrix not found for frame {frame_key}. Skipping.")
          result[video_id][id_str][ob_id] = np.eye(4)
          continue
      
      K_matrix = np.array(reader.K[frame_key])  # Convert K to a NumPy array

      ob_mask = get_mask(reader, i_frame, ob_id, detect_type=detect_type)
      if ob_mask is None:
          logging.info("ob_mask not found, skip")
          result[video_id][id_str][ob_id] = np.eye(4)
          continue

      est.gt_pose = reader.get_gt_pose(i_frame, ob_id)

      # Pass the K matrix as a NumPy array to the register function
      pose = est.register(K=K_matrix, rgb=color, depth=depth, ob_mask=ob_mask, ob_id=ob_id)
      logging.info(f"pose:\n{pose}")

      if debug >= 3:
          m = est.mesh_ori.copy()
          tmp = m.copy()
          tmp.apply_transform(pose)
          tmp.export(f'{debug_dir}/model_tf.obj')

      result[video_id][id_str][ob_id] = pose

  return result



def run_pose_estimation():
  """
  This is the main function that orchestrates the entire pose estimation process:
    - Sets up the reader for the LINEMOD dataset (LinemodReader).
    - Loads the mesh for each object in the dataset and resets the model for each object.
    - Runs the pose estimation worker function for each frame.
    - Saves the results (poses for each frame and object) in a YAML file (linemod_res.yml).
  """
  wp.force_load(device='cuda')
  reader_tmp = LinemodReader(f'Linemod_preprocessed/data/01', split=None)

  debug = opt.debug
  use_reconstructed_mesh = opt.use_reconstructed_mesh
  debug_dir = opt.debug_dir

  res = NestDict()
  glctx = dr.RasterizeCudaContext()
  mesh_tmp = trimesh.primitives.Box(extents=np.ones((3)), transform=np.eye(4)).to_mesh()
  est = FoundationPose(model_pts=mesh_tmp.vertices.copy(), model_normals=mesh_tmp.vertex_normals.copy(), symmetry_tfs=None, mesh=mesh_tmp, scorer=None, refiner=None, glctx=glctx, debug_dir=debug_dir, debug=debug)

  for ob_id in reader_tmp.ob_ids:
    ob_id = int(ob_id)

    if ob_id != 1:
      continue  # Skip other objects

    if use_reconstructed_mesh:
        mesh = reader_tmp.get_reconstructed_mesh(ob_id, ref_view_dir=opt.ref_view_dir)
    else:
        mesh = reader_tmp.get_gt_mesh(ob_id)
    symmetry_tfs = reader_tmp.symmetry_tfs[ob_id]

    args = []

    video_dir = f'Linemod_preprocessed/data/{ob_id:02d}'
    reader = LinemodReader(video_dir, split=None)
    video_id = reader.get_video_id()
    est.reset_object(model_pts=mesh.vertices.copy(), model_normals=mesh.vertex_normals.copy(), symmetry_tfs=symmetry_tfs, mesh=mesh)

    for i in range(len(reader.color_files)):
        args.append((reader, [i], est, debug, ob_id, "cuda:0"))

    outs = []
    for arg in args:
        out = run_pose_estimation_worker(*arg)
        outs.append(out)

    for out in outs:
        for video_id in out:
            for id_str in out[video_id]:
                for ob_id in out[video_id][id_str]:
                    res[video_id][id_str][ob_id] = out[video_id][id_str][ob_id]

  with open(f'{opt.debug_dir}/linemod_res.yml','w') as ff:
      yaml.safe_dump(make_yaml_dumpable(res), ff)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    code_dir = os.path.dirname(os.path.realpath(__file__))

    print("CODE DIR", code_dir)
    
    # Add arguments for LINEMOD directory and other settings
    parser.add_argument('--linemod_dir', type=str, default="/Linemod_preprocessed", help="LINEMOD root directory")
    parser.add_argument('--use_reconstructed_mesh', type=int, default=0, help="Use reconstructed mesh or ground truth")
    parser.add_argument('--ref_view_dir', type=str, default="/Linemod_preprocessed/ref_views")
    parser.add_argument('--debug', type=int, default=0, help="Debug level")
    parser.add_argument('--debug_dir', type=str, default=f'{code_dir}/debug', help="Directory to save debug info")

    opt = parser.parse_args()

    # Set a random seed for reproducibility
    set_seed(0)

    # Define detection type (mask, box, or detected)
    detect_type = 'mask'

    # Run pose estimation
    run_pose_estimation()