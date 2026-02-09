import sqlite3

conn = sqlite3.connect("data/memory.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memory (
    memory_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id TEXT,
    type TEXT,
    key TEXT,
    value TEXT,
    origin_turn INTEGER,
    last_used_turn INTEGER,
    confidence REAL
)
""")
conn.commit()

def save_memory(user_id: str, memory: dict):
    cursor.execute("""
        INSERT INTO memory 
        (user_id, type, key, value, origin_turn, last_used_turn, confidence)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        memory["type"],
        memory["key"],
        memory["value"],
        memory["origin_turn"],
        memory["origin_turn"],
        memory["confidence"]
    ))
    conn.commit()