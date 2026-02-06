# AGI (Artificial General Intelligence) Implementation using OpenAI API
# This file contains the core logic for interacting with the OpenAI API to build an AGI system

import openai
import os
from typing import Dict, Any, List

# Set up OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

class AGI:
    def __init__(self, model_name: str = 'gpt-4', max_tokens: int = 2048):
        """Initialize the AGI system with a specific model and parameters.""
        self.model_name = model_name
        self.max_tokens = max_tokens

    def generate_response(self, prompt: str, temperature: float = 0.7, top_p: float = 1.0) -> str:
        """Generate a response from the model given a prompt.""
        try:
            response = openai.Completion.create(
                engine=self.model_name,
                prompt=prompt,
                max_tokens=self.max_tokens,
                temperature=temperature,
                top_p=top_p
            )
            return response.choices[0].text.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def chat_with_ai(self, messages: List[Dict[str, str]], temperature: float = 0.7, top_p: float = 1.0) -> str:
        """Chat with the AI using a list of message history.""
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=messages,
                temperature=temperature,
                top_p=top_p
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error: {str(e)}"

    def set_model(self, model_name: str):
        """Change the model used by the AGI system.""
        self.model_name = model_name

    def set_max_tokens(self, max_tokens: int):
        """Set the maximum number of tokens for responses.""
        self.max_tokens = max_tokens

if __name__ == '__main__':
    # Example usage of the AGI class
    agi = AGI(model_name='gpt-3.5-turbo')
    response = agi.generate_response("What is the capital of France?")
    print(f"AGI Response: {response}")

    # Chat example
    messages = [
        {"role": "system", "content": "You are an AI assistant."},
        {"role": "user", "content": "Who won the 2022 FIFA World Cup?"}
    ]
    chat_response = agi.chat_with_ai(messages)
    print(f"Chat Response: {chat_response}")