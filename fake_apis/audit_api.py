from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Audit API")


class AuditEvent(BaseModel):
    id: str
    actor: str
    action: str
    resource: str
    created_at: datetime


audit_events = [
    AuditEvent(id="AUD1001", actor="system", action="customer.created", resource="C1001", created_at=datetime.now()),
    AuditEvent(id="AUD1002", actor="fraud-api", action="alert.opened", resource="F7002", created_at=datetime.now()),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "audit-api"}


@app.get("/audit-events")
def list_events():
    return audit_events


@app.post("/audit-events")
def create_event(event: AuditEvent):
    audit_events.append(event)
    return {"message": "Audit event recorded", "event": event}

