from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.modify',
          'https://www.googleapis.com/auth/calendar.readonly']

def authenticate_gmail():
    creds = None
    if os.path.exists("gmail_token.pkl"):
        with open("gmail_token.pkl", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials_gmail.json", SCOPES)
        creds = flow.run_local_server(port=0)

        with open("gmail_token.pkl", "wb") as token:
            pickle.dump(creds, token)

    service = build("gmail", "v1", credentials=creds)
    return service
