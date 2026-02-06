# AGI Project

This project implements a basic Artificial General Intelligence (AGI) agent using OpenAI API. It serves as a foundational system that can engage in intelligent conversations and maintain context over multiple interactions.

## Features
- **Conversational Agent**: Uses OpenAI's GPT models to generate intelligent responses.
- **Memory System**: Maintains conversation history for context-aware interactions.
- **Modular Design**: Easy to extend with additional features like task execution or learning capabilities.
- **Error Handling**: Gracefully handles API errors and user inputs.

## Installation
1. Clone this repository or download the files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable (replace 'your-api-key' with your actual key):
   ```bash
   export OPENAI_API_KEY='your-api-key'
   ```
   On Windows, use:
   ```cmd
   set OPENAI_API_KEY=your-api-key
   ```

## Usage
Run the main script to start interacting with the AGI agent:
```bash
python main.py
```

Once running, you can:
- Type any message to have a conversation.
- Type 'reset' to clear the conversation history and start fresh.
- Type 'exit' to quit the application.

## Project Structure
- `main.py`: Entry point for the application, handles user interaction loop.
- `agi_agent.py`: Core AGI agent class, manages conversation and OpenAI API calls.
- `config.py`: Configuration settings, including API key and model selection.
- `requirements.txt`: Lists the Python dependencies (only `openai` library).

## Code Overview
- The `AGIAgent` class in `agi_agent.py` uses the OpenAI ChatCompletion API to process inputs. It maintains a conversation history to enable multi-turn dialogues.
- Configuration is centralized in `config.py` for easy management.
- The main loop in `main.py` provides a simple CLI for real-time interaction.

## Notes
- This is a simplified implementation of AGI, focusing on conversational intelligence using state-of-the-art language models.
- A true AGI would require advanced features such as task decomposition, autonomous learning, and multi-modal processing. This project can be extended to incorporate those elements.
- Ensure you have an active OpenAI API key and sufficient credits for API usage.

## Future Enhancements
- Integrate external tools (e.g., web search, databases) for task execution.
- Add a graphical user interface (GUI) or web interface.
- Implement a memory system with long-term storage for learning across sessions.
- Support for different AI models or multi-agent architectures.

## License
This project is open-source and can be modified as needed for educational or research purposes.
