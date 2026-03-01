from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

class EmailClassifier:

    def classify(self, text):

        prompt = f"""
You are an executive email triage system.

Classify the following email into EXACTLY ONE of these:

- Very Important
- Medium Important
- Not Important

Definitions:

Very Important:
Executive-level, legal, financial, urgent deadlines,
high authority sender, sensitive matters.

Medium Important:
Project discussions, follow-ups, internal coordination.

Not Important:
Basic scheduling, confirmations, small talk,
simple timing questions, low impact messages.

Email:
{text}

Respond with only the category name.
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        category = response.choices[0].message.content.strip()

        return category, 0.95
