# Cloud Data Upload Portal 
# --- modules/uploader.py ---
# This module handles file uploads and metadata management for a cloud data upload portal.
import uuid
import json
from pathlib import Path
from datetime import date
import pandas as pd

# Root folder to save files
DATA_ROOT = Path("data")
METADATA_FILE = DATA_ROOT / "metadata.csv"

# Check if the data directory exists, if not create it
if not DATA_ROOT.exists():
    DATA_ROOT.mkdir(parents=True, exist_ok=True)

# Ensure the metadata file exists
if not METADATA_FILE.exists():
    # Create an empty metadata file with headers
    pd.DataFrame(columns=[
        "file_id", "file_name", "project_name", "uploader_name",
        "upload_date", "file_path", "comments", "file_format"
    ]).to_csv(METADATA_FILE, index=False)

# check if the metadata file is made
print("Metadata file created:", METADATA_FILE.exists())



# Function to save the uploaded file
# and create a folder structure based on the project name and date
def save_uploaded_file(file, project_name):
    # first: make data storage folder if it doesn't exist
    today = date.today().isoformat() # "2025-05-08"
    folder_path = DATA_ROOT / project_name / today
     # Create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)
    print("Folder created:", folder_path.exists())
    print("Folder contains:", list(folder_path.iterdir()))
    print("File name:", file.name)
    
    # save uploaded file
    file_path = folder_path / file.name
    # TODO: Check if the file already exists
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())  # Save the file to the specified path
    return file_path




# Prepare metadata row
def create_metadata_dict(file, project_name, uploader_name, comments, file_path):
    return {
        "file_id": str(uuid.uuid4()),
        "file_name": file.name,
        "project_name": project_name,
        "uploader_name": uploader_name,
        "upload_date": date.today().isoformat(),
        "file_path": str(file_path),
        "comments": comments,
        "file_format": Path(file.name).suffix.lstrip("."),
    }



# Append metadata to local CSV
def append_metadata_row(metadata):
    df = pd.DataFrame([metadata])
    df.to_csv(METADATA_FILE, mode="a", header=False, index=False)


def save_metadata_json(metadata, file_path):
    # Save metadata as JSON
    metadata_path = file_path.with_suffix(file_path.suffix + ".metadata.json")
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)
    print("Metadata saved to:", metadata_path)

# Save file and metadata
def save_file_and_metadata(file, project_name, uploader_name, comments):
    file_path = save_uploaded_file(file, project_name)
    metadata = create_metadata_dict(file, project_name, uploader_name, comments, file_path)
    append_metadata_row(metadata)
    save_metadata_json(metadata, file_path)
    return file_path, metadata