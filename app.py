import streamlit as st
from auth.gmail_auth import authenticate_gmail
from services.gmail_service import get_messages
from services.outlook_service import get_outlook_messages
from models.classifier import EmailClassifier
from models.response_generator import generate_response
from models.scheduling_engine import extract_time_request, generate_availability

st.set_page_config(layout="wide")
st.title("AI Executive Email Assistant")

classifier = EmailClassifier()

if st.button("Connect Gmail"):
    gmail_service = authenticate_gmail()
    emails = get_messages(gmail_service)

    for email in emails:
        category, score = classifier.classify(
            email["subject"] + " " + email["snippet"])

        st.subheader(email["subject"])
        st.write("From:", email["sender"])
        st.write("Category:", category)
        st.write("Confidence:", round(score, 3))

        if category == "Not Important" and score > 0.9:
            if extract_time_request(email["snippet"]):
                availability = generate_availability(None)
            else:
                availability = None

            reply = generate_response(email["snippet"], None, availability)

            st.text_area("Suggested Reply", reply)
