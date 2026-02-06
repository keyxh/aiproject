# AGI Project

This project is a basic implementation of an Artificial General Intelligence (AGI) system using the OpenAI API. It simulates intelligent task processing through interactive prompts.

## Overview

The system allows users to input tasks, which are then processed by OpenAI's GPT models (e.g., GPT-4) to generate responses. This is a simplified AGI simulation for educational and experimental purposes.

## Features

- Interactive command-line interface for task input.
- Modular design with separate modules for API integration, task management, and configuration.
- Error handling and logging for robustness.
- Easy configuration via environment variables.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key (sign up at [OpenAI](https://platform.openai.com/))

## Installation

1. Clone the repository or download the code files.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root directory and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
   Optionally, you can set other variables like `MODEL_NAME` or `MAX_TOKENS` in the `.env` file and update `config.py` accordingly.

## Usage

Run the main script to start the AGI system:
```bash
python agi_main.py
```

Once running, you can enter tasks at the prompt. For example:
```
Enter a task (or 'quit' to exit): Explain quantum computing in simple terms.
```

The system will use OpenAI's API to generate a response and display it.

To exit, type `quit` or press Ctrl+C.

## Project Structure

- `agi_main.py`: Main entry point with the interactive loop.
- `openai_integration.py`: Handles all OpenAI API calls with error management.
- `task_manager.py`: Manages task storage and processing logic.
- `config.py`: Loads configuration from environment variables.
- `requirements.txt`: Lists project dependencies.
- `README.md`: This documentation file.

## Limitations

- This is not a true AGI; it relies on external API calls and has no autonomous learning or reasoning capabilities.
- Performance depends on OpenAI API availability and rate limits.
- The system is basic and intended for demonstration; it can be extended for more complex use cases.

## Future Enhancements

- Add support for task decomposition and multi-step reasoning.
- Implement memory or context management for ongoing conversations.
- Integrate with other APIs or tools for enhanced functionality.
- Add a web or GUI interface for better user experience.

## License

This project is open-source and available under the MIT License. Feel free to modify and distribute.

## Contributing

Contributions are welcome! Please open issues or pull requests for suggestions and improvements.