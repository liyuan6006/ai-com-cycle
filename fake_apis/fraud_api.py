from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Fraud API")


class FraudAlert(BaseModel):
    id: str
    customer_id: str
    transaction_id: str
    reason: str
    severity: str
    status: str


alerts = [
    FraudAlert(id="F7001", customer_id="C1002", transaction_id="T9001", reason="Unusual merchant category", severity="Medium", status="Open"),
    FraudAlert(id="F7002", customer_id="C1001", transaction_id="T9011", reason="Velocity limit exceeded", severity="High", status="Investigating"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "fraud-api"}


@app.get("/fraud-alerts")
def list_alerts():
    return alerts


@app.get("/fraud-alerts/{alert_id}")
def get_alert(alert_id: str):
    for alert in alerts:
        if alert.id == alert_id:
            return alert
    raise HTTPException(404, "Fraud alert not found")


@app.patch("/fraud-alerts/{alert_id}/status")
def update_status(alert_id: str, status: str):
    for alert in alerts:
        if alert.id == alert_id:
            alert.status = status
            return alert
    raise HTTPException(404, "Fraud alert not found")

