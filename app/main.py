from fastapi import FastAPI
from pydantic import BaseModel
from app.db import get_connection, init_db

app = FastAPI()

class KeyValue(BaseModel):
    key: str
    value: str

@app.on_event("startup")
def startup():
    init_db()

@app.post("/add")
def add_key_value(data: KeyValue):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO key_values (key, value) VALUES (%s, %s) RETURNING id", (data.key, data.value))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": new_id, "key": data.key, "value": data.value}

@app.get("/all")
def get_all():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, key, value FROM key_values")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "key": r[1], "value": r[2]} for r in rows]
