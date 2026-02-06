import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    初级工程师实现的AGI引擎基础框架。
    目前通过调用OpenAI API模拟AGI能力，后续可扩展为多模型、记忆、推理等模块。
    """
    def __init__(self):
        self.history: List[Dict[str, Any]] = []  # 对话历史记录

    def generate_response(self, user_input: str) -> str:
        """
        使用OpenAI API生成响应。
        输入：用户问题或指令
        输出：模型生成的自然语言响应
        """
        self.history.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 可替换为gpt-4等更高级模型
                messages=self.history,
                max_tokens=150,
                temperature=0.7
            )
            assistant_response = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": assistant_response})
            return assistant_response
        except Exception as e:
            return f"Error: {str(e)}"

    def reset(self):
        """
        重置对话历史。
        """
        self.history.clear()

    def get_history(self) -> List[Dict[str, Any]]:
        """
        获取当前对话历史。
        """
        return self.history

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine()
    print("AGI引擎已启动。输入 'quit' 退出。")
    
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.generate_response(user_input)
        print(f"AGI: {response}")