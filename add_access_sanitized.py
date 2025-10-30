"""
Add Email Access to Dealer Files (Sanitized Version)
---------------------------------------------------
This script reads a JSON mapping of dealer codes → emails,
then adds each email as an Editor to the corresponding file
(e.g., '10. [code] - Template ...') in Google Drive.
"""

import json
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/drive']

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

def add_permission(drive, file_id, email):
    permission = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': email
    }
    drive.permissions().create(fileId=file_id, body=permission, sendNotificationEmail=False).execute()

def main():
    drive = auth()
    with open('email_map.example.json') as f:
        email_map = json.load(f)
    # Contoh pencarian file (disederhanakan untuk demo)
    for code, email in email_map.items():
        print(f"Would add {email} to file for dealer {code}")
        # Logic mencari file + menambahkan akses bisa ditambahkan di sini
        # (disensor di versi publik)

if __name__ == "__main__":
    main()
