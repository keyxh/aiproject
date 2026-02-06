# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\n\nclass AGI:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        self.api = openai.OpenAI(api_key=self.api_key)\n\n    def generate_response(self, prompt):\n        response = self.api.Completion.create(\n            engine=\"text-davinci-002\",\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n\n# Example usage:\nif __name__ == \"__main__\":\n    api_key = 'your_openai_api_key_here'\n    agi_instance = AGI(api_key=api_key)\n    user_input = input('Enter your prompt: ')\n    print(agi_instance.generate_response(user_input))\n"
        },
        {
            "filename": "requirements.txt",
            "content": "openai==0.27.0\n"
        }
    ]
}
```