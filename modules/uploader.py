import os
import pandas as pd
from pathlib import Path
from datetime import date

# Root folder to save files
DATA_ROOT = Path("data")
METADATA_FILE = Path("metadata.csv")


def save_file_and_metadata(file, project_name, uploader_name, comments):
    # Step 1: Prepare folder path
    today = date.today().isoformat()  # e.g. "2025-05-08"
    folder_path = DATA_ROOT / project_name / today
    folder_path.mkdir(parents=True, exist_ok=True)

    # Step 2: Save uploaded file
    file_path = folder_path / file.name
    with open(file_path, "wb") as f:
        f.write(file.getbuffer())

    # Step 3: Prepare metadata row
    metadata = {
        "file_name": file.name,
        "project_name": project_name,
        "uploader_name": uploader_name,
        "upload_date": today,
        "file_path": str(file_path),
        "comments": comments,
        "file_format": Path(file.name).suffix.lstrip("."),
    }

    # Step 4: Append metadata to local CSV
    metadata_df = pd.DataFrame([metadata])
    if METADATA_FILE.exists():
        metadata_df.to_csv(METADATA_FILE, mode="a", header=False, index=False)
    else:
        metadata_df.to_csv(METADATA_FILE, mode="w", header=True, index=False)

    return file_path