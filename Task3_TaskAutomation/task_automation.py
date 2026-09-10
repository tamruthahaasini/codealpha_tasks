import os
import shutil

# Folder containing the files
source_folder = "test_files"

# Folder where JPG images will be moved
destination_folder = "jpg_files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Check all files in the source folder
for file in os.listdir(source_folder):

    # Check if the file is a JPG image
    if file.lower().endswith(".jpg"):
        
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        # Move the JPG file
        shutil.move(source_path, destination_path)

        print(file, "moved successfully!")

print("\nJPG file organization completed!")
