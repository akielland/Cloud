# This is a simple Streamlit app that allows users to upload files and save metadata.

import pandas as pd

# --- modules/metadata_viewer.py ---

def load_metadata():
    if METADATA_FILE.exists():
        return pd.read_csv(METADATA_FILE)
    return pd.DataFrame()


def filter_metadata(df, by, value):
    return df[df[by] == value] if by in df.columns else df