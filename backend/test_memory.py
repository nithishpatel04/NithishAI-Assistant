from app.memory.firestore_memory import (
    save_long_term_memory,
    get_long_term_memories,
)


USER_ID = "user_001"

save_long_term_memory(
    USER_ID,
    "User prefers Python for AI development.",
)

print("Long-term memory saved!")

memories = get_long_term_memories(USER_ID)

print("\nLong-term memories:")

for memory in memories:
    print("-", memory)