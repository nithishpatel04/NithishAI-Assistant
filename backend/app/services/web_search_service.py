import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    vertexai=True,
    project=os.getenv("GCP_PROJECT_ID"),
    location=os.getenv("GCP_LOCATION", "global"),
)


def search_web(question: str) -> str:
    """
    Search the live web using Google Search grounding.

    Use this for information that may be current or changing,
    including recent news, movies, sports, companies, software
    versions, releases, events and other up-to-date information.
    """

    print(f"WEB SEARCH CALLED: {question}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    google_search=types.GoogleSearch()
                )
            ]
        ),
    )

    return response.text