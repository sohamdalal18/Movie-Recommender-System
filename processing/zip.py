import os
import zipfile

compressed_folder = "file.zip"
extraction_path = "Files" 

# Extract the zip file if the folder doesn't exist
if not os.path.exists(extraction_path):
    with zipfile.ZipFile(compressed_folder, 'r') as zip_ref:
        zip_ref.extractall()


# Base path for pickle files
base_path = "Files"