import os
from urllib.parse import quote

from services.http_client import get_json


BASE_URL = os.getenv("CRM_API_URL", "http://127.0.0.1:8005")


def get_customer_interactions(customer_id: str):
    return get_json(BASE_URL, f"/interactions/customer/{quote(customer_id)}", default=[])
