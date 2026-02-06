import os
from openai import OpenAI
from dotenv import load_dotenv

class AGIAgent:
    """A simple AGI agent using OpenAI's API for simulating general intelligence."""
    
    def __init__(self, model="gpt-4", temperature=0.7):
        """
        Initialize the AGI agent with OpenAI configuration.
        
        Args:
            model (str): The OpenAI model to use (e.g., 'gpt-4', 'gpt-3.5-turbo').
            temperature (float): Controls randomness in response generation (0.0 to 1.0).
        """
        load_dotenv()  # Load environment variables from .env file
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set. Please set it in .env or export it.")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.temperature = temperature
        self.conversation_history = []  # Store conversation context as list of messages
    
    def add_to_history(self, role, content):
        """
        Add a message to the conversation history.
        
        Args:
            role (str): Role of the message sender ('user' or 'assistant').
            content (str): Content of the message.
        """
        self.conversation_history.append({"role": role, "content": content})
    
    def get_response(self, user_input):
        """
        Generate a response from the AGI agent based on user input and history.
        
        Args:
            user_input (str): The input text from the user.
        
        Returns:
            str: The response text from the agent, or an error message if API call fails.
        """
        # Add user input to conversation history
        self.add_to_history("user", user_input)
        
        try:
            # Call OpenAI Chat Completions API with current conversation history
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=self.temperature,
            )
            assistant_response = response.choices[0].message.content
            # Add assistant response to history for context in next interaction
            self.add_to_history("assistant", assistant_response)
            return assistant_response
        except Exception as e:
            # Handle errors gracefully (e.g., network issues, API limits)
            return f"Error generating response: {str(e)}"
    
    def run_interactive(self):
        """
        Run the agent in an interactive command-line loop.
        """
        print("AGI Agent started. Type your queries, or 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("AGI Agent shutting down. Goodbye!")
                break
            response = self.get_response(user_input)
            print(f"AGI: {response}")

if __name__ == "__main__":
    # Instantiate and run the AGI agent in interactive mode
    try:
        agent = AGIAgent()
        agent.run_interactive()
    except ValueError as ve:
        print(f"Configuration error: {ve}")
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")