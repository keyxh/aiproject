# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) that aims to implement a true AGI using OpenAI API. I'm acting as a mid-level engineer.

Let me think about what a mid-level engineer would generate:
- Practical implementation code
- Well-structured and modular
- Following best practices
- With necessary comments and documentation
- Not too abstract (like an architect) but also not too basic

For a true AGI implementation using OpenAI API, I should create:
1. A main orchestration layer
2. A prompt management system
3. Memory/context management
4. Tool/function calling capabilities
5. A simple but extensible architecture

Let me create a comprehensive but practical implementation. I'll structure it as:
- Main entry point
- Core AGI engine
- Prompt templates
- Memory system
- Tool system
- Configuration

I'll write this in Python since it's the most common language for working with OpenAI APIs and AI projects.

The JSON structure should contain multiple files that form a coherent project structure.

Let me create meaningful, runnable code with good practices:

1. `config.py` - Configuration management
2. `core/agi_engine.py` - Main AGI engine
3. `memory/memory_manager.py` - Memory management
4. `tools/tool_manager.py` - Tool calling system
5. `prompts/prompt_manager.py` - Prompt templates and management
6. `main.py` - Entry point
7. `requirements.txt` - Dependencies

This represents what a mid-level engineer would produce: practical, modular, well-documented code that can actually run and be extended.
</think>

