from fastapi import FastAPI
from pydantic import BaseModel, Field

from graph.workflow import run_complaint_workflow


app = FastAPI(title="Fake Bank FastAPI Gateway")


class ComplaintRequest(BaseModel):
    customer_id: str = Field(..., examples=["C1001"])
    message: str = Field(..., examples=["My card was charged twice at Metro Grocery."])
    channel: str = Field("Web", examples=["Web", "Mobile", "Phone"])


@app.get("/health")
def health():
    return {"status": "ok", "service": "fastapi-gateway"}


@app.post("/complaint-workflow")
def complaint_workflow(request: ComplaintRequest):
    return run_complaint_workflow(request.model_dump())
