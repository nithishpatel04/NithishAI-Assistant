import json
import os

from dotenv import load_dotenv
from google import genai

from app.memory.firestore_memory import save_long_term_memory


load_dotenv()

client = genai.Client(
    vertexai=True,
    project=os.getenv("GCP_PROJECT_ID"),
    location=os.getenv("GCP_LOCATION", "global"),
)


def analyze_and_save_memory(user_id: str, message: str):
    """
    Analyze a user message and save useful long-term information.
    """

    prompt = f"""
Analyze the following user message.

Decide whether it contains useful information that would be helpful
to remember in future conversations.

Good memories include:
- preferences
- ongoing projects
- goals
- skills
- recurring requirements
- stable personal information relevant to future assistance

Do not remember:
- ordinary questions
- temporary statements
- greetings
- random conversation

User message:
{message}

Return ONLY valid JSON using this format:

{{
    "should_remember": true,
    "memory": "concise fact to remember"
}}

If nothing should be remembered:

{{
    "should_remember": false,
    "memory": null
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    text = response.text.strip()

    # Handle Markdown code fences if the model returns them.
    text = text.replace("```json", "").replace("```", "").strip()

    result = json.loads(text)

    if result.get("should_remember") and result.get("memory"):
        save_long_term_memory(
            user_id=user_id,
            content=result["memory"],
        )

    return result