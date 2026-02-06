# AGI Project

A simple implementation of an Artificial General Intelligence (AGI) agent using OpenAI API.

## Overview

This project demonstrates a basic AGI agent that engages in intelligent conversations by leveraging OpenAI's GPT models. It's designed as a starting point for exploring AGI concepts with current AI technology.

## Features

- Interactive conversation with context retention.
- Uses OpenAI API for generating intelligent responses.
- Easy setup and configuration via environment variables.
- Error handling and user-friendly prompts.

## Installation

1. **Clone or download the project files.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up OpenAI API key:**
   - Copy `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` and replace `your_api_key_here` with your actual OpenAI API key.

## Usage

Run the AGI agent:

```bash
python main.py
```

Once started, type your messages and press Enter. The agent will respond based on the conversation history. Type 'exit' to quit the program.

Example interaction:
```
AGI Agent started. Type your messages below. Type 'exit' to quit.
You: Hello, how are you?
AGI: I'm doing well, thank you! How can I assist you today?
You: What is artificial general intelligence?
AGI: Artificial General Intelligence (AGI) refers to a type of AI that possesses the ability to understand, learn, and apply knowledge across a wide range of tasks, similar to human intelligence.
You: exit
Exiting AGI Agent. Goodbye!
```

## Code Structure

- `main.py`: Core implementation of the AGIAgent class and the interactive loop.
- `requirements.txt`: Lists Python dependencies (OpenAI client and dotenv for environment variables).
- `.env.example`: Template for setting the OpenAI API key securely.

## Dependencies

- `openai`: Official OpenAI Python client for API access.
- `python-dotenv`: Loads environment variables from a .env file.

## Notes

- This is a simplified simulation and does not represent a true AGI, but it showcases how to build an intelligent agent using existing AI models.
- Ensure you have an active OpenAI API key with sufficient credits.
- The agent maintains conversation history in memory; restarting the program resets the context.

## License

MIT License. Feel free to modify and extend this project for educational or experimental purposes.
