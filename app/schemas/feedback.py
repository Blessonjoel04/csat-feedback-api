from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class FeedbackCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    rating: int = Field(..., ge=1, le=5)
    description: Optional[str] = None
