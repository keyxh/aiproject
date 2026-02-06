"""
Configuration management for AGI project.
Loads environment variables from .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in .env file.")

# Model configuration
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")  # Default to GPT-4 if not specified