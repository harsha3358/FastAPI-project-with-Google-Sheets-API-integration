import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import os
import certifi
os.environ['SSL_CERT_FILE'] = certifi.where()

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "11QcpK8lHNj8hUhSJuby8nO70QWj9-hd6cT6Ea3yiIoI"
RANGE = "Sheet1!A:D"  

try:
    creds = Credentials.from_service_account_file(
        "credentials.json", scopes=SCOPES
    )

    service = build("sheets", "v4", credentials=creds)
    sheet = service.spreadsheets()
    GOOGLE_READY = True

except Exception as e:
    print("Google Initialization Failed:", e)
    GOOGLE_READY = False


def read_users():
    if not GOOGLE_READY:
        return []

    try:
        result = sheet.values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE
        ).execute()
        return result.get("values", [])
    except Exception as e:
        print("Read Error:", e)
        return []


def add_user(email, password_hash, role):
    if not GOOGLE_READY:
        print("Google not connected.")
        return False

    try:
        timestamp = str(datetime.now())

        sheet.values().append(
            spreadsheetId=SPREADSHEET_ID,
            range=RANGE,
            valueInputOption="RAW",
            body={
                "values": [[email, password_hash, role, timestamp]]
            }
        ).execute()

        return True

    except Exception as e:
        print("Write Error:", e)
        return False