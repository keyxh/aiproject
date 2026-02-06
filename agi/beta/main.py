import openai
import os
from typing import List, Dict, Any

# 配置OpenAI API密钥
os.environ["OPENAI_API_KEY"] = "your_openai_api_key_here"  # 替换为你的实际API密钥

# 初始化OpenAI客户端
openai.api_key = os.getenv("OPENAI_API_KEY")

class AGIEngine:
    """
    AGI引擎核心类，封装与OpenAI API交互逻辑，支持多轮对话、上下文管理、任务分解等。
    """
    def __init__(self):
        self.conversation_history: List[Dict[str, Any]] = []
        self.system_prompt = "You are an AGI assistant designed to understand and execute complex tasks with human-like reasoning. Respond in a clear, concise, and helpful manner."

    def add_system_prompt(self, prompt: str):
        """
        设置系统提示词，用于引导模型行为。
        """
        self.system_prompt = prompt

    def generate_response(self, user_input: str) -> str:
        """
        生成AI响应，使用OpenAI API。
        :param user_input: 用户输入文本
        :return: AI生成的响应文本
        """
        # 构建对话历史
        messages = [
            {"role": "system", "content": self.system_prompt}
        ] + self.conversation_history + [{"role": "user", "content": user_input}]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",  # 或者使用 "gpt-3.5-turbo" 以节省成本
                messages=messages,
                temperature=0.7,
                max_tokens=1500
            )
            ai_response = response.choices[0].message.content
            # 更新对话历史
            self.conversation_history.append({"role": "user", "content": user_input})
            self.conversation_history.append({"role": "assistant", "content": ai_response})
            return ai_response
        except Exception as e:
            return f"Error: {str(e)}"

    def reset_conversation(self):
        """
        重置对话历史，开始新的对话。
        """
        self.conversation_history = []

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        获取当前对话历史。
        :return: 对话历史列表
        """
        return self.conversation_history

# 示例使用
if __name__ == "__main__":
    agi = AGIEngine()
    agi.add_system_prompt("You are a highly intelligent assistant capable of solving complex problems. Think step by step.")

    print("AGI Engine Initialized. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        response = agi.generate_response(user_input)
        print(f"AGI: {response}")