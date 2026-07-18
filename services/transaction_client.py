import os
from urllib.parse import quote

from services.http_client import get_json


BASE_URL = os.getenv("TRANSACTION_API_URL", "http://127.0.0.1:8003")


def get_customer_transactions(customer_id: str):
    transactions = []
    for account_id in _demo_accounts_for_customer(customer_id):
        transactions.extend(get_json(BASE_URL, f"/transactions/account/{quote(account_id)}", default=[]))
    return transactions


def _demo_accounts_for_customer(customer_id: str):
    return {
        "C1001": ["A3001"],
        "C1002": ["A3002"],
    }.get(customer_id, [])
