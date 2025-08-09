from fastapi import APIRouter

router = APIRouter(prefix="/progress", tags=["progress"])

@router.get("/{user_id}")
async def get_progress(user_id: str) -> dict:
    return {"mastery": {}, "streaks": {"days": 1}, "goals": {"daily_minutes": 20}}
