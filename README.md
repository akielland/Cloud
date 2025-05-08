# Cloud 1 – Data Upload Portal Pilot

This is a pilot project for creating a simple internal **web-based data upload portal** for uploading data to the cloud. The goal is to allow users to upload datasets via a browser interface, fill in metadata through a short form, and automatically store both the file and metadata for later retrieval and analysis.

---

## Project Description

The system provides:

- A **Streamlit web app** where users can:
  - Upload files (CSV, Excel, etc.)
  - Fill in a form with metadata (project name, tags, contact, comments)
- Automatic upload of files to **Azure Blob Storage**
- Automatic saving of metadata to a structured format (initially CSV, later Delta table in Azure Fabric Lakehouse)
- A clear project structure for future expansion and deployment

---

##  Tools and Stack (Phase 1)

| Purpose              | Tool / Service             |
|----------------------|----------------------------|
| Web frontend         | Streamlit (Python)         |
| File storage         | Azure Blob Storage         |
| Metadata storage     | Local CSV → Delta Table (Fabric) |
| Backend logic        | Python modules             |

---

## 📌 Phase 1 Goals

1. **Build and run Streamlit app locally**:
   - Support file upload and form input
   - Save files locally or in Azure Blob Storage
   - Save metadata to CSV

2. **Structure code as a maintainable project**:
   - Use modular Python code for backend logic

3. **Test and demo the system**:
   - Share local app with test users
   - Verify file and metadata integrity

4. **Prepare for Phase 2**:
   - Integrate with Delta Table in Azure Fabric Lakehouse
   - Add search and retrieval functionality
   - Deploy publicly or internally via Streamlit Cloud or Azure App Service

---

##  Project Structure (Planned)


