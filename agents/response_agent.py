from services.email_client import send_email


def response_agent(state: dict) -> dict:
    intake = state["intake"]
    resolution = state["resolution"]
    customer = intake["customer"] or {}

    response = {
        "customer_id": intake["customer_id"],
        "channel": intake["channel"],
        "subject": "We received your banking complaint",
        "body": (
            f"We received your complaint and classified it as {state['classification']['category']}. "
            f"Current status: {resolution['status']}. Next action: {resolution['next_action']}."
        ),
    }

    email_result = None
    if customer.get("email"):
        email_result = send_email(customer["email"], response["subject"], response["body"])

    state["response"] = {
        **response,
        "email_result": email_result,
    }
    return state
