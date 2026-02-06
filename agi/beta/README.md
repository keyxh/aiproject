# AGI Project

This project implements a basic Artificial General Intelligence (AGI) system using OpenAI's API.

## Description

The AGI agent is designed to simulate intelligent behavior by leveraging OpenAI's language models. It can process user inputs, maintain conversation history, and generate responses.

## Features

- Interactive command-line interface.
- Conversation history management.
- Configurable OpenAI model.
- Environment-based configuration.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agi
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

Run the main script:
```bash
python main.py
```

Then, interact with the AGI agent by typing messages. Type 'exit' to quit.

## Configuration

- Modify `config.py` or the `.env` file to change settings.
- The default model is "gpt-4". You can change it in `agi_agent.py`.

## Project Structure

- `main.py`: Entry point for the AGI system.
- `agi_agent.py`: AGI agent class.
- `openai_client.py`: OpenAI API client.
- `config.py`: Configuration module.
- `requirements.txt`: Dependencies list.

## License

This project is licensed under the MIT License.

## Disclaimer

This is a simulation and does not constitute a true AGI. It uses existing AI models for demonstration purposes.
