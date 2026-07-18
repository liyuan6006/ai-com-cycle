from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Complaint API")


class Complaint(BaseModel):
    id: str
    customer_id: str
    title: str
    category: str
    priority: str
    status: str
    created_at: datetime


complaints = [
    Complaint(id="CMP1001", customer_id="C1001", title="ATM did not dispense cash", category="ATM", priority="High", status="Open", created_at=datetime.now()),
    Complaint(id="CMP1002", customer_id="C1002", title="Duplicate card charge", category="Card", priority="Medium", status="Investigating", created_at=datetime.now()),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "complaint-api"}


@app.get("/complaints")
def list_complaints():
    return complaints


@app.get("/complaints/{complaint_id}")
def get_complaint(complaint_id: str):
    for complaint in complaints:
        if complaint.id == complaint_id:
            return complaint
    raise HTTPException(404, "Complaint not found")


@app.post("/complaints")
def create_complaint(complaint: Complaint):
    complaints.append(complaint)
    return {"message": "Complaint created", "complaint": complaint}

