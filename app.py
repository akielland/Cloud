
import streamlit as st
from modules.uploader import save_file_and_metadata

st.title("Cloud Data Upload Portal")

# Form fields
uploaded_file = st.file_uploader("Choose a file")
project = st.text_input("Project name")
uploader = st.text_input("Your name")
comments = st.text_area("Comments (optional)")

if st.button("Submit"):
    if uploaded_file and project and uploader:
        file_path = save_file_and_metadata(uploaded_file, project, uploader, comments)
        st.success(f"File saved to {file_path}")
    else:
        st.warning("Please complete all required fields.")
