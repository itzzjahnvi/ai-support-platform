from pydantic import BaseModel

class TicketCreate(BaseModel):
    email: str
    message: str