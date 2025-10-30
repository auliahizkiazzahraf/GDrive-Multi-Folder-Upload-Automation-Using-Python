"""
Google Drive Upload Automation (Sanitized Version)
-------------------------------------------------
This script automatically uploads a single Excel template file
to each dealer’s yearly folder (e.g., 2025) inside region folders (R1, R2).
Filename pattern:
  "10. [3-char dealer code] - Template Master Claim Program Oktober 2025.xlsx"

SAFE TO SHARE:
- No credentials or company data
- Uses config.example.json for structure
"""

import os
import shutil
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import json

SCOPES = ['https://www.googleapis.com/auth/drive.file']

def auth():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('drive', 'v3', credentials=creds)

def find_folder_by_name(drive, name, parent_id=None):
    q = f"mimeType='application/vnd.google-apps.folder' and name='{name}'"
    if parent_id:
        q += f" and '{parent_id}' in parents"
    results = drive.files().list(q=q, fields='files(id,name)').execute()
    return results.get('files', [])

def list_folders_in_parent(drive, parent_id):
    q = f"mimeType='application/vnd.google-apps.folder' and '{parent_id}' in parents"
    res = drive.files().list(q=q, fields='files(id,name)').execute()
    return res.get('files', [])

def upload_to_all_dealers(template_path, year, root_folder):
    drive = auth()
    root = find_folder_by_name(drive, root_folder)[0]
    regions = list_folders_in_parent(drive, root['id'])

    for region in regions:
        if region['name'] not in ['R1', 'R2']:
            continue
        dealers = list_folders_in_parent(drive, region['id'])
        for dealer in dealers:
            code = dealer['name'][:3]
            folder_2025 = find_folder_by_name(drive, year, dealer['id'])
            if not folder_2025:
                continue
            folder_id = folder_2025[0]['id']
            target_filename = f"10. {code} - Template Master Claim Program Oktober {year}.xlsx"
            tmp = f".tmp_{target_filename}"
            shutil.copy(template_path, tmp)
            media = MediaFileUpload(tmp)
            drive.files().create(body={'name': target_filename, 'parents': [folder_id]}, media_body=media).execute()
            os.remove(tmp)
            print(f"Uploaded {target_filename}")

if __name__ == "__main__":
    upload_to_all_dealers("template.xlsx", "2025", "Claim Sales Program")
