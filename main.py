import argparse
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
from datetime import datetime

def upload_file(service, file_path, folder_id, email_address):
    try:
        # Extract the file name from the file path
        file_name = os.path.basename(file_path)
        
        # Append the date to the file name to avoid overwriting files
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name_with_date = f"{timestamp}_{file_name}"
        
        # Define the file metadata and specify the parent folder
        file_metadata = {
            'name': file_name_with_date,
            'parents': [folder_id]
        }

        # Specify the file to be uploaded
        media = MediaFileUpload(file_path, resumable=True)

        # Upload the file to the specified folder in Google Drive
        uploaded_file = service.files().create(body=file_metadata, media_body=media, fields='id, parents').execute()

        # Print file ID and folder ID where it was uploaded
        print(f'Uploaded {file_name} to Google Drive with ID: {uploaded_file.get("id")}')

        # Share the file with your personal Google account
        user_permission = {
            'type': 'user',
            'role': 'writer',
            'emailAddress': email_address
        }
        service.permissions().create(
            fileId=uploaded_file['id'],
            body=user_permission,
            fields='id',
        ).execute()

    except HttpError as error:
        print(f'An error occurred while uploading {file_name}: {error}')
    except Exception as e:
        print(f'An unexpected error occurred while uploading {file_name}: {e}')

# usage:
# python backup_script.py --directory "C:/path/to/your/backup/files" --folder_id "1oNFK9bCu7DCwOheQaz9aav0l5LSYfOsA" --key_file "upload-drive-433718-c39e41e16470.json" --email "sajidjqurashi1@gmail.com"

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Backup files to Google Drive using a service account.")
    parser.add_argument('--directory', required=True, help="Directory containing files to back up")
    parser.add_argument('--folder_id', required=True, help="Google Drive folder ID where files will be uploaded")
    parser.add_argument('--key_file', required=True, help="Path to the service account JSON key file")
    parser.add_argument('--email', required=True, help="Email address to share the uploaded files with")
    args = parser.parse_args()

    # Authenticate using the service account
    creds = Credentials.from_service_account_file(args.key_file, scopes=['https://www.googleapis.com/auth/drive'])
    service = build('drive', 'v3', credentials=creds)

    # Iterate through all files in the backup directory
    for file_name in os.listdir(args.directory):
        file_path = os.path.join(args.directory, file_name)
        if os.path.isfile(file_path):
            upload_file(service, file_path, args.folder_id, args.email)

if __name__ == '__main__':
    main()
