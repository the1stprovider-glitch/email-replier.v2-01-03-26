def extract_time_request(email_text):
    keywords = ["free", "available", "meeting", "schedule"]
    for word in keywords:
        if word in email_text.lower():
            return True
    return False


def generate_availability(calendar_data):
    # Simplified logic
    return "Thursday 2-4pm or Friday 10-12."
