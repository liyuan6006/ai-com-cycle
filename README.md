# Fake Bank System

This demo models a customer complaint workflow:

```text
Customer
  -> FastAPI Gateway
  -> LangGraph Workflow
  -> Intake Agent
  -> Classification Agent
  -> Investigation Agent
  -> Evidence Agent
  -> Resolution Agent
  -> Response Agent
  -> Reporting Agent
  -> Customer API, Complaint API, Transaction API, Fraud API, CRM API, Email API, Notes API
```

Each downstream service is a standalone FastAPI app module in `fake_apis/` with in-memory sample data. The gateway workflow is organized into `agents/`, `graph/`, `models/`, `prompts/`, and `services/`.

## Gateway

Run the gateway:

```powershell
cd fake-bank-system
uvicorn main:app --reload --port 8000
```

Submit a complaint:

```powershell
Invoke-RestMethod -Method Post http://localhost:8000/complaint-workflow `
  -ContentType "application/json" `
  -Body '{"customer_id":"C1001","message":"My card was charged twice at Metro Grocery.","channel":"Web"}'
```

The workflow uses LangGraph when it is installed. If LangGraph is not installed, it runs the same nodes sequentially so the demo remains usable.

## Downstream API Ports

The gateway reads these environment variables, with local defaults:

```text
CUSTOMER_API_URL=http://127.0.0.1:8001
COMPLAINT_API_URL=http://127.0.0.1:8002
TRANSACTION_API_URL=http://127.0.0.1:8003
FRAUD_API_URL=http://127.0.0.1:8004
CRM_API_URL=http://127.0.0.1:8005
EMAIL_API_URL=http://127.0.0.1:8006
NOTES_API_URL=http://127.0.0.1:8007
```

Run a fake downstream API from the app root with:

```powershell
uvicorn fake_apis.customer_api:app --reload --port 8001
```
