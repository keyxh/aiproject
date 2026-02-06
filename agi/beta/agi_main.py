#!/usr/bin/env python3
"""
Main entry point for the AGI system.
This script initializes the AGI system and runs a simple interactive loop.
"""

import sys
from task_manager import TaskManager

def main():
    """
    Main function to run the AGI system.
    """
    print("Welcome to AGI System - A basic implementation using OpenAI API")
    tm = TaskManager()
    
    while True:
        try:
            user_input = input("Enter a task (or 'quit' to exit): ")
            if user_input.lower() == 'quit':
                break
            
            # Add and process the task
            tm.add_task(user_input)
            result = tm.process_tasks()[-1]  # Get the result of the latest task
            print(f"AGI Response: {result}")
            print("-" * 50)  # Separator for clarity
        except KeyboardInterrupt:
            print("\nInterrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()