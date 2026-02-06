# AGI Project

This project aims to implement an Artificial General Intelligence (AGI) using the OpenAI API.

## Features

- Interactive chat with the AGI agent.
- Conversation memory persistence.
- Basic task execution capabilities.
- Extensible design for future enhancements.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd agi
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

## Usage

Run the main script to start an interactive session:

```bash
python main.py
```

Type your messages, and the AGI will respond. Type 'exit' to quit.

## Project Structure

- `main.py`: Entry point for the AGI system.
- `agi_core.py`: Core AGI logic and OpenAI API integration.
- `config.py`: Configuration management.
- `utils.py`: Utility functions.
- `memory.json`: Stores conversation history (auto-generated).

## Future Work

- Add learning mechanisms.
- Integrate with external tools and APIs.
- Implement more advanced memory and reasoning.

## License

This project is licensed under the MIT License.