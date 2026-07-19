import json
import os

from openai import OpenAI
from config import OPENAI_API_KEY

class AIClassificationService:
    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def classify_complaint(self, message: str) -> dict:
        prompt = f"""
You are a Wells Fargo complaint classification assistant.

Classify the complaint.

Return ONLY valid JSON.

Categories:
- Fraud
- Card
- ATM
- General Banking

Priority:
- Critical
- High
- Medium

Complaint:
{message}

Example:

{{
    "category":"Fraud",
    "priority":"Critical"
}}
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        return json.loads(response.choices[0].message.content)


ai_classification_service = AIClassificationService()
