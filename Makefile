    .PHONY: migrate dev seed

    migrate:
	psql postgresql://tutor:tutor@localhost:5432/tutor -f migrations/0001_initial.sql

    dev:
	uvicorn api.main:app --reload

    seed:
	@echo "(stub) load content JSON/YAML into DB or cache"
