import os

from services.http_client import post_json


BASE_URL = os.getenv("EMAIL_API_URL", "http://127.0.0.1:8006")


def send_email(to_address: str, subject: str, body: str):
    payload = {
        "to_address": to_address,
        "subject": subject,
        "body": body,
        "status": "Queued",
    }
    return post_json(BASE_URL, "/emails", payload, default={"status": "Unavailable"})
