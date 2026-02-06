#!/usr/bin/env python3
"""
AGI System Main Entry Point.
This module initializes the AGI agent and starts the interaction loop.
"""

import sys
from agi_agent import AGIAgent

def main():
    """Main function to run the AGI agent."""
    print("Initializing AGI Agent...")
    agent = AGIAgent()
    
    print("AGI Agent started. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Exiting AGI Agent.")
                break
            
            response = agent.process_input(user_input)
            print(f"AGI: {response}")
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting.")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
