# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = api_key\n\n    def generate_response(self, prompt):\n        response = openai.Completion.create(\n            engine=\"text-davinci-002\",\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n\n# Example usage:\nif __name__ == \"__main__\":\n    api_key = \"your-openai-api-key\"\n    agi_instance = AGI(api_key)\n    prompt = \"What is the impact of AI on society?\"\n    print(agi_instance.generate_response(prompt))\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project aims to create an Artificial General Intelligence (AGI) using the OpenAI API.\n\n## Features\n- Uses OpenAI's GPT-3 model to generate human-like responses.\n- Can be extended with additional AI capabilities.\n\n## Setup\n1. Install OpenAI Python package:\n   ```bash\n   pip install openai\n   ```\n2. Obtain an OpenAI API key from https://platform.openai.com/ and set the `OPENAI_API_KEY` environment variable.\n\n## Usage\n```python\nfrom agi import AGI\n\n# Initialize the AGI instance with your API key\nagi_instance = AGI(api_key=\"your-openai-api-key\")\n\n# Generate a response to a prompt\nresponse = agi_instance.generate_response(\"What is the impact of AI on society?\")\nprint(response)\n```\n\n## Contributing\nContributions are welcome. Please follow the coding standards and submit pull requests to the main repository.\n"
        }
    ]
}
```