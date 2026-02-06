from agi_agent import AGIAgent

def main():
    """
    Main function to run the AGI agent in an interactive loop.
    Provides a simple command-line interface for user interaction.
    """
    agent = AGIAgent()
    print("Welcome to the AGI Agent. This is a basic implementation using OpenAI API.")
    print("Type 'exit' to quit or 'reset' to clear conversation history.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'reset':
            agent.reset_conversation()
            print("Conversation history reset.")
            continue
        
        response = agent.process_input(user_input)
        print(f"AGI: {response}")

if __name__ == "__main__":
    main()
