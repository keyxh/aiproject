# agi

 "files": [
    {
      "filename": "main.py",
      "content": "'''\n# AGI模型主要接口\n\nimport openai\n\nclass AGIModel:\n    def __init__(self, api_key):\n        self.api_key = api_key\n        self.openai_api = openai.API(key=api_key)\n\n    def request(self, prompt):\n        response = self.openai_api.create_completion(\n            engine=\"davinci\",\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n'''\n",
    {
      "filename": "agi.py",
      "content": "'''\n# AGI模型实现代码\n\nfrom main import AGIModel\n\nclass MyAGI(AGIModel):\n    def __init__(self, api_key):\n        super().__init__(api_key)\n\n    def advanced_request(self, prompt, engine=\"davinci\"):\n        response = self.openai_api.create_completion(\n            engine=engine,\n            prompt=prompt,\n            max_tokens=150\n        )\n        return response.choices[0].text.strip()\n'''\n",
    {
      "filename": "requirements.txt",
      "content": "openai==0.3.5\n"
    }
  ]
}