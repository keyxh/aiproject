import openai
from config import OPENAI_API_KEY, MODEL

class AGIAgent:
    """
    AGI Agent class that uses OpenAI API to process inputs and maintain conversation history.
    This serves as a foundational implementation for an Artificial General Intelligence system.
    """
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.model = MODEL
        self.conversation_history = []  # Maintains context for multi-turn conversations

    def process_input(self, user_input):
        """
        Process user input by sending it to the OpenAI API and returning the response.
        Maintains conversation history for context-aware interactions.
        
        Args:
            user_input (str): The input text from the user.
        
        Returns:
            str: The assistant's response or an error message.
        """
        # Add user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})
        
        # Prepare messages for the API call using the entire history
        messages = self.conversation_history
        
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages
            )
            assistant_response = response.choices[0].message['content']
            
            # Add assistant response to history for future context
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response
        except Exception as e:
            # Handle errors gracefully
            return f"Error processing input: {str(e)}"

    def reset_conversation(self):
        """
        Reset the conversation history to start a new session.
        """
        self.conversation_history = []
