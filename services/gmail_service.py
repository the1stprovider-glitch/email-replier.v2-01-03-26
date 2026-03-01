import base64

def get_messages(service, max_results=20):
    results = service.users().messages().list(
        userId='me', maxResults=max_results).execute()

    messages = results.get('messages', [])
    emails = []

    for msg in messages:
        txt = service.users().messages().get(
            userId='me', id=msg['id']).execute()

        payload = txt['payload']
        headers = payload['headers']

        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        sender = next(h['value'] for h in headers if h['name'] == 'From')

        emails.append({
            "id": msg['id'],
            "subject": subject,
            "sender": sender,
            "snippet": txt['snippet']
        })

    return emails
