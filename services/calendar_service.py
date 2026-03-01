import requests
from auth.microsoft_auth import get_token

def get_calendar_events():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    url = "https://graph.microsoft.com/v1.0/me/calendarview?startDateTime=2026-03-01T00:00:00&endDateTime=2026-03-07T23:59:00"
    return requests.get(url, headers=headers).json()
