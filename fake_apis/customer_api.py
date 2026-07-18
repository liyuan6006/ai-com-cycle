from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Customer API")


class Customer(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    phone: str
    status: str


customers = [
    Customer(id="C1001", first_name="Avery", last_name="Morgan", email="avery.morgan@example.com", phone="555-0101", status="Active"),
    Customer(id="C1002", first_name="Jordan", last_name="Lee", email="jordan.lee@example.com", phone="555-0102", status="Review"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "customer-api"}


@app.get("/customers")
def list_customers():
    return customers


@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    for customer in customers:
        if customer.id == customer_id:
            return customer
    raise HTTPException(404, "Customer not found")


@app.post("/customers")
def create_customer(customer: Customer):
    customers.append(customer)
    return {"message": "Customer created", "customer": customer}
