from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Card API")


class Card(BaseModel):
    id: str
    customer_id: str
    account_id: str
    last_four: str
    card_type: str
    status: str


cards = [
    Card(id="CARD501", customer_id="C1001", account_id="A3001", last_four="1188", card_type="Debit", status="Active"),
    Card(id="CARD502", customer_id="C1002", account_id="A3002", last_four="4421", card_type="Credit", status="Frozen"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "card-api"}


@app.get("/cards")
def list_cards():
    return cards


@app.get("/cards/{card_id}")
def get_card(card_id: str):
    for card in cards:
        if card.id == card_id:
            return card
    raise HTTPException(404, "Card not found")


@app.patch("/cards/{card_id}/status")
def update_status(card_id: str, status: str):
    for card in cards:
        if card.id == card_id:
            card.status = status
            return card
    raise HTTPException(404, "Card not found")

