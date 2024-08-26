
# Google Drive Backup Script

This Python script automates the process of backing up files from a specified directory to a Google Drive folder using a service account. The script also automatically shares the uploaded files with a specified email address.

## Features

- **Automated Uploads**: Uploads all files in the specified directory to Google Drive.
- **Timestamped Backups**: Each file is renamed with a timestamp to prevent overwriting.
- **Permission Management**: Automatically shares the uploaded files with your personal Google account.

## Requirements

- Python 3.x
- Google API Python Client
- Service account JSON key file with appropriate permissions

## Setup

1. Clone the repository or download the script.

2. Install the required Python packages:

   ```bash
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

3. Place your service account JSON key file in a secure location.

## Usage

To back up files, run the script with the following command-line arguments:

```bash
python backup_script.py --directory "C:/path/to/your/backup/files" --folder_id "Google_Drive_Folder_ID" --key_file "path/to/service-account-key.json" --email "your-email@gmail.com"
```

### Command-Line Arguments

- `--directory`: The directory containing files to back up.
- `--folder_id`: The Google Drive folder ID where files will be uploaded.
- `--key_file`: The path to your service account JSON key file.
- `--email`: The email address to share the uploaded files with.

### Example

```bash
python backup_script.py --directory "C:/backups" --folder_id "your-google-drive-folder-id" --key_file "service-account.json" --email "your-email@gmail.com"
```

## Automating Backups

You can automate the script to run at regular intervals using a task scheduler (e.g., Windows Task Scheduler, cron jobs on Unix-like systems).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
