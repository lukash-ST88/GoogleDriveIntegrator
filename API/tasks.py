from celery import shared_task
from .google_drive_service_account import create_file


@shared_task()
def create_file_task(title, content):
    create_file(title, content)

