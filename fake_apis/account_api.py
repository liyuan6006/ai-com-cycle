from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Account API")


class Account(BaseModel):
    id: str
    customer_id: str
    account_type: str
    balance: float
    status: str


accounts = [
    Account(id="A3001", customer_id="C1001", account_type="Checking", balance=3820.41, status="Open"),
    Account(id="A3002", customer_id="C1002", account_type="Credit Card", balance=-641.09, status="Open"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "account-api"}


@app.get("/accounts")
def list_accounts():
    return accounts


@app.get("/accounts/{account_id}")
def get_account(account_id: str):
    for account in accounts:
        if account.id == account_id:
            return account
    raise HTTPException(404, "Account not found")


@app.get("/accounts/customer/{customer_id}")
def get_customer_accounts(customer_id: str):
    return [account for account in accounts if account.customer_id == customer_id]

