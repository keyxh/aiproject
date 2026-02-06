# AGI Project

A simple implementation of an Artificial General Intelligence (AGI) using OpenAI API.

## Overview

This project aims to simulate AGI behavior by leveraging OpenAI's powerful language models. It provides a command-line interface for interactive conversations with the AGI.

## Features

- Interactive chat with AGI using OpenAI API
- Simple memory system to maintain context
- Configurable model settings
- Easy to run and extend

## Setup

1. **Clone the repository** (if applicable).

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```
   - Optionally, set the model name:
     ```
     MODEL_NAME=gpt-4  # or another model
     ```

4. **Run the AGI system**:
   ```
   python main.py
   ```

## Usage

- Start the program and type your messages.
- Type `exit` to quit.
- Type `reset` to clear the conversation memory.

## Code Structure

- `main.py`: Entry point with CLI.
- `agi.py`: Core AGI class with memory and API interaction.
- `config.py`: Configuration management.
- `requirements.txt`: List of dependencies.

## Contributing

As a junior engineer, this is a basic implementation. Future improvements could include:
- Enhanced memory systems (e.g., vector databases)
- Multi-modal capabilities
- Integration with external tools
- Web interface

## License

This project is for educational purposes. Use responsibly.