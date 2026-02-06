#!/usr/bin/env python3
"""
AGI Main Entry Point

This script initializes the AGI system and starts an interactive session.
"""

from agi_core import AGI
import config

def main():
    """Main function to run the AGI."""
    # Initialize AGI
    agi = AGI(api_key=config.OPENAI_API_KEY)
    
    print("Welcome to the AGI System!")
    print("Type 'exit' to quit.")
    
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == 'exit':
            break
        
        response = agi.chat(user_input)
        print(f"AGI: {response}")

if __name__ == "__main__":
    main()