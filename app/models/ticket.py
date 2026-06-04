from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    message = Column(Text)
    status = Column(String, default="open")
    ai_reply = Column(Text, nullable=True)