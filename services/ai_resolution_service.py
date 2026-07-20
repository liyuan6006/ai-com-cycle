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

Your job is to determine the best next action based on the complaint classification and supporting evidence.

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

Rules:

1. If the complaint requires another team to investigate or perform work,
set "create_jira" to true.

2. If the complaint can be resolved immediately,
set "create_jira" to false.

3. When create_jira is true, populate the jira object.

4. When create_jira is false, set jira to null.

Return JSON in exactly this format:

{{
    "next_action": "Escalate to Fraud Team",
    "status": "Escalated",
    "owner": "Fraud Team",
    "summary": "Evidence strongly supports potential fraud.",

    "create_jira": true,

    "jira": {{
        "summary": "Fraud Complaint",
        "description": "Customer reported unauthorized transactions requiring investigation.",
        "priority": "High",
        "assignee": "Fraud Team"
    }}
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