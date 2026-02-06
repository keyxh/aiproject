# AGI (Artificial General Intelligence) Implementation using OpenAI API
# This file contains the core logic for interacting with the OpenAI API to simulate an AGI system.

import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Define a function to generate responses using the OpenAI API
def generate_response(prompt):
    """Generate a response based on the given prompt using OpenAI's GPT model.

    Args:
        prompt (str): The input prompt for the AI model.

    Returns:
        str: The generated response from the AI model.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Using GPT-3.5 model
            prompt=prompt,
            max_tokens=150,  # Maximum number of tokens in the response
            n=1,  # Number of responses to generate
            stop=None,  # Stop generating when the model reaches this token
            temperature=0.7  # Controls the randomness of the output
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage of the AGI system
def main():
    print("Welcome to the AGI System!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        response = generate_response(user_input)
        print(f"AGI: {response}")

if __name__ == "__main__":
    main()
