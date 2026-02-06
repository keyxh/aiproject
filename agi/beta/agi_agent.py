"""
AGI Agent Module.
This module defines the AGIAgent class that handles task processing and memory.
"""

from openai_client import OpenAIClient

class AGIAgent:
    """AGI Agent that processes inputs and generates responses using OpenAI API."""
    
    def __init__(self, model="gpt-4"):
        """
        Initialize the AGI Agent.
        
        Args:
            model (str): The OpenAI model to use (e.g., "gpt-4").
        """
        self.client = OpenAIClient(model=model)
        self.conversation_history = []  # Store conversation history for context
        
    def process_input(self, user_input):
        """
        Process user input and generate a response.
        
        Args:
            user_input (str): The input from the user.
        
        Returns:
            str: The generated response.
        """
        # Add user input to history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Prepare messages for OpenAI API
        messages = [
            {"role": "system", "content": "You are an advanced AGI (Artificial General Intelligence) capable of handling a wide range of tasks. Provide helpful, accurate, and thoughtful responses."}
        ]
        messages.extend(self.conversation_history)
        
        # Get response from OpenAI
        response = self.client.chat_completion(messages)
        
        # Add assistant response to history
        self.conversation_history.append({"role": "assistant", "content": response})
        
        # Optionally, limit history size to manage context window
        if len(self.conversation_history) > 10:  # Keep last 10 exchanges
            self.conversation_history = self.conversation_history[-10:]
        
        return response
