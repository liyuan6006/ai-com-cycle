import json

from openai import OpenAI

from config import OPENAI_API_KEY


class AIEvidenceService:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def analyze_evidence(
        self,
        customer_message: str,
        classification: dict,
        investigation: dict,
    ) -> dict:

        prompt = f"""
You are an experienced Wells Fargo complaint investigator.

You are given:

1. Customer complaint
2. Complaint classification
3. Investigation results

Your job is to analyze all available evidence.

Return ONLY valid JSON.

Example:

{{
    "summary": "Customer's complaint is supported by the available evidence.",
    "key_findings": [
        "Open fraud alert exists.",
        "Customer previously contacted support."
    ],
    "risk_assessment": "High",
    "recommended_focus": "Investigate disputed card transactions.",
    "confidence": "High"
}}

Customer Complaint:
{customer_message}

Classification:
{json.dumps(classification, indent=2)}

Investigation:
{json.dumps(investigation, indent=2)}
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


ai_evidence_service = AIEvidenceService()