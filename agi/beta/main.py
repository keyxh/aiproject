#!/usr/bin/env python3
"""
AGI Agent using OpenAI API
This script implements a basic Artificial General Intelligence (AGI) agent
that interacts with users through a command-line interface.
It uses OpenAI's GPT model to generate responses, simulating AGI-like behavior.
"""

import os
import sys
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("Error: OPENAI_API_KEY not found in environment variables.\n"
          "Please create a .env file with OPENAI_API_KEY=your_key_here")
    sys.exit(1)


def agi_agent(prompt: str, model: str = "gpt-4", max_tokens: int = 200) -> str:
    """
    Interact with OpenAI API to generate an AGI-like response.
    
    Args:
        prompt (str): User's input prompt.
        model (str): OpenAI model to use (default: "gpt-4").
        max_tokens (int): Maximum tokens in response (default: 200).
    
    Returns:
        str: Generated response from the model, or error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AGI (Artificial General Intelligence) agent. "
                        "You can handle diverse tasks, answer questions, solve problems, "
                        "and engage in meaningful conversations. Be adaptive, helpful, "
                        "and accurate in your responses."
                    )
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,  # Balance creativity and consistency
            top_p=0.9
        )
        return response.choices[0].message['content'].strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI API error: {e}"
    except Exception as e:
        return f"Unexpected error: {e}"


def main() -> None:
    """
    Main function to run the AGI agent in an interactive loop.
    """
    print("=== AGI Agent (Powered by OpenAI API) ===")
    print("Type your query, or 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("AGI: Goodbye! Have a great day.")
                break
            
            response = agi_agent(user_input)
            print(f"AGI: {response}")
        except KeyboardInterrupt:
            print("\nAGI: Session interrupted. Exiting.")
            break
        except Exception as e:
            print(f"AGI: Critical error - {e}")
            break


if __name__ == "__main__":
    main()
