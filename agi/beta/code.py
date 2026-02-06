# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        openai.api_key = self.api_key\n\n    def generate_response(self, prompt):\n        try:\n            response = openai.Completion.create(\n                engine='text-davinci-002',\n                prompt=prompt,\n                max_tokens=150\n            )\n            return response.choices[0].text.strip()\n        except openai.error.OpenAIError as e:\n            return f'An error occurred: {e}\n\n# Example usage\nif __name__ == '__main__':\n    api_key = 'your_openai_api_key_here'\n    agi_instance = AGI(api_key)\n    prompt = 'Translate the following English text to French: "Hello, how are you?"'\n    translation = agi_instance.generate_response(prompt)\n    print(translation)"
        }
    ]
}
```