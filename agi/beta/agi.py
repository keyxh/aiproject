# AGI Implementation using OpenAI API
# This file contains the core logic for the AGI system

import openai
import os
from typing import Dict, Any, List

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

class AGI:
    def __init__(self, model_name: str = 'gpt-4'):
        self.model_name = model_name
        self.history = []

    def add_to_history(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.history.append({"role": role, "content": content})

    def get_response(self, prompt: str) -> str:
        """Get a response from the OpenAI model based on the prompt."""
        self.add_to_history("user", prompt)
        response = openai.ChatCompletion.create(
            model=self.model_name,
            messages=self.history
        )
        response_content = response.choices[0].message.content
        self.add_to_history("assistant", response_content)
        return response_content

    def reset_conversation(self):
        """Reset the conversation history."""
        self.history = []

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the current conversation history."""
        return self.history

if __name__ == "__main__":
    # Example usage of the AGI class
    agi = AGI()
    print(agi.get_response("Hello, how can I assist you?"))
    print(agi.get_response("Can you explain what AGI is?"))
    print(agi.get_response("What are the challenges in creating AGI?"))
    agi.reset_conversation()
    print(agi.get_response("Can you summarize the conversation so far?"))
