#!/usr/bin/env python3
"""
Configuration module for managing environment variables and settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please set it in a .env file.")

# Optional: Add other configuration settings here
# For example:
# MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4")
# MAX_TOKENS = int(os.getenv("MAX_TOKENS", 1000))