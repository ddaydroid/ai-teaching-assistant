# AI Teaching Assistant (MVP: Markdown + Python)

Chat-first learning with adaptive lessons and auto-graded exercises.

## Dev Quickstart
```bash
# 1) Bring up services (DB + runners)
docker compose up -d

# 2) Apply DB migration
make migrate

# 3) Run API locally
uvicorn api.main:app --reload
```

## Project Layout
- `api/` FastAPI service (orchestrator + endpoints)
- `content/` Curriculum blocks + exercises (Markdown/Python)
- `runners/` Grading sandboxes (Dockerized)
- `migrations/` SQL migrations
