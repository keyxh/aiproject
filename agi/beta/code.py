# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "# agi.py\n\nimport openai\nfrom flask import Flask, request, jsonify\n\napp = Flask(__name__)\n\n# 设置OpenAI API密钥\nopenai.api_key = 'your-api-key'\n\n\n\n@app.route('/generate', methods=['POST'])\n\ndef generate_response):\n    # 获取用户输入的数据\n    data = request.get_json()\n    prompt = data.get('prompt')\n    if not prompt:\n        return jsonify({'error': 'No prompt provided'}), 400\n\n    # 使用OpenAI GPT-3 API生成响应\n    response = openai.Completion.create(\n        engine='text-davinci-002',\n        prompt=prompt,\n        max_tokens=150\n    )\n    return jsonify({'response': response.choices[0].text.strip()}), 200\n\n\nif __name__ == '__main__':\n    app.run(debug=True)\n"
        },
        {
            "filename": "requirements.txt",
            "content": "Flask==2.0.3\nopenai\n"
        },
        {
            "filename": "README.md",
            "content": "# AGI Project\n\nThis repository contains the code for a project aiming to create an Artificial General Intelligence (AGI) using the OpenAI API.\n\n## Overview\n\nThe project includes a simple Flask web service that can accept text prompts and generate responses using the GPT-3 model provided by OpenAI.\n\n## Features\n\n- Accepts text prompts via a POST request to the `/generate` endpoint.\n- Uses the OpenAI GPT-3 API to generate responses.\n\n## Setup\n\n1. Clone the repository:\n    ```bash\n    git clone https://github.com/your-username/agi.git\n    cd agi\n    ```\n\n2. Install the required packages:\n    ```bash\n    pip install -r requirements.txt\n    ```\n\n3. Start the Flask server:\n    ```bash\n    python agi.py\n    ```\n\n4. Test the service by sending a POST request to `http://localhost:5000/generate` with a JSON body containing a `prompt` field.\n\n## License\n\nThis project is licensed under the [MIT License](https://github.com/your-username/agi/blob/main/LICENSE).\n"
        }
    ]
}
```