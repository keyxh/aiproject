import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_api_key_here"  # 请替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，用于模拟通用人工智能行为。
    当前版本基于OpenAI API实现基础对话与推理能力。
    """
    def __init__(self, model: str = "gpt-4"):
        self.model = model
        self.conversation_history: List[Dict[str, Any]] = []

    def send_message(self, user_input: str) -> str:
        """
        向AGI发送用户消息并获取响应。
        :param user_input: 用户输入的文本
        :return: AGI的回复文本
        """
        # 添加用户消息到对话历史
        self.conversation_history.append({"role": "user", "content": user_input})

        # 调用OpenAI API获取响应
        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history
            )
            assistant_reply = response.choices[0].message.content
            # 添加AI回复到对话历史
            self.conversation_history.append({"role": "assistant", "content": assistant_reply})
            return assistant_reply
        except Exception as e:
            return f"Error: {str(e)}"

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
    print("AGI系统已启动。输入 'quit' 退出。")
    
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.send_message(user_input)
        print(f"AGI: {response}")