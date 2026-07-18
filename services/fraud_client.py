import os

from services.http_client import get_json


BASE_URL = os.getenv("FRAUD_API_URL", "http://127.0.0.1:8004")


def get_customer_fraud_alerts(customer_id: str):
    alerts = get_json(BASE_URL, "/fraud-alerts", default=[])
    return [item for item in alerts if item.get("customer_id") == customer_id]
