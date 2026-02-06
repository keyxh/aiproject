import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.environ["OPENAI_API_KEY"]

class AGIEngine:
    """
    初级工程师实现的AGI引擎基础框架。
    目前通过调用OpenAI API实现基础对话与推理能力。
    未来可扩展为多模态、记忆、规划等模块。
    """
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.model = model
        self.conversation_history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str):
        """
        向对话历史中添加一条消息。
        role: "user" 或 "assistant"
        """
        self.conversation_history.append({"role": role, "content": content})

    def generate_response(self, user_input: str) -> str:
        """
        根据用户输入生成AI响应。
        使用OpenAI API调用模型。
        """
        self.add_message("user", user_input)

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history
            )
            assistant_reply = response.choices[0].message.content
            self.add_message("assistant", assistant_reply)
            return assistant_reply
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history = []

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