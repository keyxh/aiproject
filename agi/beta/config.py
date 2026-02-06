#!/usr/bin/env python3
"""
Configuration module for the AGI project.
Handles environment variables and settings for OpenAI API integration.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY is not set in environment variables. "
        "Please set it in a .env file or export it."
    )