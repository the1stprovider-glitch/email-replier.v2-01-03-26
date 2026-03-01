import msal
import requests
from config import MS_CLIENT_ID, MS_CLIENT_SECRET, MS_TENANT_ID

AUTHORITY = f"https://login.microsoftonline.com/{MS_TENANT_ID}"
SCOPE = ["https://graph.microsoft.com/.default"]

def get_token():
    app = msal.ConfidentialClientApplication(
        MS_CLIENT_ID,
        authority=AUTHORITY,
        client_credential=MS_CLIENT_SECRET
    )

    result = app.acquire_token_for_client(scopes=SCOPE)
    return result["access_token"]
