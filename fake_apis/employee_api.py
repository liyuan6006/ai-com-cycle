from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Employee API")


class Employee(BaseModel):
    id: str
    name: str
    email: str
    role: str
    branch_id: str
    active: bool


employees = [
    Employee(id="E2001", name="Sam Patel", email="sam.patel@examplebank.test", role="Relationship Manager", branch_id="B101", active=True),
    Employee(id="E2002", name="Nina Cruz", email="nina.cruz@examplebank.test", role="Branch Banker", branch_id="B102", active=True),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "employee-api"}


@app.get("/employees")
def list_employees():
    return employees


@app.get("/employees/{employee_id}")
def get_employee(employee_id: str):
    for employee in employees:
        if employee.id == employee_id:
            return employee
    raise HTTPException(404, "Employee not found")
