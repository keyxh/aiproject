"""
Core AGI module that interacts with OpenAI API.
Implements a simple memory system for context.
"""

import openai
from config import OPENAI_API_KEY, MODEL_NAME

class AGI:
    """
    Artificial General Intelligence class.
    Uses OpenAI's API to simulate intelligent behavior.
    """
    
    def __init__(self):
        """Initialize the AGI with OpenAI client and memory."""
        self.client = openai.OpenAI(api_key=OPENAI_API_KEY)
        self.model = MODEL_NAME
        self.memory = []  # Simple list to store conversation history
        
    def think(self, prompt):
        """
        Process the user prompt and generate a response.
        
        Args:
            prompt (str): The user's input.
            
        Returns:
            str: The AGI's response.
        """
        # Add prompt to memory
        self.memory.append({"role": "user", "content": prompt})
        
        # Prepare messages for API call
        messages = self.memory
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=150  # Limit response length
            )
            ai_response = response.choices[0].message.content
            
            # Add AI response to memory
            self.memory.append({"role": "assistant", "content": ai_response})
            
            return ai_response
        except Exception as e:
            return f"Error: {str(e)}"
    
    def reset_memory(self):
        """Reset the conversation memory."""
        self.memory = []