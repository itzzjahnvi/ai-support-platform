from fastapi import FastAPI

from app.db.database import Base, engine
from app.models.ticket import Ticket
from app.api.routes import ticket

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(ticket.router)

@app.get("/")
def home():
    return {"message": "Backend working"}