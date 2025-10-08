from pydantic import BaseModel, EmailStr
from typing import Optional

class TextModerationRequest(BaseModel):
    email: EmailStr
    content: str

class ModerationResponse(BaseModel):
    classification: str
    confidence: float
    reasoning: str
