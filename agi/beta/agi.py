#!/usr/bin/env python3
"""
AGI (Artificial General Intelligence) Agent Implementation using OpenAI API.
This module provides a simple AGI agent that can engage in conversations and perform tasks.
"""

import os
from typing import List, Dict, Any
from openai import OpenAI
from config import OPENAI_API_KEY


class AGIAgent:
    """
    A basic AGI agent that uses OpenAI's GPT model to process inputs and generate responses.
    
    Attributes:
        client (OpenAI): The OpenAI client instance.
        model (str): The model to use for completions.
        conversation_history (List[Dict]): History of the conversation for context.
    """
    
    def __init__(self, model: str = "gpt-4"):
        """
        Initialize the AGI agent.
        
        Args:
            model (str): The OpenAI model to use. Default is "gpt-4".
        """
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.model = model
        self.conversation_history = []
    
    def add_to_history(self, role: str, content: str):
        """
        Add a message to the conversation history.
        
        Args:
            role (str): The role of the speaker, e.g., "user" or "assistant".
            content (str): The content of the message.
        """
        self.conversation_history.append({"role": role, "content": content})
    
    def process_input(self, user_input: str) -> str:
        """
        Process the user input and generate a response using OpenAI API.
        
        Args:
            user_input (str): The input from the user.
        
        Returns:
            str: The generated response from the agent.
        """
        # Add user input to history
        self.add_to_history("user", user_input)
        
        try:
            # Call OpenAI API with current conversation history
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=150,
                temperature=0.7
            )
            
            # Extract the assistant's response
            assistant_response = response.choices[0].message.content
            
            # Add assistant response to history
            self.add_to_history("assistant", assistant_response)
            
            return assistant_response
        
        except Exception as e:
            # Handle errors gracefully
            return f"Error processing input: {e}"
    
    def run(self):
        """
        Run the AGI agent in an interactive loop.
        """
        print("AGI Agent Initialized. Type 'exit' to quit.")
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Exiting AGI Agent.")
                    break
                
                response = self.process_input(user_input)
                print(f"AGI: {response}")
            
            except KeyboardInterrupt:
                print("\nInterrupted. Exiting.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point for running the agent
    agent = AGIAgent()
    agent.run()