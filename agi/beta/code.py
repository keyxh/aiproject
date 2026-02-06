# agi

```json
{
  "files": [
    {
      "filename": "main.py",
      "content": "# This is a very basic example of interacting with the OpenAI API.\n# It is not a true AGI, but a starting point for exploration.\n\nimport openai\n\n# Set your OpenAI API key\nopenai.api_key = \"YOUR_API_KEY\"\n\n# Define a function to get a response from the OpenAI API\ndef get_response(prompt):\n    response = openai.Completion.create(\n        engine=\"text-davinci-003\",  # Choose a suitable engine\n        prompt=prompt,\n        max_tokens=100\n    )\n    return response.choices[0].text\n\n# Example usage:\nuser_input = input(\"You: \")\nwhile user_input.lower() != \"exit\":\n    response = get_response(user_input)\n    print(\"AGI: \" + response)\n    user_input = input(\"You: \")\nprint(\"Exiting...\")\n"
    }
  ]
}
```
