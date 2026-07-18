import os

from services.http_client import post_json


BASE_URL = os.getenv("NOTES_API_URL", "http://127.0.0.1:8007")


def create_note(customer_id: str, title: str, body: str):
    payload = {
        "customer_id": customer_id,
        "title": title,
        "body": body,
        "author": "LangGraph Workflow",
    }
    return post_json(BASE_URL, "/notes", payload, default={"status": "Unavailable"})
