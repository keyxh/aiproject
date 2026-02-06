# AGI Implementation using OpenAI API
# This file contains the core logic for the AGI system

import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a class for the AGI system
class AGI:
    def __init__(self):
        self.model = 'gpt-3.5-turbo'  # Using GPT-3.5 Turbo as the base model

    def generate_response(self, prompt):
        """Generate a response to the given prompt using the OpenAI API."""
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=[{'role': 'user', 'content': prompt}]
            )
            return response['choices'][0]['message']['content']
        except Exception as e:
            return f"Error: {str(e)}"

    def run(self):
        """Main loop for the AGI system."""
        print("AGI System Started. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                break
            response = self.generate_response(user_input)
            print(f"AGI: {response}")

if __name__ == "__main__":
    agi = AGI()
    agi.run()
