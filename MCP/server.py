import requests
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Jira MCP HTTP Server")

JIRA_API = "http://127.0.0.1:8005"
MCP_HOST = "127.0.0.1"
MCP_PORT = 8006


class CreateJiraIssueRequest(BaseModel):
    summary: str
    description: str
    priority: str
    assignee: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "jira-mcp-http-server"}


@app.post("/tools/create_jira_issue")
def create_jira_issue(
    request: CreateJiraIssueRequest,
):
    """
    Create a Jira issue.
    """

    try:
        response = requests.post(
            f"{JIRA_API}/api/issues",
            json={
                "summary": request.summary,
                "description": request.description,
                "priority": request.priority,
                "assignee": request.assignee,
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }


@app.get("/tools/get_latest_jira_issue")
def get_latest_jira_issue():
    """
    Get the latest Jira issue.
    """

    try:
        response = requests.get(
            f"{JIRA_API}/api/issues/latest",
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }


if __name__ == "__main__":
    uvicorn.run(app, host=MCP_HOST, port=MCP_PORT)
