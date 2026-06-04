from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app.models.ticket import Ticket
from app.schemas.ticket import TicketCreate
from app.workers.worker import process_ticket

router = APIRouter(prefix="/tickets", tags=["Tickets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_ticket(data: TicketCreate, db: Session = Depends(get_db)):
    ticket = Ticket(
        email=data.email,
        message=data.message
    )

    db.add(ticket)
    db.commit()
    db.refresh(ticket)

    # Trigger async AI processing
    process_ticket.delay(ticket.id)

    return {
        "message": "Ticket created",
        "ticket_id": ticket.id
    }

@router.get("/")
def get_tickets(db: Session = Depends(get_db)):
    return db.query(Ticket).all()