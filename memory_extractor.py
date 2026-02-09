def extract_memory(message: str, turn: int):
    msg = message.lower()

    if "prefer" in msg or "preferred" in msg or "only after" in msg:
        return {
            "type": "preference",
            "key": "general",
            "value": message,
            "origin_turn": turn,
            "confidence": 0.9
        }

    if "call me" in msg or "remind me" in msg:
        return {
            "type": "commitment",
            "key": "follow_up",
            "value": message,
            "origin_turn": turn,
            "confidence": 0.85
        }

    return None