from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="Fake Bank Notification API")


class Notification(BaseModel):
    id: str
    customer_id: str
    destination: str
    channel: str
    subject: str
    status: str
    sent_at: datetime | None = None


notifications = [
    Notification(id="N8001", customer_id="C1001", destination="avery.morgan@example.com", channel="Email", subject="Statement ready", status="Sent", sent_at=datetime.now()),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "notification-api"}


@app.get("/notifications")
def list_notifications():
    return notifications


@app.post("/notifications")
def send_notification(notification: Notification):
    notification.status = "Sent"
    notification.sent_at = datetime.now()
    notifications.append(notification)
    return {"message": "Notification sent", "notification": notification}
