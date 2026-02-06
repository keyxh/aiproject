"""
AGI Core Module

This module contains the main AGI class that interacts with OpenAI API and manages the agent's state.
"""

import openai
from typing import List, Dict, Any
import json
import os

class AGI:
    """Artificial General Intelligence agent."""
    
    def __init__(self, api_key: str, model: str = "gpt-4"):
        """
        Initialize the AGI agent.
        
        Args:
            api_key: OpenAI API key.
            model: The OpenAI model to use (default: gpt-4).
        """
        openai.api_key = api_key
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []
        # Initialize memory or other components as needed
        self.memory_file = "memory.json"
        self.load_memory()
    
    def load_memory(self):
        """Load conversation history from memory file."""
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                self.conversation_history = json.load(f)
        else:
            self.conversation_history = []
    
    def save_memory(self):
        """Save conversation history to memory file."""
        with open(self.memory_file, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def chat(self, user_message: str) -> str:
        """
        Process a user message and return a response.
        
        Args:
            user_message: The input from the user.
        
        Returns:
            The AGI's response.
        """
        # Add user message to history
        self.conversation_history.append({"role": "user", "content": user_message})
        
        # Prepare messages for OpenAI API
        messages = self.conversation_history
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                max_tokens=150,
                temperature=0.7
            )
            ai_message = response.choices[0].message['content']
            
            # Add AI response to history
            self.conversation_history.append({"role": "assistant", "content": ai_message})
            
            # Save memory
            self.save_memory()
            
            return ai_message
        except Exception as e:
            return f"Error: {str(e)}"
    
    def learn(self, data: str):
        """
        Method for the AGI to learn from new data.
        This is a placeholder for more advanced learning capabilities.
        """
        # In a real AGI, this could involve fine-tuning or updating internal models.
        # For now, just log the data.
        print(f"Learning from data: {data}")
        # Placeholder for future implementation
    
    def execute_task(self, task: str) -> str:
        """
        Execute a specific task.
        
        Args:
            task: Description of the task to execute.
        
        Returns:
            Result of the task execution.
        """
        # This could be extended to use tools or external APIs.
        # For simplicity, use the chat method to generate a response.
        return self.chat(f"Execute task: {task}")