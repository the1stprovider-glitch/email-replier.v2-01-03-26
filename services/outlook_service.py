import requests
from auth.microsoft_auth import get_token

def get_outlook_messages():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = "https://graph.microsoft.com/v1.0/me/messages?$top=20"
    response = requests.get(url, headers=headers).json()

    emails = []
    for msg in response.get("value", []):
        emails.append({
            "id": msg["id"],
            "subject": msg["subject"],
            "sender": msg["from"]["emailAddress"]["address"],
            "snippet": msg["bodyPreview"]
        })

    return emails
