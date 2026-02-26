from pydantic import BaseModel

class MotivationRequest(BaseModel):
    text: str | None = None # Optional user input

class MotivationResponse(BaseModel):
    response: str # AI-generated motivational message
