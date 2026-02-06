import openai
import os
import logging
from typing import List, Dict, Any, Optional

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# 从环境变量加载OpenAI API密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API密钥未设置，请设置环境变量 OPENAI_API_KEY")

# 初始化OpenAI客户端
openai.api_key = OPENAI_API_KEY

class AGIEngine:
    """
    AGI（通用人工智能）引擎核心类，封装与OpenAI API交互逻辑，支持多轮对话、上下文管理、任务规划等。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.conversation_history: List[Dict[str, Any]] = []
        logging.info(f"AGI引擎初始化，使用模型: {model}")

    def add_message(self, role: str, content: str):
        """
        添加一条对话消息到历史记录中。
        :param role: 角色，如 'user' 或 'assistant'
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})
        logging.debug(f"添加消息: {role} - {content}")

    def get_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        从OpenAI API获取响应。
        :param prompt: 输入提示
        :param max_tokens: 最大响应长度
        :return: 模型生成的响应文本
        """
        # 将用户输入添加到历史记录
        self.add_message("user", prompt)

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=self.conversation_history,
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            assistant_response = response.choices[0].message.content
            self.add_message("assistant", assistant_response)
            logging.info(f"模型响应: {assistant_response[:100]}...")
            return assistant_response
        except Exception as e:
            logging.error(f"调用OpenAI API失败: {e}")
            return "抱歉，请求失败，请稍后再试。"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history.clear()
        logging.info("对话历史已重置。")

    def set_temperature(self, temperature: float):
        """
        设置生成温度。
        :param temperature: 温度值，0.0~1.0
        """
        self.temperature = temperature
        logging.info(f"温度设置为: {temperature}")

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        获取当前对话历史。
        :return: 对话历史列表
        """
        return self.conversation_history.copy()

# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.7)

    # 与AGI交互
    print("欢迎使用AGI系统！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.get_response(user_input)
        print(f"AGI: {response}")