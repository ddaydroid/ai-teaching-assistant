from fastapi import APIRouter
from ..schemas import AttemptIn, AttemptOut

router = APIRouter(prefix="/attempt", tags=["attempt"])

@router.post("")
async def submit_attempt(payload: AttemptIn) -> AttemptOut:
    # TODO: Route to grading runners
    return AttemptOut(status="pass", feedback={"msg": "stub grader"})
