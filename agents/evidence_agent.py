def evidence_agent(state: dict) -> dict:
    investigation = state["investigation"]

    state["evidence"] = {
        "customer_verified": investigation["customer"] is not None,
        "prior_complaint_count": len(investigation["complaints"]),
        "related_transaction_count": len(investigation["transactions"]),
        "open_fraud_alert_count": len(investigation["fraud_alerts"]),
        "crm_context_count": len(investigation["crm_interactions"]),
        "items": {
            "customer": investigation["customer"],
            "complaints": investigation["complaints"],
            "transactions": investigation["transactions"],
            "fraud_alerts": investigation["fraud_alerts"],
            "crm_interactions": investigation["crm_interactions"],
        },
    }
    return state
