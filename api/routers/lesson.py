from fastapi import APIRouter
from ..models import fetch_next_activity

router = APIRouter(prefix="/lesson", tags=["lesson"])

@router.post("/next")
async def next_lesson(user_id: str) -> dict:
    row = await fetch_next_activity(user_id)
    if not row:
        return {"message": "No activities yet"}
    return {
        "activity": {
            "id": row["id"],
            "concepts": row["concept_ids"],
            "difficulty": row["difficulty"],
            "lang": row["lang"],
            "content": row["content_json"],
        }
    }
