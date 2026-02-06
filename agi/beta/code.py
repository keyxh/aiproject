# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = self.api_key\n\n    def process_query(self, query):\n        try:\n            response = openai.Completion.create(\n                engine=\"text-davinci-002\",\n                prompt=query,\n                max_tokens=150\n            )\n            return response.choices[0].text.strip()\n        except Exception as e:\n            return f\"Error occurred: {str(e)}\"\n\n# Usage example\nif __name__ == \"__main__\":\n    api_key = \"your_openai_api_key_here\"\n    agi_instance = AGI(api_key)\n    user_query = \"What is the latest in AI research?\"\n    answer = agi_instance.process_query(user_query)\n    print(answer)\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis project aims to create an Artificial General Intelligence (AGI) using the OpenAI API.\n\n## Features\n- Utilizes OpenAI's GPT-3 model to process natural language queries.\n- Can be extended to include more advanced functionalities like reasoning, learning, and problem-solving.\n\n## Setup\n\n1. Install OpenAI Python client:\n\n    ```bash\n    pip install openai\n    ```\n\n2. Set up your OpenAI API key:\n\n    - Sign up for an OpenAI account at [https://openai.com/](https://openai.com/).\n    - Create a new API key in your OpenAI dashboard.\n    - Replace `your_openai_api_key_here` in `agi.py` with your API key.\n\n## Usage\n\nRun the `agi.py` script to interact with the AGI.\n\n```bash\npython agi.py\n```\n"
        }
    ]
}
```