# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = api_key\n\n    def generate_response(self, prompt):\n        response = openai.Completion.create(\n            engine='text-davinci-002',\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n\n# Example usage\nif __name__ == '__main__':\n    api_key = 'your-openai-api-key'\n    agi_instance = AGI(api_key)\n    prompt = 'What is the latest AI technology trend?'\n    response = agi_instance.generate_response(prompt)\n    print(response)\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project is an attempt to create an Artificial General Intelligence (AGI) using the OpenAI API.\n\n## Features\n\n- Uses OpenAI's text-davinci-002 model for generating responses.\n- Can handle a variety of prompts and generate contextually appropriate responses.\n\n## Setup\n\n1. Install OpenAI Python package:\n    ```bash\n    pip install openai\n    ```\n\n2. Set up your OpenAI API key:\n    - Go to https://platform.openai.com/account/api-keys\n    - Create a new API key\n    - Store your API key securely, e.g., in an environment variable.\n\n3. Run the AGI instance:\n    ```bash\n    python agi.py\n    ```\n\n## Usage\n\n```python\nfrom agi import AGI\n\napi_key = 'your-openai-api-key'\nagi_instance = AGI(api_key)\nprompt = 'What is the latest AI technology trend?'\nresponse = agi_instance.generate_response(prompt)\nprint(response)\n```"
        }
    ]
}
```