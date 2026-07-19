import json

from openai import OpenAI

from config import OPENAI_API_KEY


class AIResponseService:

    def __init__(self):
        self.client = OpenAI(api_key=OPENAI_API_KEY)

    def generate_customer_response(
        self,
        customer_name: str,
        customer_message: str,
        classification: dict,
        resolution: dict,
    ) -> dict:

        prompt = f"""
You are a Wells Fargo Customer Care specialist.

Generate a professional email to the customer.

Requirements:

- Be empathetic.
- Thank the customer.
- Summarize the complaint.
- Explain the current status.
- Explain the next action.
- Do NOT promise an outcome.
- Keep it under 200 words.

Return ONLY valid JSON.

Example:

{{
    "subject":"We received your banking complaint",
    "body":"Dear John,\\n\\nThank you for contacting Wells Fargo..."
}}

Customer Name:
{customer_name}

Customer Complaint:
{customer_message}

Classification:
{json.dumps(classification, indent=2)}

Resolution:
{json.dumps(resolution, indent=2)}
"""

        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            temperature=0.4,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return json.loads(response.choices[0].message.content)


ai_response_service = AIResponseService()