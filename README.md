**Full automation helps reduce manual uploads from hours to seconds!**

This repo contains a simplified version of an automation I built at work to streamline monthly file uploads and permission management for each files in Google Drive folder.

⚠️ **Note**
This is a sanitized, public-safe version.  
No credentials or company data included.  

**🎯 Brief Concept**
Every month, I need to upload Excel files to Google Drive, into folders with a fairly deep structure. I need to upload the template file to all folders, automatically rename it according to the folder name, and grant access to each user's email.

**Scripts Overview**
1. upload_automation_sanitized.py
    Automates uploading Excel files to designated folders on Google Drive. Features include:
     - Copying a template file per folder
     - Renaming files automatically
     - Uploading to the respective folders
2. add_access_sanitized.py
    Automates adding access permissions to Google Drive folders or files.

Both scripts are self-contained and rely only on standard Python libraries and pydrive

**Tech Stack**
- Python + Google Drive API
- JSON config for flexible structure
- OAuth2 user authorization

**🛠️ Quick setup**
    1. Enable Google Drive API in Google Cloud Console
    2. Download credentials.json (OAuth client ID)
    3. Create config.json and email_map.json

**Files**
| File | Description |
|------|--------------|
| `upload_automation_sanitized.py` | Demo of auto-upload process |
| `add_access_sanitized.py` | Adds editor permissions to files |
| `config.example.json` | Example configuration |
| `email_map.example.json` | Dummy email mapping |
| `.gitignore` | Hides sensitive files |

**💡 Personal insight**
Initially, this was just a small idea to ease my monthly workload. But once implemented, the results were remarkable:
    1. Routine work can be fully automated
    2. Risk of human error drastically reduced
    3. All files and dealer access are automatically recorded
This is a simple example of how small automation can make a huge impact on daily workflows.

