import os

# OpenAI API configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

# Model configuration
MODEL = "gpt-4"  # Can be changed to other models like "gpt-3.5-turbo"
