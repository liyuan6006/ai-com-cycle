# def evidence_agent(state: dict) -> dict:
#     investigation = state["investigation"]

#     state["evidence"] = {
#         "customer_verified": investigation["customer"] is not None,
#         "prior_complaint_count": len(investigation["complaints"]),
#         "related_transaction_count": len(investigation["transactions"]),
#         "open_fraud_alert_count": len(investigation["fraud_alerts"]),
#         "crm_context_count": len(investigation["crm_interactions"]),
#         "items": {
#             "customer": investigation["customer"],
#             "complaints": investigation["complaints"],
#             "transactions": investigation["transactions"],
#             "fraud_alerts": investigation["fraud_alerts"],
#             "crm_interactions": investigation["crm_interactions"],
#         },
#     }
#     return state

from services.ai_evidence_service import ai_evidence_service


def evidence_agent(state: dict) -> dict:

    investigation = state["investigation"]

    result = ai_evidence_service.analyze_evidence(
        customer_message=state["intake"]["message"],
        classification=state["classification"],
        investigation=investigation,
    )

    state["evidence"] = {

        # Existing fields
        "customer_verified": investigation["customer"] is not None,
        "prior_complaint_count": len(investigation["complaints"]),
        "related_transaction_count": len(investigation["transactions"]),
        "open_fraud_alert_count": len(investigation["fraud_alerts"]),
        "crm_context_count": len(investigation["crm_interactions"]),

        # AI Analysis
        "summary": result["summary"],
        "key_findings": result["key_findings"],
        "risk_assessment": result["risk_assessment"],
        "recommended_focus": result["recommended_focus"],
        "confidence": result["confidence"],

        # Raw evidence
        "items": {
            "customer": investigation["customer"],
            "complaints": investigation["complaints"],
            "transactions": investigation["transactions"],
            "fraud_alerts": investigation["fraud_alerts"],
            "crm_interactions": investigation["crm_interactions"],
        },
    }

    return state