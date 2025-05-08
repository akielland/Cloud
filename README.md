# Cloud



## Strategy

 Component               Tool/Approach                             | Comments                                                                  

| **IDE**                 VS Code                                   | Great choice for Python + Streamlit + Git. Use extensions for GitHub, Jupyter, and Azure. |
| **Version Control**    | Git + GitHub                              | Excellent. Start with a private repo; use issues and branches as you go.                  |
| **Frontend**           | Streamlit                                 | Ideal for this pilot. Easy to integrate with Python logic.                                |
| **Backend**            | Python modules + Azure SDK                | Good for organizing logic (uploading, metadata handling).                                 |
| **Notebook Support**   | Jupyter for exploration, modules for prod | Perfect — notebook for testing logic, package into modules for reuse.                     |
| **Deployment (later)** | Streamlit on Azure VM / Streamlit Cloud   | Easy to set up once the app works locally.                                                |
| **AI Support**         | ChatGPT as pair-programmer                | Efficient. Models like GPT-4-turbo are ideal. You’re using the right one now.             |








data_upload_portal/
│
├── app.py                    # Main Streamlit app
├── .streamlit/config.toml   # App settings (title, theme)
│
├── requirements.txt          # Python dependencies
├── README.md                 # Project overview
│
├── modules/                 # Custom Python logic
│   ├── uploader.py          # File handling and Azure upload
│   ├── metadata.py          # Metadata validation/storage
│
├── notebooks/               # Jupyter notebooks for exploration
│   └── test_metadata.ipynb
│
└── tests/                   # Later: unit tests
