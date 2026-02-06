# agi

```json
{
    "files": [
        {
            "filename": "agi_project/agi.py",
            "content": "# agi.py\n\nimport openai\nfrom datetime import datetime\n\nclass AGI: \n    def __init__(self, api_key: str): \n        self.api_key = api_key \n        self.api = openai.OpenAI(api_key=self.api_key)\n\n    def generate_response(self, input_text: str, engine: str = 'text-davinci-002') -> str: \n        \n        # Set up the prompt for the OpenAI API\n        prompt = f\"User: {input_text}\nAI: \"\n\n        # Call the OpenAI API to generate a response\n        response = self.api.Completion.create(\n            engine=engine,\n            prompt=prompt,\n            max_tokens=150\n        )\n\n        # Return the generated response from the AI\n        return response.choices[0].text.strip()\n\n# Example usage:\nif __name__ == '__main__':\n    api_key = 'your_openai_api_key_here'\n    agi = AGI(api_key)\n    input_text = 'What is the weather like today?'\n    response = agi.generate_response(input_text)\n    print(response)"
        },
        {
            "filename": "agi_project/main.py",
            "content": "# main.py\n\nfrom agi_project.agi import AGI\n\nif __name__ == '__main__':\n    api_key = 'your_openai_api_key_here'\n    agi = AGI(api_key)\n    user_input = input('Enter your question: ')\n    answer = agi.generate_response(user_input)\n    print('AI Response:', answer)"
        },
        {
            "filename": "agi_project/README.md",
            "content": "# AGI Project\n\nThis project aims to create a truly advanced AI (AGI) using the OpenAI API.\n\n## Features\n- Uses OpenAI's GPT-3 model for natural language processing\n- Provides a simple interface for generating AI responses to user input\n\n## Installation\n\nTo install the project, run:\n\n    pip install -r requirements.txt\n\n## Usage\n\n1. Set up an OpenAI API key at https://openai.com/api_keys\n2. Set the API key in the `main.py` file under the `api_key` variable\n3. Run the `main.py` file to interact with the AGI\n\n## Contributing\n\nContributions are welcome. Please follow the contributing guidelines.\n\n## License\n\nThis project is licensed under the MIT License."
        },
        {
            "filename": "agi_project/requirements.txt",
            "content": "openai==0.27.0\n"
        }
    ]
}
```