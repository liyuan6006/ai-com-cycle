from datetime import datetime
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Email API")


class EmailMessage(BaseModel):
    id: str | None = None
    to_address: str
    subject: str
    body: str
    status: str = "Queued"
    sent_at: datetime | None = None


emails = [
    EmailMessage(
        id="EM1001",
        to_address="avery.morgan@example.com",
        subject="Statement ready",
        body="Your latest statement is ready.",
        status="Sent",
        sent_at=datetime.now(),
    ),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "email-api"}


@app.get("/emails")
def list_emails():
    return emails


@app.get("/emails/{email_id}")
def get_email(email_id: str):
    for email in emails:
        if email.id == email_id:
            return email
    raise HTTPException(404, "Email not found")


@app.post("/emails")
def send_email(email: EmailMessage):
    email.id = email.id or f"EM{1000 + len(emails) + 1}"
    email.status = "Sent"
    email.sent_at = datetime.now()
    emails.append(email)
    return {"message": "Email sent", "email": email}
