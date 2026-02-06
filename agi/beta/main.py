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
    raise ValueError("OPENAI_API_KEY 环境变量未设置")

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
        logger.info(f"AGI引擎初始化，使用模型: {model}")

    def add_message(self, role: str, content: str):
        """
        向对话历史中添加一条消息。
        :param role: 消息角色（"user" 或 "assistant"）
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})
        logger.debug(f"添加消息: {role} - {content}")

    def get_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        从OpenAI API获取响应。
        :param prompt: 用户输入或系统提示
        :param max_tokens: 最大响应长度
        :return: AI生成的响应文本
        """
        # 将用户输入添加到历史中
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
            logger.info(f"AI响应: {assistant_response[:100]}...")
            return assistant_response
        except Exception as e:
            logger.error(f"调用OpenAI API失败: {e}")
            return "抱歉，请求失败，请稍后再试。"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history.clear()
        logger.info("对话历史已重置。")

    def set_system_prompt(self, system_prompt: str):
        """
        设置系统提示词，用于引导AI行为。
        :param system_prompt: 系统提示词
        """
        self.conversation_history.insert(0, {"role": "system", "content": system_prompt})
        logger.info("系统提示词已设置。")

    def get_conversation_summary(self) -> str:
        """
        获取当前对话历史的摘要。
        :return: 对话摘要
        """
        if not self.conversation_history:
            return "无对话历史。"
        return "\n".join([f"{msg['role']}: {msg['content'][:80]}..." for msg in self.conversation_history])

# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.7)

    # 设置系统提示词
    agi.set_system_prompt("你是一个具有高度智能和创造力的通用人工智能助手，能够理解并回答各种复杂问题，支持多轮对话和任务规划。")

    # 与用户交互
    print("欢迎使用AGI引擎！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        response = agi.get_response(user_input)
        print(f"AI: {response}")