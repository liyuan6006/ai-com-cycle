from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Notes API")


class Note(BaseModel):
    id: str | None = None
    customer_id: str
    title: str
    body: str
    author: str
    created_at: datetime | None = None


notes = [
    Note(
        id="NOTE1001",
        customer_id="C1001",
        title="Welcome call",
        body="Customer prefers email updates for service requests.",
        author="Sam Patel",
        created_at=datetime.now(),
    ),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "notes-api"}


@app.get("/notes")
def list_notes():
    return notes


@app.get("/notes/customer/{customer_id}")
def get_customer_notes(customer_id: str):
    return [note for note in notes if note.customer_id == customer_id]


@app.get("/notes/{note_id}")
def get_note(note_id: str):
    for note in notes:
        if note.id == note_id:
            return note
    raise HTTPException(404, "Note not found")


@app.post("/notes")
def create_note(note: Note):
    note.id = note.id or f"NOTE{1000 + len(notes) + 1}"
    note.created_at = datetime.now()
    notes.append(note)
    return {"message": "Note created", "note": note}

