# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom flask import Flask, request, jsonify\n\n# Initialize the OpenAI API client\nopenai.api_key = 'your-openai-api-key'\n\n# Create a Flask app\napp = Flask(__name__)\n\n# Endpoint to generate text using OpenAI's GPT-3 model\n@app.route('/generate', methods=['POST'])\ndef generate_text():\n    data = request.get_json()\n    prompt = data.get('prompt')\n    max_tokens = data.get('max_tokens', 50)\n\n    # Ensure that the prompt is not empty\n    if not prompt:\n        return jsonify({'error': 'Prompt is required'}), 400\n\n    # Generate text using the OpenAI API\n    response = openai.Completion.create(\n        engine='text-davinci-002',\n        prompt=prompt,\n        max_tokens=max_tokens\n    )\n    generated_text = response.choices[0].text.strip()\n\n    return jsonify({'generated_text': generated_text})\n\n# Run the Flask app\nif __name__ == '__main__':\n    app.run(debug=True)\n"
        },
        {
            "filename": "requirements.txt",
            "content": "Flask==2.0.3\nopenai==0.27.0\n"
        }
    ]
}
```