from hots import load_HOTS_scenes
from estimater import FoundationPose
from Utils import *

def run_hots():
    # Load the HOTS dataset
    train_data, _ = load_HOTS_scenes(root='HOTS_v1', transform=True)

    # Initialize FoundationPose (may need to adapt for RGB-only data)
    estimator = FoundationPose(model_pts=None, model_normals=None, scorer=None, refiner=None)

    # Loop through the HOTS dataset
    for i in range(len(train_data)):
        img, target = train_data[i]
        
        # For HOTS, we'll assume the mask is in 'instance_masks'
        instance_mask = target["instance_masks"]
        
        # Note: You might want to check if 'K' is provided in the HOTS dataset, otherwise handle it.
        K = None  # Replace this with actual camera intrinsics if available

        # Perform pose estimation using the RGB image and instance mask
        pose = estimator.register(K=K, rgb=img, ob_mask=instance_mask)
        
        # Print the pose for each sample
        print(f"Pose for sample {i}: {pose}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    code_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Specify HOTS dataset directory
    parser.add_argument('--hots_dir', type=str, default="path/to/HOTS_v1", help="HOTS dataset root directory")

    # Add optional debug flag for logging or testing
    parser.add_argument('--debug', type=int, default=0, help="Debug level (0 for no debug)")
    parser.add_argument('--debug_dir', type=str, default=f'{code_dir}/debug', help="Directory to save debug information")
    
    opt = parser.parse_args()

    # Set the random seed for reproducibility (optional but recommended)
    set_seed(0)

    # Run the HOTS-specific pose estimation function
    run_hots()
