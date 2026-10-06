from datetime import datetime, timezone

from google.cloud import firestore


db = firestore.Client()


def save_message(user_id: str, role: str, content: str):
    """
    Save one conversation message to Firestore.
    """

    message = {
        "role": role,
        "content": content,
        "created_at": datetime.now(timezone.utc),
    }

    (
        db.collection("users")
        .document(user_id)
        .collection("messages")
        .add(message)
    )


def get_recent_messages(user_id: str, limit: int = 10):
    """
    Retrieve the user's most recent conversation messages.
    """

    docs = (
        db.collection("users")
        .document(user_id)
        .collection("messages")
        .order_by("created_at", direction=firestore.Query.DESCENDING)
        .limit(limit)
        .stream()
    )

    messages = []

    for doc in docs:
        data = doc.to_dict()

        messages.append({
            "role": data["role"],
            "content": data["content"],
        })

    # Firestore returned newest → oldest.
    # Gemini should receive conversation chronologically.
    messages.reverse()

    return messages

def save_long_term_memory(user_id: str, content: str):
    """
    Save an important user fact as long-term memory.
    """

    memory = {
        "content": content,
        "created_at": datetime.now(timezone.utc),
    }

    (
        db.collection("users")
        .document(user_id)
        .collection("memories")
        .add(memory)
    )


def get_long_term_memories(user_id: str, limit: int = 20):
    """
    Retrieve long-term memories for a user.
    """

    docs = (
        db.collection("users")
        .document(user_id)
        .collection("memories")
        .order_by(
            "created_at",
            direction=firestore.Query.DESCENDING,
        )
        .limit(limit)
        .stream()
    )

    memories = []

    for doc in docs:
        data = doc.to_dict()
        memories.append(data["content"])

    return memories