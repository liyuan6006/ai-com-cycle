# def classification_agent(state: dict) -> dict:
#     message = state["intake"]["message"].lower()

#     if any(term in message for term in ["fraud", "unauthorized", "stolen", "did not authorize"]):
#         category = "Fraud"
#         priority = "Critical"
#     elif any(term in message for term in ["card", "charge", "charged", "debit", "credit"]):
#         category = "Card"
#         priority = "High"
#     elif any(term in message for term in ["atm", "cash"]):
#         category = "ATM"
#         priority = "High"
#     else:
#         category = "General Banking"
#         priority = "Medium"

#     state["classification"] = {
#         "category": category,
#         "priority": priority,
#         "needs_fraud_review": category == "Fraud",
#     }
#     return state


from services.ai_classification_service import ai_classification_service


def classification_agent(state: dict) -> dict:

    message = state["intake"]["message"]

    result = ai_classification_service.classify_complaint(message)

    state["classification"] = {
        "category": result["category"],
        "priority": result["priority"],
        "needs_fraud_review": result["category"] == "Fraud",
    }

    return state
