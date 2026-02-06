# AGI Project

This project implements a simple Artificial General Intelligence (AGI) agent using OpenAI's API.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Set your OpenAI API key as an environment variable: `export OPENAI_API_KEY='your-api-key'` or create a `.env` file with `OPENAI_API_KEY=your-api-key`.
3. Run the agent: `python agi_agent.py`

## Usage

The agent runs in interactive mode, prompting for user input and generating intelligent responses using OpenAI's GPT models. It maintains conversation history for context-aware interactions.

## Features

- Conversational memory for continuous dialogue
- Uses OpenAI's latest models (default: gpt-4)
- Error handling and extensible for tool integration

## Note

This is a demonstration project and does not achieve true AGI, but showcases how to build an intelligent agent using available APIs as a foundation.