import json

from openai import OpenAI

from config import OPENAI_API_KEY


class AIResolutionService:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def recommend_resolution(
        self,
        classification: dict,
        evidence: dict,
    ) -> dict:

        prompt = f"""
You are an experienced Wells Fargo complaint resolution specialist.

Your job is to determine the best next action based on the complaint classification and evidence.

Return ONLY valid JSON.

Possible Owners:
- Fraud Team
- Customer Care
- Operations

Possible Status:
- Escalated
- Pending Operations Review
- Queued
- Resolved

Example:

{{
    "next_action":"Escalate to Fraud Team",
    "status":"Escalated",
    "owner":"Fraud Team",
    "summary":"Evidence strongly supports potential fraud. Escalating for investigation."
}}

Classification:

{json.dumps(classification, indent=2)}

Evidence:

{json.dumps(evidence, indent=2)}
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return json.loads(response.choices[0].message.content)


ai_resolution_service = AIResolutionService()