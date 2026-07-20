from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Fake Jira API")

_latest_issue = None
_next_issue_number = 10001


class CreateIssueRequest(BaseModel):
    summary: str
    description: str
    priority: str
    assignee: str


@app.post("/api/issues")
def create_issue(request: CreateIssueRequest):
    global _latest_issue, _next_issue_number

    issue = {
        "ticketId": f"JIRA-{_next_issue_number}",
        "status": "Created",
        "summary": request.summary,
        "description": request.description,
        "priority": request.priority,
        "assignee": request.assignee,
    }

    _next_issue_number += 1
    _latest_issue = issue

    return issue


@app.get("/api/issues/latest")
def get_latest_issue():
    if _latest_issue is None:
        return {
            "ticketId": None,
            "status": "Not Found",
            "message": "No Jira issues have been created.",
        }

    return _latest_issue
