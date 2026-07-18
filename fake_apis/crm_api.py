from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank CRM API")


class Interaction(BaseModel):
    id: str
    customer_id: str
    channel: str
    summary: str
    owner: str
    created_at: datetime


interactions = [
    Interaction(id="CRM5001", customer_id="C1001", channel="Phone", summary="Asked about mortgage rates.", owner="Sam Patel", created_at=datetime.now()),
    Interaction(id="CRM5002", customer_id="C1002", channel="Branch", summary="Requested debit card replacement.", owner="Nina Cruz", created_at=datetime.now()),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "crm-api"}


@app.get("/interactions")
def list_interactions():
    return interactions


@app.get("/interactions/customer/{customer_id}")
def get_customer_interactions(customer_id: str):
    return [interaction for interaction in interactions if interaction.customer_id == customer_id]


@app.post("/interactions")
def create_interaction(interaction: Interaction):
    interactions.append(interaction)
    return {"message": "Interaction logged", "interaction": interaction}

