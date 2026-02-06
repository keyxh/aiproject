# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": """
import os
import json
from typing import Dict, List
import requests

class AGI:
  def __init__(self, api_key: str):
    self.api_key = api_key
    self.api_url = 'https://api.openai.com/v1'

  def get_response(self, prompt: str) -> str:
    """
    获取模型的响应。
    
    参数：
    prompt (str): 输入的提示。
    
    返回：
    str: 模型的响应。
    """
    headers = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'prompt': prompt,
      'max_tokens': 2048,
      'temperature': 0.7
    }
    response = requests.post(f'{self.api_url}/completions', headers=headers, json=data)
    return response.json()['choices'][0]['text']

  def converse(self, prompt: str) -> str:
    """
    与模型进行对话。
    
    参数：
    prompt (str): 输入的提示。
    
    返回：
    str: 模型的响应。
    """
    return self.get_response(prompt)

def main():
  api_key = 'YOUR_API_KEY'  # 替换为你的 API 密钥
  agi = AGI(api_key)
  prompt = 'Hello, how are you?'
  response = agi.converse(prompt)
  print(response)

if __name__ == '__main__':
  main()
"""
    },
    {
      "filename": "requirements.txt",
      "content": """
requests
"""
    },
    {
      "filename": "README.md",
      "content": """
# AGI 项目
实现一个真正意义上的 AGI，如果使用的模型 API 用 OpenAI API。
"""
    }
  ]
}
```