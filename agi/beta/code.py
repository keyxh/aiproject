# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# Set your OpenAI API key\nopenai.api_key = 'your-api-key'\n\n\n@app.route('/generate', methods=['POST'])\ndef generate_response():\n    data = request.get_json()\n    prompt = data.get('prompt', '')\n    max_tokens = data.get('max_tokens', 50)\n\n    # Ensure that the prompt and max_tokens are provided\n    if not prompt or not isinstance(max_tokens, int) or max_tokens <= 0:\n        return jsonify({'error': 'Invalid request'}), 400\n\n    # Call the OpenAI API to generate a response\n    response = openai.Completion.create(\n        engine='text-davinci-002',  # or the engine you prefer\n        prompt=prompt,\n        max_tokens=max_tokens\n    )\n\n    return jsonify({'response': response.choices[0].text.strip()}), 200\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"
        },
        {
            "filename": "requirements.txt",
            "content": "Flask==2.0.1\nopenai==0.27.0\n"
        }
    ]
}
```