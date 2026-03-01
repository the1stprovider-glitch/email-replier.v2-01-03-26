import json

def save_feedback(email_id, correct_category):
    data = {"email_id": email_id, "label": correct_category}

    with open("feedback.json", "a") as f:
        f.write(json.dumps(data) + "\n")
