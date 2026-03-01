from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(email_text, style_embedding, availability=None):

    prompt = f"""
    You are writing in the user's personal style.
    Email received:
    {email_text}

    Availability:
    {availability}

    Respond naturally and professionally.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
