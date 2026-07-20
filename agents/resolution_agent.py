# def resolution_agent(state: dict) -> dict:
#     classification = state["classification"]
#     evidence = state["evidence"]

#     if classification["needs_fraud_review"] or evidence["open_fraud_alert_count"]:
#         next_action = "Escalate to Fraud Team"
#         status = "Escalated"
#         owner = "Fraud Team"
#     elif classification["priority"] == "High":
#         next_action = "Open priority operations case"
#         status = "Pending Operations Review"
#         owner = "Customer Care"
#     else:
#         next_action = "Route to customer care queue"
#         status = "Queued"
#         owner = "Customer Care"

#     state["resolution"] = {
#         "next_action": next_action,
#         "status": status,
#         "summary": f"{classification['priority']} priority {classification['category']} complaint.",
#         "owner": owner,
#     }
#     return state

from services.ai_resolution_service import ai_resolution_service
from MCP.client import jira_mcp_client


def resolution_agent(state: dict) -> dict:

    result = ai_resolution_service.recommend_resolution(
        classification=state["classification"],
        evidence=state["evidence"],
    )

    state["resolution"] = {
        "next_action": result["next_action"],
        "status": result["status"],
        "summary": result["summary"],
        "owner": result["owner"],
    }

    if result.get("create_jira", True):

        jira = jira_mcp_client.create_issue(
            summary=result["jira"]["summary"],
            description=result["jira"]["description"],
            priority=result["jira"]["priority"],
            assignee=result["jira"]["assignee"],
        )

        state["jira"] = jira

    return state
