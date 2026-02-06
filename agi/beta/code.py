# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom typing import Any, Dict, Optional\n\nclass AGI:\n    def __init__(self, api_key: str, model: str = 'gpt-3.5-turbo'):\n        self.api_key = api_key\n        self.model = model\n        self.api = openai.OpenAI(api_key=self.api_key)\n\n    def think(self, prompt: str) -> Optional[str]:\n        \"\"\"\n        Generate a response based on the given prompt using the OpenAI API.\n        \"\"\"\n        try:\n            response = self.api.Completion.create(\n                engine=self.model,\n                prompt=prompt,\n                max_tokens=150\n            )\n            return response.choices[0].text.strip()\n        except Exception as e:\n            print(f'Error occurred: {e}')\n            return None\n\n# Usage example\nif __name__ == '__main__':\n    api_key = 'your_openai_api_key_here'\n    agi_instance = AGI(api_key=api_key)\n    prompt = 'What is the latest technology trend in AI?'\n    response = agi_instance.think(prompt=prompt)\n    if response:\n        print(response)\n    else:\n        print('No response received. Please check your OpenAI API key and model.')"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project aims to create an Artificial General Intelligence (AGI) using the OpenAI API.\n\n## Features\n- Utilizes OpenAI's GPT-3.5-turbo model\n- Can process and generate responses to prompts\n\n## Setup\n\n1. Install OpenAI Python package:\n    ```bash\n    pip install openai\n    ```\n\n2. Set your OpenAI API key:\n    ```python\n    import os\n    os.environ['OPENAI_API_KEY'] = 'your_openai_api_key_here'\n    ```\n\n## Usage\n\nTo use the AGI, instantiate the `AGI` class with your OpenAI API key and call the `think` method with a prompt.\n\n```python\nfrom agi import AGI\n\napi_key = 'your_openai_api_key_here'\nagi_instance = AGI(api_key=api_key)\nprompt = 'What is the latest technology trend in AI?'\nresponse = agi_instance.think(prompt=prompt)\nif response:\n    print(response)\nelse:\n    print('No response received. Please check your OpenAI API key and model.')\n```\n\n## License\n\nThis project is licensed under MIT.\n"
        }
    ]
}
```