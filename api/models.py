from typing import Any
from psycopg.rows import dict_row
from .deps import get_conn

async def fetch_next_activity(user_id: str) -> dict[str, Any] | None:
    async with get_conn() as conn:
        async with conn.cursor(row_factory=dict_row) as cur:
            await cur.execute("SELECT id, concept_ids, difficulty, lang, content_json FROM activities LIMIT 1")
            row = await cur.fetchone()
            return row
