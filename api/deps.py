import os
import psycopg
from contextlib import asynccontextmanager

DSN = os.getenv("DATABASE_URL", "postgresql://tutor:tutor@localhost:5432/tutor")

@asynccontextmanager
async def get_conn():
    async with await psycopg.AsyncConnection.connect(DSN) as conn:
        yield conn
