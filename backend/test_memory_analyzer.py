from app.services.memory_service import analyze_and_save_memory


USER_ID = "user_001"

result = analyze_and_save_memory(
    USER_ID,
    "What is Docker?",
)

print(result)