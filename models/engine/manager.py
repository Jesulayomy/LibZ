""" This module contains the Manager class (Mostly for creating folders for users) """
from __future__ import print_function

import os.path  # To confirm the token presence (No need to sign in)

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
from googleapiclient.http import MediaFileUpload
# Creates a media file to upload

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
        'https://www.googleapis.com/auth/drive.resource',
        'https://www.googleapis.com/auth/drive.metadata.readonly'
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
            return Manager.SERVICE
        except HttpError as err:
            print(err)
        return None

    def create_user_folder(self, user: Type[User]):
        """ Create a folder for the user """
        service = self.get_service(Manager.CREDS)
        if service is None:
            return None
        folder_metadata = {
            'name': user.id,
            'mimeType': 'application/vnd.google-apps.folder',
            'description': f'Uploaded by: {user.display_name}'
        }

        folder = service.files().create(
            body=folder_metadata, fields='id').execute()

        user.folder = folder.get('id')
        print(f'Folder ID: {folder.get("id")}')
        return user

    def refresh_book(self, book: Type[Book]):
        """ Refreshes the book data from the drive """
        pass
