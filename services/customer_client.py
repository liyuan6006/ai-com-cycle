import os
from urllib.parse import quote

from services.http_client import get_json


BASE_URL = os.getenv("CUSTOMER_API_URL", "http://127.0.0.1:8001")


def get_customer(customer_id: str):
    return get_json(BASE_URL, f"/customers/{quote(customer_id)}")
