from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Document API")


class Document(BaseModel):
    id: str
    customer_id: str
    document_type: str
    file_name: str
    status: str


documents = [
    Document(id="D6001", customer_id="C1001", document_type="Statement", file_name="statement-june.pdf", status="Available"),
    Document(id="D6002", customer_id="C1002", document_type="Dispute Form", file_name="card-dispute.pdf", status="Pending Review"),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "document-api"}


@app.get("/documents")
def list_documents():
    return documents


@app.get("/documents/customer/{customer_id}")
def get_customer_documents(customer_id: str):
    return [document for document in documents if document.customer_id == customer_id]


@app.get("/documents/{document_id}")
def get_document(document_id: str):
    for document in documents:
        if document.id == document_id:
            return document
    raise HTTPException(404, "Document not found")

