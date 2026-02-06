import openai
import os
import logging
from typing import List, Dict, Any, Optional

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 从环境变量加载OpenAI API密钥
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise ValueError("请设置环境变量 OPENAI_API_KEY")

# 初始化OpenAI客户端
openai.api_key = OPENAI_API_KEY

class AGIEngine:
    """
    AGI（通用人工智能）引擎核心类。
    该类封装了与OpenAI API交互的能力，支持多轮对话、上下文管理、任务规划等。
    """
    def __init__(self, model: str = "gpt-4", temperature: float = 0.7):
        self.model = model
        self.temperature = temperature
        self.conversation_history: List[Dict[str, Any]] = []
        logger.info(f"AGI引擎初始化，使用模型: {model}")

    def add_message(self, role: str, content: str):
        """
        向对话历史中添加一条消息。
        :param role: 消息角色（"user" 或 "assistant"）
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})
        logger.debug(f"添加消息: {role} - {content}")

    def generate_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        使用OpenAI API生成响应。
        :param prompt: 输入提示
        :param max_tokens: 最大响应长度
        :return: 生成的响应文本
        """
        # 将对话历史与新提示合并
        messages = self.conversation_history + [{"role": "user", "content": prompt}]

        try:
            response = openai.ChatCompletion.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                max_tokens=max_tokens
            )
            response_text = response.choices[0].message.content.strip()
            self.add_message("assistant", response_text)
            logger.info(f"生成响应: {response_text[:100]}...")
            return response_text
        except Exception as e:
            logger.error(f"生成响应失败: {e}")
            return "抱歉，我无法处理该请求。"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history = []
        logger.info("对话历史已重置。")

    def set_temperature(self, temperature: float):
        """
        设置生成响应的温度参数。
        :param temperature: 温度值（0.0 ~ 1.0）
        """
        self.temperature = temperature
        logger.info(f"温度参数已设置为: {temperature}")

    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        获取当前对话历史。
        :return: 对话历史列表
        """
        return self.conversation_history.copy()

# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.8)

    # 与AGI交互
    print("欢迎使用AGI！输入 'quit' 退出。")
    while True:
        user_input = input("你: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.generate_response(user_input)
        print(f"AGI: {response}")