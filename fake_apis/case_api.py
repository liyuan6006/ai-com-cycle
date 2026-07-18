from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Case API")


class Case(BaseModel):
    id: str
    customer_id: str
    source: str
    title: str
    assigned_to: str
    status: str


cases = [
    Case(id="CASE3001", customer_id="C1001", source="Complaint", title="ATM cash dispute", assigned_to="Operations", status="Open"),
    Case(id="CASE3002", customer_id="C1002", source="Fraud", title="Card fraud investigation", assigned_to="Fraud Team", status="Investigating"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "case-api"}


@app.get("/cases")
def list_cases():
    return cases


@app.get("/cases/{case_id}")
def get_case(case_id: str):
    for case in cases:
        if case.id == case_id:
            return case
    raise HTTPException(404, "Case not found")


@app.patch("/cases/{case_id}/status")
def update_status(case_id: str, status: str):
    for case in cases:
        if case.id == case_id:
            case.status = status
            return case
    raise HTTPException(404, "Case not found")