```json
{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "openai>=1.0.0\npython-dotenv>=1.0.0\npydantic>=2.0.0\nloguru>=0.7.0\n"
        },
        {
            "filename": "config.py",
            "content": "\"\"\"\n配置文件 - 管理AGI系统的所有配置\n\"\"\"\nfrom pathlib import Path\nfrom typing import Optional\nfrom pydantic import BaseModel\nfrom dotenv import load_dotenv\nimport os\n\n# 加载环境变量\nload_dotenv()\n\n\nclass OpenAIConfig(BaseModel):\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model: str = os.getenv(\"OPENAI_MODEL\", \"gpt-4\")\n    max_tokens: int = int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\"))\n    temperature: float = float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\"))\n    timeout: int = int(os.getenv(\"OPENAI_TIMEOUT\", \"60\"))\n\n\nclass MemoryConfig(BaseModel):\n    \"\"\"记忆系统配置\"\"\"\n    max_short_term记忆: int = int(os.getenv(\"MAX_SHORT_TERM_MEMORY\", \"10\"))\n    memory_file: str = os.getenv(\"MEMORY_FILE\", \"agi_memory.json\")\n\n\nclass AGIConfig(BaseModel):\n    \"\"\"AGI主配置\"\"\"\n    openai: OpenAIConfig = OpenAIConfig()\n    memory: MemoryConfig = MemoryConfig()\n    debug_mode: bool = os.getenv(\"DEBUG_MODE\", \"false\").lower() == \"true\"\n    system_prompt: str = os.getenv(\"SYSTEM_PROMPT\", \"你是一个通用人工智能助手，具备推理、学习和解决问题的能力。\")\n\n\n# 全局配置实例\nconfig = AGIConfig()\n"
        },
        {
            "filename": "core/agi_engine.py",
            "content": "\"\"\"\nAGI核心引擎 - 实现通用人工智能的主要逻辑\n\"\"\"\nfrom typing import List, Dict, Any, Optional\nfrom loguru import logger\nfrom openai import OpenAI\nfrom pydantic import BaseModel\n\nfrom config import config\nfrom memory.memory_manager import MemoryManager\nfrom tools.tool_manager import ToolManager\nfrom prompts.prompt_manager import PromptManager\n\n\nclass Message(BaseModel):\n    \"\"\"消息模型\"\"\"\n    role: str  # \"user\", \"assistant\", \"system\"\n    content: str\n    timestamp: Optional[str] = None\n\n\nclass AGIEngine:\n    \"\"\"\n    AGI核心引擎类\n    \n    负责协调所有组件，实现智能对话和任务处理\n    \"\"\"\n\n    def __init__(self):\n        \"\"\"初始化AGI引擎\"\"\"\n        self.client = OpenAI(api_key=config.openai.api_key)\n        self.memory_manager = MemoryManager()\n        self.tool_manager = ToolManager()\n        self.prompt_manager = PromptManager()\n        \n        logger.info(\"AGI引擎初始化完成\")\n\n    def chat(self, user_input: str) -> str:\n        \"\"\"\n        处理用户输入并生成响应\n        \n        Args:\n            user_input: 用户输入的文本\n            \n        Returns:\n            AGI生成的响应文本\n        \"\"\"\n        try:\n            # 1. 检索相关记忆\n            relevant_memories = self.memory_manager.retrieve(user_input)\n            \n            # 2. 构建对话上下文\n            messages = self._build_context(user_input, relevant_memories)\n            \n            # 3. 调用OpenAI API\n            response = self._call_llm(messages)\n            \n            # 4. 提取并执行工具调用\n            tool_calls = self._parse_tool_calls(response)\n            if tool_calls:\n                tool_results = self._execute_tool_calls(tool_calls)\n                # 将工具结果加入上下文，再次调用\n                messages.append({\"role\": \"assistant\", \"content\": response})\n                messages.extend(tool_results)\n                response = self._call_llm(messages)\n            \n            # 5. 存储新的记忆\n            self.memory_manager.store(user_input, response)\n            \n            return response\n            \n        except Exception as e:\n            logger.error(f\"处理用户输入时出错: {e}\")\n            return f\"抱歉，处理您的请求时出现错误: {str(e)}\"\n\n    def _build_context(self, user_input: str, relevant_memories: List[Dict]) -> List[Dict]:\n        \"\"\"\n        构建对话上下文\n        \n        Args:\n            user_input: 用户输入\n            relevant_memories: 相关记忆\n            \n        Returns:\n            格式化的消息列表\n        \"\"\"\n        messages = []\n        \n        # 添加系统提示\n        system_prompt = self.prompt_manager.get_system_prompt()\n        messages.append({\"role\": \"system\", \"content\": system_prompt})\n        \n        # 添加相关记忆\n        if relevant_memories:\n            memory_context = self.prompt_manager.format_memory_context(relevant_memories)\n            messages.append({\"role\": \"system\", \"content\": memory_context})\n        \n        # 添加短期记忆（历史对话）\n        short_term记忆 = self.memory_manager.get_short_term_history()\n        for msg in short_term记忆:\n            messages.append({\"role\": msg[\"role\"], \"content\": msg[\"content\"]})\n        \n        # 添加当前用户输入\n        messages.append({\"role\": \"user\", \"content\": user_input})\n        \n        return messages\n\n    def _call_llm(self, messages: List[Dict]) -> str:\n        \"\"\"\n        调用OpenAI LLM\n        \n        Args:\n            messages: 消息列表\n            \n            Returns:\n                LLM生成的响应\n        \"\"\"\n        response = self.client.chat.completions.create(\n            model=config.openai.model,\n            messages=messages,\n            max_tokens=config.openai.max_tokens,\n            temperature=config.openai.temperature,\n        )\n        \n        return response.choices[0].message.content\n\n    def _parse_tool_calls(self, response: str) -> List[Dict]:\n        \"\"\"\n        解析LLM响应中的工具调用\n        \n        Args:\n            response: LLM响应\n            \n            Returns:\n            工具调用列表\n        \"\"\"\n        # 简单实现：检查响应中是否包含工具调用标记\n        # 实际项目中可以使用更复杂的解析逻辑\n        if \"<tool_call>\" in response and \"</tool_call>\" in response:\n            start = response.find(\"<tool_call>\") + len(\"<tool_call>\")\n            end = response.find(\"</tool_call>\")\n            tool_call_str = response[start:end]\n            \n            import json\n            try:\n                return json.loads(tool_call_str)\n            except json.JSONDecodeError:\n                logger.warning(\"无法解析工具调用\")\n                return []\n        \n        return []\n\n    def _execute_tool_calls(self, tool_calls: List[Dict]) -> List[Dict]:\n        \"\"\"\n        执行工具调用\n        \n        Args:\n            tool_calls: 工具调用列表