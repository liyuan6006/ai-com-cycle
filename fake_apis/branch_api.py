from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Branch API")


class Branch(BaseModel):
    id: str
    name: str
    city: str
    state: str
    phone: str


branches = [
    Branch(id="B101", name="Downtown Banking Center", city="Phoenix", state="AZ", phone="555-1101"),
    Branch(id="B102", name="North Valley Banking Center", city="Scottsdale", state="AZ", phone="555-1102"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "branch-api"}


@app.get("/branches")
def list_branches():
    return branches


@app.get("/branches/{branch_id}")
def get_branch(branch_id: str):
    for branch in branches:
        if branch.id == branch_id:
            return branch
    raise HTTPException(404, "Branch not found")

