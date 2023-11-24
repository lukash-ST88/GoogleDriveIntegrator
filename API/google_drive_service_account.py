from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

creds_file = os.path.join(BASE_DIR, 'Service_account_secrets.json')


def create_file(file_name, file_content):
    credentials = service_account.Credentials.from_service_account_file(
        creds_file, scopes=['https://www.googleapis.com/auth/drive']
    )
    service = build("drive", "v3", credentials=credentials)
    folder_metadata = {
        'name': file_name,
        "parents": ['1z4hcK_NJ8-1cfPd6CV0pjNxo48Gmww8n'],
        'mimeType': 'application/vnd.google-apps.file',
    }
    with open(file_name, 'w') as file:
        file.write(file_content)

    media = MediaFileUpload(os.path.join(BASE_DIR, file_name), mimetype='text/plain')

    request = service.files().create(body=folder_metadata, media_body=media, fields='id')
    response = request.execute()

    if os.path.exists(file_name):
        os.remove(file_name)

    print('Новый файл успешно создан. Идентификатор файла: %s' % response)
