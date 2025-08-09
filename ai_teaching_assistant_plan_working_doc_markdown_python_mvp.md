# Project Progress – AI Teaching Assistant (Markdown + Python MVP)

## Current Progress ✅
- **Repo Scaffold Completed:** Full folder structure, placeholders, and base configs for API, content, runners, migrations, and CI.
- **Seed Content Added:** Initial Markdown (3 exercises) and Python (5 exercises) with YAML/JSON definitions.
- **Dockerized Runners:** Stub implementations for `runner-python` and `runner-markdown` built into `docker-compose.yml`.
- **API Endpoints:** `/lesson/next`, `/progress/{user_id}`, `/attempt` (currently stubbed but scaffolded for runner integration).
- **Git Init Script:** Provided for quick initialization and first commit.
- **CI/CD:** GitHub Actions workflows for basic lint/build checks on API and runners.

---

## Work In Progress 🔄
- **Runner Integration:** Wiring `/attempt` endpoint to invoke Dockerized runners with volume mounting for submissions.
- **Grading Logic:** Implementing real grading for Markdown (lint + rules) and Python (pytest + AST checks).
- **Progress Tracking:** Expanding `/progress` to query mastery and streak data from DB.
- **Content Expansion:** Adding more exercises for Markdown advanced features and Python Core I completion.

---

## Next Steps ▶️
1. **Wire `/attempt` to Runners:** Enable mounting temp files and parsing output.
2. **Implement Real Graders:** Replace stub logic with actual lint/test execution.
3. **Volume Mounting:** Ensure Docker runners can access submitted code/markdown.
4. **DB Migrations:** Add full schema from Minimal DB Schema section.
5. **Local/CI Test Payloads:** Add sample `/attempt` tests in CI to validate runner integration.
6. **Frontend Integration:** Connect chat UI with endpoints for interactive lessons.

---

## Future Plans 🚀
- **Adaptive Learning Engine:** Implement mastery tracking with Bayesian Knowledge Tracing.
- **Additional Tracks:** Add JavaScript after MVP stability.
- **Projects & Capstones:** Multi-step, real-world challenges that combine multiple concepts.
- **Peer Review Mode:** Optional mentor-mentee style code reviews.
- **Export/Import Progress:** JSON-based profile migration between devices.
- **Gamification:** Streaks, badges, and goal-setting with dynamic nudges.
- **Offline Mode:** Allow lesson and exercise completion without internet, sync on reconnect.
