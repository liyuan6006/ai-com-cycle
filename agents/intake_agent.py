from services.customer_client import get_customer


def intake_agent(state: dict) -> dict:
    request = state["request"]
    customer_id = request["customer_id"]
    customer = get_customer(customer_id)

    state["intake"] = {
        "customer_id": customer_id,
        "channel": request.get("channel", "Web"),
        "message": request["message"],
        "customer": customer,
        "valid_customer": customer is not None,
    }
    return state
