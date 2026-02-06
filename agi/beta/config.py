import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Config:
    """
    Configuration class for AGI project.
    Manages API keys and other settings.
    """
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")  # Replace with your API key or set in .env file
    MODEL = "gpt-4"  # Default model to use; can be changed to gpt-3.5-turbo or others
