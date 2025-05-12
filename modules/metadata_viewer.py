# This is part of app that allows users to upload files and save metadata.

import pandas as pd

from modules.uploader import METADATA_FILE

# --- modules/metadata_viewer.py ---



def load_metadata():
    """
    Load metadata from the CSV file. If the file does not exist or is empty,
    create a new DataFrame with the expected columns.
    """
    expected_columns = [
        "file_id", "file_name", "project_name", "uploader_name",
        "upload_date", "file_path", "comments", "file_format"
    ]
    if METADATA_FILE.exists():
        try:
            df = pd.read_csv(METADATA_FILE)
            if all(col in df.columns for col in expected_columns):
                return df
        except Exception:
            pass

    print("Loading metadata from:", METADATA_FILE.resolve())
    print("File exists:", METADATA_FILE.exists())


    return pd.DataFrame(columns=expected_columns)



def filter_metadata(df, by, value):
    return df[df[by] == value] if by in df.columns else df



