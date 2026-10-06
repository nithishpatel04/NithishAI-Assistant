import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    gcp_project_id: str = os.getenv("GCP_PROJECT_ID", "")
    gcp_location: str = os.getenv("GCP_LOCATION", "")


settings = Settings()
