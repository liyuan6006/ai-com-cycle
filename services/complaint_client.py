import os

from services.http_client import get_json


BASE_URL = os.getenv("COMPLAINT_API_URL", "http://127.0.0.1:8002")


def get_customer_complaints(customer_id: str):
    complaints = get_json(BASE_URL, "/complaints", default=[])
    return [item for item in complaints if item.get("customer_id") == customer_id]
