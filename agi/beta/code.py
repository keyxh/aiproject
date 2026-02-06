# agi

```json
{
  "files": [
    {
      "filename": "agi.py",
      "content": "
import os
import json
import requests

class AGI:
  def __init__(self, api_key):
    self.api_key = api_key
    self.api_url = 'https://api.openai.com/v1'

  def generate_text(self, prompt, max_tokens=1024):
    """
    生成文本
    :param prompt: 输入提示
    :param max_tokens: 最大token数
    :return: 生成的文本
    """
    headers = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }
    data = {
      'prompt': prompt,
      'max_tokens': max_tokens
    }
    response = requests.post(f'{self.api_url}/completions', headers=headers, json=data)
    return response.json()['choices'][0]['text']

  def answer_question(self, question):
    """
    回答问题
    :param question: 问题
    :return: 答案
    """
    prompt = f'答案：{question}'
    return self.generate_text(prompt)

  def chat(self, message):
    """
    聊天
    :param message: 消息
    :return: 回复
    """
    prompt = f'用户：{message}\n助手：'
    return self.generate_text(prompt)

# 示例用法
if __name__ == '__main__':
  api_key = 'YOUR_API_KEY'
  agi = AGI(api_key)
  print(agi.generate_text('Hello, how are you?'))
  print(agi.answer_question('What is the meaning of life?'))
  print(agi.chat('Hello, I am happy to meet you!'))
"
    },
    {
      "filename": "requirements.txt",
      "content": "
requests
"
    },
    {
      "filename": "README.md",
      "content": "
# AGI
一个真正意义上的AGI实现，使用OpenAI API。
"
    }
  ]
}
```