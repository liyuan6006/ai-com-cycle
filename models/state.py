from typing import TypedDict


class WorkflowState(TypedDict, total=False):
    request: dict
    intake: dict
    classification: dict
    investigation: dict
    evidence: dict
    resolution: dict
    response: dict
    reporting: dict
