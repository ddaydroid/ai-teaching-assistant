from pydantic import BaseModel
from typing import Any, List

class Activity(BaseModel):
    id: str
    concepts: List[str]
    difficulty: float
    lang: str
    content: dict[str, Any]

class AttemptIn(BaseModel):
    user_id: str
    activity_id: str
    lang: str
    submission: str | dict

class AttemptOut(BaseModel):
    status: str
    feedback: dict[str, Any] | None = None
