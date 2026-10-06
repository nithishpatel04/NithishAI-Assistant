import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

project_id = os.getenv("GCP_PROJECT_ID")
location = os.getenv("GCP_LOCATION", "global")

client = genai.Client(
    vertexai=True,
    project=project_id,
    location=location,
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say: Hello Nithish! Your first Gemini connection is working.",
)

print(response.text)