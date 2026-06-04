from celery import Celery

from app.db.database import SessionLocal
from app.models.ticket import Ticket
from app.services.llm_service import generate_reply

celery = Celery(
    "worker",
    broker="redis://localhost:6379/0"
)

@celery.task
def process_ticket(ticket_id):

    db = SessionLocal()

    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()

    if not ticket:
        return

    ai_response = generate_reply(ticket.message)

    ticket.ai_reply = ai_response
    ticket.status = "ai_generated"

    db.commit()

    db.close()