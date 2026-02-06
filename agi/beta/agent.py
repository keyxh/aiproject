import openai
from config import Config

class AIAgent:
    """
    AI Agent class that uses OpenAI API to simulate AGI.
    This class handles conversations, memory, and interactions with the OpenAI model.
    """
    def __init__(self, api_key=None, model=None):
        """
        Initialize the AI Agent.
        Args:
            api_key (str): OpenAI API key. If None, uses Config.OPENAI_API_KEY.
            model (str): Model to use. If None, uses Config.MODEL.
        """
        if api_key is None:
            api_key = Config.OPENAI_API_KEY
        if model is None:
            model = Config.MODEL
        
        self.api_key = api_key
        self.model = model
        openai.api_key = self.api_key  # Set the API key for OpenAI
        self.memory = []  # Store conversation history as a list of message dictionaries
        
    def chat(self, message):
        """
        Send a message to OpenAI and get a response.
        Args:
            message (str): User's message.
        Returns:
            str: AI's response.
        """
        self.memory.append({"role": "user", "content": message})
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.memory
            )
        except Exception as e:
            return f"Error: {e}"  # Handle API errors gracefully
        
        reply = response.choices[0].message.content
        self.memory.append({"role": "assistant", "content": reply})
        
        return reply
    
    def remember(self, memory_text):
        """
        Add a specific memory to the agent (e.g., system instructions).
        Args:
            memory_text (str): Text to remember.
        """
        self.memory.append({"role": "system", "content": memory_text})
        
    def clear_memory(self):
        """Clear all memories to reset the conversation."""
        self.memory = []
