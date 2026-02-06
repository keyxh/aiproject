"""
Configuration Module.
This module handles configuration settings for the AGI project.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Other configurations can be added here
# Example: MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
