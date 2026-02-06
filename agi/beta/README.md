# AGI Project

A simple implementation of an Artificial General Intelligence (AGI) agent using OpenAI API.

## Description

This project aims to create a basic AGI agent that can engage in conversations and perform tasks by leveraging OpenAI's powerful language models. The agent maintains conversation history to provide context-aware responses, simulating aspects of general intelligence.

## Features

- Interactive chat interface for natural language interaction.
- Context memory using conversation history to enhance coherence.
- Configurable OpenAI model (e.g., GPT-4) via code parameters.
- Robust error handling and modular design for extensibility.

## Installation

1. Clone the repository (if applicable) or set up the project directory:
   ```bash
   git clone <repository-url>
   cd agi
   ```
   If starting fresh, create a directory and place the provided files in it.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the project root and add:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Alternatively, export it as an environment variable in your shell.
   - Obtain an API key from [OpenAI](https://platform.openai.com/).

## Usage

Run the AGI agent from the command line:

```bash
python agi.py
```

Then, type your messages, and the agent will respond interactively. Type 'exit' to quit the session.

## Configuration

- Modify `config.py` to adjust environment variable loading or add other settings.
- In `agi.py`, you can change the default model by passing a different model name (e.g., "gpt-3.5-turbo") to the `AGIAgent` constructor.
- Adjust parameters like `max_tokens` and `temperature` in the `process_input` method for custom behavior.

## Dependencies

- `openai`: Python client library for interacting with OpenAI API.
- `python-dotenv`: For managing environment variables from a `.env` file.

Ensure you have Python 3.7 or higher installed.

## Project Structure

- `agi.py`: Main agent implementation with interactive loop.
- `config.py`: Configuration handling for API keys.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This documentation file.

## Best Practices Followed

- Uses environment variables for sensitive data (API keys).
- Modular code with clear separation of concerns (agent logic vs. configuration).
- Comprehensive error handling and user-friendly prompts.
- Detailed docstrings and comments for maintainability.

## Limitations

- This is a basic implementation and does not constitute a true AGI; it relies on external AI models.
- Performance depends on OpenAI API availability and rate limits.
- For production use, consider adding features like logging, persistence, and advanced task decomposition.

## License

This project is intended for educational and experimental purposes. Use responsibly and in compliance with OpenAI's terms of service.

## Contributing

Feel free to fork the project and submit pull requests for improvements, such as adding memory management, multi-modal capabilities, or integration with other tools.