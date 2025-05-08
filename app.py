import streamlit as st

st.title("Upload Portal")

file = st.file_uploader("Choose a file")
project = st.text_input("Project name")
uploader = st.text_input("Your name")

if st.button("Submit"):
    if file and project:
        # Save logic here (to disk or OneLake later)
        st.success("File uploaded successfully!")
    else:
        st.warning("Please fill in all fields.")
