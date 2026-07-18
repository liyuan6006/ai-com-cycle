from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Transaction API")


class Transaction(BaseModel):
    id: str
    account_id: str
    amount: float
    merchant: str
    type: str
    status: str
    created_at: datetime


transactions = [
    Transaction(id="T9001", account_id="A3001", amount=-84.27, merchant="Metro Grocery", type="Debit", status="Posted", created_at=datetime.now()),
    Transaction(id="T9002", account_id="A3002", amount=2500.00, merchant="Payroll", type="Credit", status="Posted", created_at=datetime.now()),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "transaction-api"}


@app.get("/transactions")
def list_transactions():
    return transactions


@app.get("/transactions/{transaction_id}")
def get_transaction(transaction_id: str):
    for transaction in transactions:
        if transaction.id == transaction_id:
            return transaction
    raise HTTPException(404, "Transaction not found")


@app.get("/transactions/account/{account_id}")
def get_account_transactions(account_id: str):
    return [transaction for transaction in transactions if transaction.account_id == account_id]

