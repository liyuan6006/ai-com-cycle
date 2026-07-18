from agents import (
    classification_agent,
    evidence_agent,
    intake_agent,
    investigation_agent,
    reporting_agent,
    resolution_agent,
    response_agent,
)
from models.state import WorkflowState


WORKFLOW_NODES = (
    ("intake", intake_agent),
    ("classification", classification_agent),
    ("investigation", investigation_agent),
    ("evidence", evidence_agent),
    ("resolution", resolution_agent),
    ("response", response_agent),
    ("reporting", reporting_agent),
)


def run_complaint_workflow(request: dict) -> dict:
    final_state = _run_graph({"request": request})

    return {
        "customer_id": request["customer_id"],
        "intake": final_state["intake"],
        "classification": final_state["classification"],
        "investigation": final_state["investigation"],
        "evidence": final_state["evidence"],
        "resolution": final_state["resolution"],
        "response": final_state["response"],
        "reporting": final_state["reporting"],
    }


def _run_graph(state: WorkflowState) -> WorkflowState:
    try:
        return _run_langgraph(state)
    except ImportError:
        return _run_fallback_graph(state)


def _run_langgraph(state: WorkflowState) -> WorkflowState:
    from langgraph.graph import END, StateGraph

    graph = StateGraph(WorkflowState)
    for node_name, node in WORKFLOW_NODES:
        graph.add_node(node_name, node)

    graph.set_entry_point(WORKFLOW_NODES[0][0])
    for index in range(len(WORKFLOW_NODES) - 1):
        graph.add_edge(WORKFLOW_NODES[index][0], WORKFLOW_NODES[index + 1][0])
    graph.add_edge(WORKFLOW_NODES[-1][0], END)

    return graph.compile().invoke(state)


def _run_fallback_graph(state: WorkflowState) -> WorkflowState:
    for _, node in WORKFLOW_NODES:
        state = node(state)
    return state
