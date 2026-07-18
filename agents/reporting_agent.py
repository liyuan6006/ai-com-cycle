from services.notes_client import create_note


def reporting_agent(state: dict) -> dict:
    customer_id = state["intake"]["customer_id"]
    note_result = create_note(
        customer_id=customer_id,
        title="Complaint workflow completed",
        body=state["resolution"]["summary"],
    )

    state["reporting"] = {
        "workflow_status": "Completed",
        "customer_id": customer_id,
        "category": state["classification"]["category"],
        "priority": state["classification"]["priority"],
        "resolution_status": state["resolution"]["status"],
        "note_result": note_result,
        "metrics": {
            "evidence_items": sum(
                len(value) if isinstance(value, list) else 1
                for value in state["evidence"]["items"].values()
                if value
            ),
        },
    }
    return state
