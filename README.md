# Cloud 1 – Data Upload Portal Pilot

This is a pilot project for creating a simple internal **web-based data upload portal** for uploading data to the cloud. The goal is to allow users to upload datasets via a browser interface, fill in metadata through a short form, and automatically store both the file and metadata for later retrieval and analysis.

---

## Project Description

The system provides:

- A **Streamlit web app** where users can:
  - Upload files (CSV, Excel, etc.)
  - Fill in a form with metadata (project name, tags, contact, sensitivity, etc.)
- Automatic upload of files to **OneLake Files** inside a **Fabric Lakehouse**
- Automatic saving of metadata to a **Delta Table** inside the same Lakehouse (`metadata_catalog`)
- A clear, modular code structure to support expansion and deployment

---

##  Tools and Stack (Phase 1)

| Purpose              | Tool / Service             |
|----------------------|----------------------------|
| Web frontend         | Streamlit (Python)         |
| File storage         | Microsoft Fabric → OneLake → Lakehouse Files |
| Metadata storage     | Local CSV → Delta Table (Fabric) |
| Metadata storage     | Delta Table (`metadata_catalog`) in Fabric Lakehouse |
| Backend logic        | Python modules             |

---

## Phase 1 Goals

1. **Build and run Streamlit app locally**:
   - Allow file upload via web UI
   - Collect and validate metadata through a form
   - Save file to Lakehouse `/Files/` folder via Fabric APIs or direct mount
   - Save metadata to `metadata_catalog` Delta Table in the `/Tables/` folder

2. **Structure code as a maintainable project**:
   - Use modular Python code for backend logic
   - Organize logic for upload, metadata handling, and Fabric interaction

3. **Test and demo the system**:
   - Run locally or within a small team
   - Verify file and metadata integrity

4. **Prepare for Phase 2**:
   - Add metadata search and retrieval UI
   - Enable authentication for secure access
   - Deploy on Streamlit Cloud or Azure App Service for internal use

---
  
<pre><code>
Lakehouse/
│
├── Files/                         # Uploaded raw files
│   └── project_name/
│       └── yyyy-mm-dd/
│           └── my_dataset.csv
│
└── Tables/
    └── metadata_catalog           # Delta Table with metadata for each file
</code></pre>


## Metadata Protocol (V1)

Each upload stores the following metadata:

| Field             | Description                             |
|------------------|-----------------------------------------|
| `file_name`       | Name of the uploaded file               |
| `project_name`    | Name of the project or team             |
| `uploader_name`   | Person uploading the file               |
| `upload_time`     | Auto-generated timestamp                |
| `tags`            | Comma-separated or array of keywords    |
| `file_format`     | CSV, XLSX, JSON, etc.                   |
| `storage_path`    | Path to file in Fabric Lakehouse        |
| `comments`        | Free-text description                   |
| `data_sensitivity`| Public / Internal / Confidential        |


