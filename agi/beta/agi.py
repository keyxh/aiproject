# AGI (Artificial General Intelligence) Implementation using OpenAI API
# This is a basic framework to demonstrate how an AGI could be built using OpenAI's models

import openai
import os
from typing import List, Dict, Any

# Set your OpenAI API key here
openai.api_key = os.getenv('OPENAI_API_KEY')

class AGI:
    def __init__(self, model_name: str = 'gpt-3.5-turbo', max_tokens: int = 1000):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.conversation_history: List[Dict[str, Any]] = []

    def add_to_conversation(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.conversation_history.append({"role": role, "content": content})

    def get_response(self, prompt: str) -> str:
        """Get a response from the OpenAI model based on the provided prompt."""
        self.add_to_conversation("user", prompt)
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model_name,
                messages=self.conversation_history,
                max_tokens=self.max_tokens
            )
            
            # Extract and add the assistant's response to the conversation history
            assistant_response = response.choices[0].message.content
            self.add_to_conversation("assistant", assistant_response)
            return assistant_response
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """Reset the conversation history."""
        self.conversation_history = []

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """Get the current conversation history."""
        return self.conversation_history

if __name__ == "__main__":
    # Example usage of the AGI class
    agi = AGI()
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        
        response = agi.get_response(user_input)
        print(f"AGI: {response}")

        # Optional: Reset conversation after a certain number of interactions
        # if len(agi.get_conversation_history()) > 10:
        #     agi.reset_conversation()
