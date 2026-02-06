import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AGIAgent:
    """
    A simple AGI agent that uses OpenAI API to simulate intelligent behavior.
    This agent maintains conversation history and processes user inputs.
    """

    def __init__(self, model="gpt-4"):
        """
        Initialize the AGI agent with OpenAI API.

        Args:
            model (str): The OpenAI model to use (default is 'gpt-4').

        Raises:
            ValueError: If OPENAI_API_KEY is not set in environment variables.
        """
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY not found. Please set it in the .env file."
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.conversation_history = []  # Store conversation context for continuity

    def process_input(self, user_input):
        """
        Process user input by sending it to OpenAI API and generating a response.

        Args:
            user_input (str): The input text from the user.

        Returns:
            str: The generated response from the AGI agent, or an error message.
        """
        # Append user input to conversation history
        self.conversation_history.append({"role": "user", "content": user_input})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation_history,
                max_tokens=500,  # Limit response length
                temperature=0.7,  # Control randomness (higher for more creative)
            )

            assistant_response = response.choices[0].message.content
            # Append assistant response to conversation history
            self.conversation_history.append(
                {"role": "assistant", "content": assistant_response}
            )

            return assistant_response
        except Exception as e:
            # Log error and return user-friendly message
            return f"AGI encountered an error: {str(e)}"

    def run(self):
        """
        Run the AGI agent in an interactive loop for real-time conversation.
        """
        print("AGI Agent started. Type your messages below. Type 'exit' to quit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting AGI Agent. Goodbye!")
                break

            response = self.process_input(user_input)
            print(f"AGI: {response}")


if __name__ == "__main__":
    # Create and run the AGI agent
    try:
        agent = AGIAgent()
        agent.run()
    except ValueError as e:
        print(f"Initialization error: {e}")
    except KeyboardInterrupt:
        print("\nAGI Agent interrupted by user.")
