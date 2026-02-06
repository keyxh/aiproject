import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，负责与OpenAI API交互，模拟通用人工智能行为。
    """
    def __init__(self):
        self.conversation_history: List[Dict[str, Any]] = []

    def send_message(self, user_input: str) -> str:
        """
        向OpenAI模型发送用户消息并返回响应。
        :param user_input: 用户输入的文本
        :return: 模型生成的响应文本
        """
        # 添加用户消息到对话历史
        self.conversation_history.append({"role": "user", "content": user_input})

        # 调用OpenAI API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # 或者使用 "gpt-3.5-turbo" 以节省成本
            messages=self.conversation_history,
            temperature=0.7,
            max_tokens=150
        )

        # 获取模型响应
        assistant_response = response.choices[0].message.content

        # 添加模型响应到对话历史
        self.conversation_history.append({"role": "assistant", "content": assistant_response})

        return assistant_response

    def reset_conversation(self):
        """
        重置对话历史，开始新的对话。
        """
        self.conversation_history.clear()

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        获取当前对话历史。
        :return: 对话历史列表
        """
        return self.conversation_history

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine()
    
    print("欢迎使用AGI引擎！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.send_message(user_input)
        print(f"AGI: {response}")
        
        # 可选：打印当前对话历史
        # print("对话历史:", agi.get_conversation_history())