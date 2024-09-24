import os

# List the mask files in the relevant directory
mask_dir = 'Linemod_preprocessed/data/01/mask'
mask_files = os.listdir(mask_dir)

#print("Available mask files:", mask_files)

# Check for specific frame masks
for frame in range(230, 236):  # Adjust range as needed
    mask_file = f'{frame:04d}.png'  
    if mask_file in mask_files:
        print(f"Mask for frame {frame} found: {mask_file}")
    else:
        print(f"Mask for frame {frame} not found.")
