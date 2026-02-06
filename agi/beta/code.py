# agi

```json
{
  "files": [
    {
      "filename": "main.py",
      "content": "# This is a basic example of interacting with the OpenAI API\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Define a function to query the OpenAI API\ndef ask_openai(prompt):\n  response = openai.Completion.create(\n    engine=\"text-davinci-003\",  # Choose the appropriate engine\n    prompt=prompt,\n    max_tokens=150\n  )\n  return response.choices[0].text\n\n# Example usage\nuser_input = input(\"You: \")\nwhile user_input.lower() != \"exit\":\n  response = ask_openai(user_input)\n  print(\"AGI: \" + response)\n  user_input = input(\"You: \")\n"
    }
  ]
}
```
