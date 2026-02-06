# agi

```json
{
    "files": [
        {
            "filename": "agi.py",
            "content": "import openai

# 初始化OpenAI API客户端
openai.api_key = 'your_openai_api_key'

def generate_response(prompt):
    # 调用OpenAI的text-davinci-003模型生成文本
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150  # 设置生成文本的最大字符数
    )
    # 返回生成文本的第一行作为回复
    return response.choices[0].text.strip()

if __name__ == '__main__':
    user_input = input('请输入您的问题: ')
    print(generate_response(user_input))
"
        },
        {
            "filename": "config.json",
            "content": "{\n    \"openai_api_key\": \"your_openai_api_key\"\n}"
        }
    ]
}
```