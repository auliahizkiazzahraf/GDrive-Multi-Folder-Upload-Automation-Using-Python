**Full automation helps reduce manual uploads from hours to seconds!**

This repo contains a simplified version of an automation I built at work to streamline monthly file uploads and permission management for each dealer's Google Drive folder.

⚠️ **Note**
This is a sanitized, public-safe version.  
No credentials or company data included.  

**🎯 Brief Concept**
Every month, I need to upload Excel files to the company’s Google Drive, into folders with a fairly deep structure. Each dealer has their own folder, and inside it, there are year folders (2025, 2026, etc.).

I need to upload the template file to all dealer folders, automatically rename it according to the dealer code, and grant access to each dealer’s email.

**Scripts Overview**
1. upload_automation_sanitized.py
    Automates uploading Excel files to designated folders on Google Drive. Features include:
     - Copying a template file per dealer
     - Renaming files automatically
     - Uploading to the respective dealer folders
2. add_access_sanitized.py
    Automates adding access permissions to Google Drive folders or files.

Both scripts are self-contained and rely only on standard Python libraries and pydrive

**Features**
- Automatically uploads a single Excel template to 70+ dealer folders.
- Renames each file using the dealer code.
- Optionally grants access to different emails per dealer.

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

