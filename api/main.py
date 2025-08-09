from fastapi import FastAPI
from .routers import lesson, attempt, progress

app = FastAPI(title="AI Teaching Assistant API")
app.include_router(lesson.router)
app.include_router(attempt.router)
app.include_router(progress.router)

@app.get("/")
async def root():
    return {"ok": True}
