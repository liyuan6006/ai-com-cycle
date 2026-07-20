import requests

MCP_SERVER = "http://127.0.0.1:8006"   # Your MCP server endpoint

class JiraMCPClient:

    def create_issue(
        self,
        summary: str,
        description: str,
        priority: str,
        assignee: str,
    ):

        response = requests.post(
            f"{MCP_SERVER}/tools/create_jira_issue",
            json={
                "summary": summary,
                "description": description,
                "priority": priority,
                "assignee": assignee,
            },
            timeout=30,
        )

        response.raise_for_status()

        return response.json()


jira_mcp_client = JiraMCPClient()
