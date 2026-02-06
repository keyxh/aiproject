"""
OpenAI Client Module.
This module provides a client for interacting with the OpenAI API.
"""

import openai
from config import OPENAI_API_KEY

class OpenAIClient:
    """Client to handle OpenAI API calls."""
    
    def __init__(self, model="gpt-4"):
        """
        Initialize the OpenAI client.
        
        Args:
            model (str): The model to use (e.g., "gpt-4").
        """
        self.model = model
        openai.api_key = OPENAI_API_KEY
        if not openai.api_key:
            raise ValueError("OpenAI API key not set. Please configure it in config.py or environment variables.")
    
    def chat_completion(self, messages):
        """
        Send a chat completion request to OpenAI API.
        
        Args:
            messages (list): List of message dictionaries with 'role' and 'content'.
        
        Returns:
            str: The content of the assistant's response.
        
        Raises:
            Exception: If the API call fails.
        """
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            return response.choices[0].message['content']
        except Exception as e:
            raise Exception(f"OpenAI API error: {e}")
