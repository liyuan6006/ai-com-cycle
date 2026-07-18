from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Risk API")


class RiskProfile(BaseModel):
    id: str
    customer_id: str
    credit_score: int
    risk_rating: str
    notes: str


risk_profiles = [
    RiskProfile(id="R4001", customer_id="C1001", credit_score=742, risk_rating="Low", notes="Stable income and long account history."),
    RiskProfile(id="R4002", customer_id="C1002", credit_score=611, risk_rating="Medium", notes="Recent overdrafts and high utilization."),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "risk-api"}


@app.get("/risk-profiles")
def list_profiles():
    return risk_profiles


@app.get("/risk-profiles/customer/{customer_id}")
def get_customer_risk(customer_id: str):
    for profile in risk_profiles:
        if profile.customer_id == customer_id:
            return profile
    raise HTTPException(404, "Risk profile not found")

