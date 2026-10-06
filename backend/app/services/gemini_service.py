import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from app.services.web_search_service import search_web

from app.tools.basic_tools import (
    get_current_date,
    get_current_time,
    calculate,
)

from app.tools.weather_tools import get_weather

from app.tools.api_tools import get_country_information

from app.memory.firestore_memory import (
    get_recent_messages,
    get_long_term_memories,
    save_message,
)

from app.services.memory_service import analyze_and_save_memory

load_dotenv()

project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION", "global")

client = genai.Client(
    vertexai=True,
    project=project_id,
    location=location,
)


def generate_response(user_id: str, message: str) -> str:

    # 1. Get recent conversation history
    history = get_recent_messages(user_id, limit=10)

    # 2. Get long-term memories
    memories = get_long_term_memories(user_id, limit=20)

    conversation = []

    for item in history:
        conversation.append(
            f"{item['role']}: {item['content']}"
        )

    conversation.append(f"user: {message}")

    # Convert memories into text
    memory_context = "\n".join(
        f"- {memory}" for memory in memories
    )

    # 3. Build Gemini prompt
    prompt = f"""
You are Nithish AI, a general-purpose agentic AI assistant.

Your goal is to help the user accurately and naturally.

IMPORTANT BEHAVIOR:

1. Answer general knowledge questions directly when you already have
   sufficient reliable knowledge.

2. Use the search_web tool whenever the question depends on current,
   recent, changing, or web-specific information.

Examples include:
- latest news
- recent movies
- current events
- sports results
- current companies or executives
- software releases and versions
- current jobs
- recent AI developments
- anything where your internal knowledge may be outdated

3. Use specialized tools when appropriate:
- get_weather for current weather
- calculate for calculations
- get_current_date for today's date
- get_current_time for current time
- get_country_information for country information

4. Use the provided user memories only when relevant.

5. LANGUAGE: English is the default language. Respond in English
   unless the user explicitly asks you to use another language.
   Once they explicitly request a language, keep using it for the
   rest of this conversation. Do not switch languages just because
   the user writes in another language or script, and do not carry
   a language preference over from earlier, unrelated conversations
   in the history; a new conversation starts in English.

6. If the user explicitly requests a language but writes it using
   Latin/Roman characters, understand the intended language and
   respond naturally in that language.

7. Never claim that you searched the web or called an API unless a
   tool actually provided that information.

Long-term memories:
{memory_context}

Recent conversation:
{chr(10).join(conversation)}

Respond to the user's latest message.
"""

    # 4. Generate response
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(
        tools=[
            get_current_date,
            get_current_time,
            calculate,
            get_weather,
            get_country_information,
            search_web,
        ],
    ),
)

    answer = response.text

    # 5. Save conversation history
    save_message(user_id, "user", message)
    save_message(user_id, "assistant", answer)

    # 6. Check whether new long-term memory should be created
    analyze_and_save_memory(
        user_id=user_id,
        message=message,
    )

    return answer