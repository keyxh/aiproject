# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = self.api_key\n\n    def generate_response(self, prompt):\n        response = openai.Completion.create(\n            engine=\"text-davinci-002\",\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n\n# Example usage:\nif __name__ == \"__main__\":\n    api_key = \"your-openai-api-key\"\n    agi_instance = AGI(api_key)\n    prompt = \"Explain the concept of artificial general intelligence in simple terms.\"\n    print(agi_instance.generate_response(prompt))\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project aims to create a truly artificial general intelligence (AGI) using the OpenAI API.\n\n## Features\n- Uses OpenAI's GPT-3 model to generate responses to prompts.\n- Simple API to interact with the AGI.\n\n## Setup\n\n1. Install the required package:\n    ```bash\n    pip install openai\n    ```\n\n2. Set your OpenAI API key in the `agi.py` file:\n    ```python\n    api_key = \"your-openai-api-key\"\n    ```\n\n## Usage\n\nTo use the AGI, create an instance of the `AGI` class and call the `generate_response` method with a prompt.\n\n```python\nfrom agi import AGI\n\napi_key = \"your-openai-api-key\"\nagi_instance = AGI(api_key)\nprompt = \"What is the weather like today?\"\nprint(gagi_instance.generate_response(prompt))\n```"
        }
    ]
}
```