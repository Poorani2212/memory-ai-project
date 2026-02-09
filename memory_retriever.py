from memory_store import cursor, conn

def retrieve_memory(user_id: str, current_turn: int):
    cursor.execute("""
        SELECT memory_id, value, origin_turn, last_used_turn
        FROM memory
        WHERE user_id=?
        ORDER BY confidence DESC
        LIMIT 2
    """, (user_id,))

    memories = cursor.fetchall()

    for mem in memories:
        cursor.execute(
            "UPDATE memory SET last_used_turn=? WHERE memory_id=?",
            (current_turn, mem[0])
        )

    conn.commit()
    return memories