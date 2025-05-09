# Cloud Data Upload Portal 
# --- modules/uploader.py ---
# This module handles file uploads and metadata management for a cloud data upload portal.
import uuid
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
        "file_name", "project_name", "uploader_name",
          "upload_date", "file_path", "comments", "file_format"
          ]).to_csv(METADATA_FILE, index=False)



def save_uploaded_file(file, project_name):    
    # Step 1: Prepare folder path
    today = date.today().isoformat()  # e.g. "2025-05-08"
    folder_path = DATA_ROOT / project_name / today
    # Create the folder if it doesn't exist
    folder_path.mkdir(parents=True, exist_ok=True)

    # Step 2: Save uploaded file
    file_path = folder_path / file.name
    with open(file_path, "wb") as f:
        f.write(file.getbuffer()) # Save the file to the specified path
    # Check if the file already exists

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


# Save file and metadata
def save_file_and_metadata(file, project_name, uploader_name, comments):
    # Save the uploaded file
    file_path = save_uploaded_file(file, project_name)

    # Create metadata dictionary
    metadata = create_metadata_dict(file, project_name, uploader_name, comments, file_path)

    # Append metadata to CSV
    append_metadata_row(metadata)

    return file_path, metadata["file_id"]

