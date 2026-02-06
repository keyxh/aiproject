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
    # 调用OpenAI的文本生成API
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=150  # 设置生成文本的最大字符数
    )
    # 返回生成的文本
    return response.choices[0].text.strip()

# 示例使用
if __name__ == '__main__':
    user_input = input('请输入您的问题: ')
    generated_response = generate_response(user_input)
    print('AGI响应:', generated_response)"
        }
    ]
}
```