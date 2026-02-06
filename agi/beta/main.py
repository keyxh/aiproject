#!/usr/bin/env python3
"""
Main entry point for the AGI project.
Provides a command-line interface to interact with the AGI.
"""

from agi import AGI

def main():
    """
    Main function to run the AGI system.
    """
    print("Welcome to AGI System using OpenAI API!")
    print("Type 'exit' to quit, 'reset' to clear memory.")
    
    # Initialize AGI
    agi = AGI()
    
    while True:
        user_input = input("\nYou: ")
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'reset':
            agi.reset_memory()
            print("Memory reset.")
            continue
        
        response = agi.think(user_input)
        print(f"AGI: {response}")

if __name__ == "__main__":
    main()