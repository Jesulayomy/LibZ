"""
    This module contains the Manager class
    (Mostly forcreating folders for users)
"""
from __future__ import print_function

import os.path  # To confirm the token presence (No need to sign in)
import fitz

from datetime import datetime
from google.auth.transport.requests import Request
# Used for credential
from google.oauth2.credentials import Credentials
# Used to get credentials from token.json
from google_auth_oauthlib.flow import InstalledAppFlow
# Helps create the file
from googleapiclient.discovery import build
# This is used to build the service
from googleapiclient.errors import HttpError
# Handles error in requests
from googleapiclient.http import (
    MediaFileUpload,
    MediaIoBaseUpload,
)
# Creates a media file to upload
from mimetypes import guess_type, guess_extension
from PIL import Image
from typing import (
    Dict,
    Type,
    Union,
)

# from models.base import Base
from models.book import Book
from models.user import User


class Manager:
    """ Manager class for handling requests for important functions """

    CREDS = None
    SCOPES = [
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive.metadata.readonly',
        ]

    SERVICE = None

    def __init__(self):
        """ Initialization of the Manager and service """
        if os.path.exists('token.json'):
            Manager.CREDS = Credentials.from_authorized_user_file(
                'token.json',
                Manager.SCOPES
            )
        self.validate_creds(Manager.CREDS)
        self.get_service(Manager.CREDS)

    def validate_creds(self, creds):
        """
            Validates the credentials sent or generates a new one
        """
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json',
                    Manager.SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as tokenfile:
                tokenfile.write(creds.to_json())

    def get_service(self, creds):
        """ Builds a service object for the api """
        try:
            Manager.SERVICE = build('drive', 'v3', credentials=creds)
        except HttpError as err:
            print(err)

    def create_user_folder(self, user: Type[User]):
        """ Create a folder for the user """
        if Manager.SERVICE is None:
            return None
        folder_metadata = {
            'name': user.id,
            'mimeType': 'application/vnd.google-apps.folder',
            'description': f'Uploaded by: {user.display_name}'
        }

        folder = Manager.SERVICE.files().create(
            body=folder_metadata, fields='id').execute()

        return folder.get('id')

    def create_book(self, parent, file):
        """ Creates a book in the user's folder """

        if Manager.SERVICE is None:
            return None
        mimetype = guess_type(file.filename)[0]
        extension = guess_extension(mimetype, strict=False)
        filename = file.filename
        if extension:
            if filename[len(filename) - len(extension):] != extension:
                filename = filename + extension

        self.create_thumbnail(file)
        file_metadata = {
            'name': filename,
            'parents': [parent]
        }
        image_metadata = {
            'name': file.filename[:-2] + 'ng',
            'parents': [parent]
        }
        file_media = MediaIoBaseUpload(file.stream, mimetype=mimetype)
        image_media = MediaFileUpload('{}'.format(
            file.filename[:-2] + 'ng'), mimetype='image/png')
        try:
            file = Manager.SERVICE.files().create(
                body=file_metadata,
                media_body=file_media,
                fields='*'
            ).execute()
            Manager.SERVICE.permissions().create(
                fileId=file.get('id'),
                body={
                    'role': 'reader',
                    'type': 'anyone',
                }
            ).execute()
            image = Manager.SERVICE.files().create(
                body=image_metadata,
                media_body=image_media,
                fields='*'
            ).execute()
            Manager.SERVICE.permissions().create(
                fileId=image.get('id'),
                body={
                    'role': 'reader',
                    'type': 'anyone',
                }
            ).execute()
        except Exception as e:
            print(e)
            return None
        result = {
            'downloadLink': file.get('webContentLink'),
            'driveId': file.get('id'),
            'driveName': file.get('name'),
            'iconLink': file.get('iconLink'),
            'thumbnailLink': image.get(
                'webViewLink').split('view')[0] + 'preview',
            'size': int(file.get('size')),
            'parents': parent,
        }
        return result

    def delete_book(self, driveId: str):
        """ Deletes the book data from the drive """
        if Manager.SERVICE is None:
            return None
        try:
            Manager.SERVICE.files().delete(fileId=driveId).execute()
        except Exception as e:
            print(e)
            return None

    def create_thumbnail(self, file):
        """ Creates a thumbnail for the pdf """
        pdf_doc = fitz.open(stream=file.read(), filetype='pdf')
        page = pdf_doc.load_page(0)
        width_ratio = 400 / page.bound().width
        height_ratio = 400 / page.bound().height
        min_ratio = min(width_ratio, height_ratio)
        matrix = fitz.Matrix(min_ratio, min_ratio)
        pix = page.get_pixmap(matrix=matrix)
        pil_image = Image.frombytes(
            "RGB",
            [pix.width, pix.height],
            pix.samples
        )
        pil_image = pil_image.resize((400, 400))
        pil_image.save(file.filename[:-2] + 'ng')
        pdf_doc.close()
