# This is a simple Streamlit app that allows users to upload files and save metadata.
# User can also view and filter metadata.

import streamlit as st
from modules.uploader import save_file_and_metadata
from modules.metadata_viewer import load_metadata, filter_metadata

st.set_page_config(page_title="Cloud Upload Portal", layout="wide")
st.title("Cloud Data Upload Portal")

# Sidebar for metadata filtering -> to be done later
# st.sidebar.header("Metadata Filter")
# metadata_df = load_metadata()

# Form fields
st.header("1. Upload a File")
uploaded_file = st.file_uploader("Choose a file")
project = st.text_input("Project name")
uploader = st.text_input("Your name")
comments = st.text_area("Comments (optional)")

if st.button("Submit"):
    if uploaded_file and project and uploader:
        file_path, metadata = save_file_and_metadata(uploaded_file, project, uploader, comments)
        st.success(f"File saved to {file_path}")
        st.json(metadata) # Display metadata
    else:
        st.warning("Please complete all required fields.")

# Metadata Viewer
st.divider()
st.header("2. View Metadata")
df = load_metadata()
if not df.empty:
    col1, col2 = st.columns(2)
    with col1:
        project_filter = st.selectbox("Filter by project", ["All"] + sorted(df["project_name"].unique().tolist()))
    with col2:
        uploader_filter = st.selectbox("Filter by uploader", ["All"] + sorted(df["uploader_name"].unique().tolist()))

    if project_filter != "All":
        df = filter_metadata(df, "project_name", project_filter)
    if uploader_filter != "All":
        df = filter_metadata(df, "uploader_name", uploader_filter)

    st.dataframe(df, use_container_width=True)
else:
    st.info("No metadata found yet. Upload a file first.")