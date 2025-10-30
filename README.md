# GDrive-Multi-Folder-Upload-Automation-Using-Python
Automates uploading files to multiple Google Drive folders and assigning different email access permissions for each folder using Python and Google Drive API.

**Context**  
This repo contains a simplified version of an automation I built at work to streamline monthly file uploads and permission management for each dealer's Google Drive folder.

**Features**
- Automatically uploads a single Excel template to 70+ dealer folders.
- Renames each file using the dealer code.
- Optionally grants access to different emails per dealer.
- Generates a rekap (summary) of file links for reporting.

**Tech Stack**
- Python + Google Drive API
- JSON config for flexible structure
- OAuth2 user authorization

**Files**
| File | Description |
|------|--------------|
| `upload_automation_sanitized.py` | Demo of auto-upload process |
| `add_access_sanitized.py` | Adds editor permissions to files |
| `config.example.json` | Example configuration |
| `email_map.example.json` | Dummy email mapping |
| `.gitignore` | Hides sensitive files |

⚠️ **Note**
This is a sanitized, public-safe version.  
No credentials or company data included.  

🪄 *Full automation helps reduce manual uploads from hours to seconds!*
