def resolution_agent(state: dict) -> dict:
    classification = state["classification"]
    evidence = state["evidence"]

    if classification["needs_fraud_review"] or evidence["open_fraud_alert_count"]:
        next_action = "Escalate to Fraud Team"
        status = "Escalated"
        owner = "Fraud Team"
    elif classification["priority"] == "High":
        next_action = "Open priority operations case"
        status = "Pending Operations Review"
        owner = "Customer Care"
    else:
        next_action = "Route to customer care queue"
        status = "Queued"
        owner = "Customer Care"

    state["resolution"] = {
        "next_action": next_action,
        "status": status,
        "summary": f"{classification['priority']} priority {classification['category']} complaint.",
        "owner": owner,
    }
    return state
