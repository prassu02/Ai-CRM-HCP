from pydantic import BaseModel

class InteractionCreate(BaseModel):
    doctor_name: str
    notes: str

class InteractionResponse(BaseModel):
    id: int
    doctor_name: str
    summary: str
    next_action: str