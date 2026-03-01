import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

GMAIL_CLIENT_SECRET = "credentials_gmail.json"
MS_CLIENT_ID = os.getenv("MS_CLIENT_ID")
MS_CLIENT_SECRET = os.getenv("MS_CLIENT_SECRET")
MS_TENANT_ID = os.getenv("MS_TENANT_ID")

AUTO_SEND_THRESHOLD = 0.92
MODEL_NAME = "microsoft/deberta-v3-large"
