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
        添加一条对话消息到历史记录中。
        :param role: "user" 或 "assistant"
        :param content: 消息内容
        """
        self.conversation_history.append({"role": role, "content": content})
        logger.debug(f"添加消息: {role} - {content}")

    def get_response(self, prompt: str, max_tokens: int = 500) -> str:
        """
        通过OpenAI API获取模型响应。
        :param prompt: 用户输入或系统提示
        :param max_tokens: 最大响应长度
        :return: 模型生成的响应文本
        """
        # 将历史对话添加到上下文中
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
            logger.info(f"模型响应: {response_text}")
            return response_text
        except Exception as e:
            logger.error(f"调用OpenAI API失败: {e}")
            return "抱歉，我无法处理该请求。"

    def reset_conversation(self):
        """
        重置对话历史。
        """
        self.conversation_history.clear()
        logger.info("对话历史已重置")

    def set_system_prompt(self, system_prompt: str):
        """
        设置系统提示词，用于引导模型行为。
        :param system_prompt: 系统提示内容
        """
        self.conversation_history.insert(0, {"role": "system", "content": system_prompt})
        logger.info("系统提示已设置")

    def get_conversation_summary(self) -> str:
        """
        获取当前对话历史的摘要。
        :return: 对话摘要文本
        """
        if not self.conversation_history:
            return "无对话历史。"
        
        # 简化摘要：仅提取最后5条消息
        recent_messages = self.conversation_history[-5:]
        summary = "对话摘要：\n" + "\n".join([
            f"{msg['role']}: {msg['content']}" for msg in recent_messages
        ])
        return summary


# 示例使用
if __name__ == "__main__":
    # 初始化AGI引擎
    agi = AGIEngine(model="gpt-4", temperature=0.7)
    
    # 设置系统提示
    agi.set_system_prompt("你是一个具备通用智能的AI助手，能够回答各种问题、执行任务、进行推理和规划。")
    
    # 与用户交互
    print("欢迎使用AGI引擎！输入 'quit' 退出。")
    while True:
        user_input = input("用户: ")
        if user_input.lower() == "quit":
            print("再见！")
            break
        
        response = agi.get_response(user_input)
        print(f"AGI: {response}")
        
        # 可选：打印对话摘要
        # print(agi.get_conversation_summary())