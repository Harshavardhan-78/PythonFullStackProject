# src/Logic.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Manages environment variables for the application.
    SUPABASE_URL and SUPABASE_KEY are loaded from the .env file.
    """
    SUPABASE_URL: str
    SUPABASE_KEY: str

    class Config:
        # Specifies that settings should be read from the .env file
        env_file = ".env"

def get_settings():
    """Initializes and returns the Settings object."""
    return Settings()