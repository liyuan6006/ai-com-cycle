from services.complaint_client import get_customer_complaints
from services.crm_client import get_customer_interactions
from services.customer_client import get_customer
from services.fraud_client import get_customer_fraud_alerts
from services.transaction_client import get_customer_transactions


def investigation_agent(state: dict) -> dict:
    customer_id = state["request"]["customer_id"]

    state["investigation"] = {
        "customer": get_customer(customer_id),
        "complaints": get_customer_complaints(customer_id),
        "transactions": get_customer_transactions(customer_id),
        "fraud_alerts": get_customer_fraud_alerts(customer_id),
        "crm_interactions": get_customer_interactions(customer_id),
    }
    return state
