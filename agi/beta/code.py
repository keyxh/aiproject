# agi

<think>用户要求我作为中级工程师为项目"agi"生成代码。项目目标是实现一个真正意义上的AGI（通用人工智能），使用OpenAI API。

我需要：
1. 生成实际的、可运行的代码
2. 遵循最佳实践
3. 包含必要的注释和文档
4. 符合中级工程师的角色特点（实现代码，而非架构设计）

让我设计一个合理的AGI系统架构。作为中级工程师，我应该生成实现代码，而不是顶层架构设计。

考虑到AGI的复杂性，我需要创建一个模块化的系统，包括：
1. 核心AGI引擎
2. 记忆系统
3. 工具使用能力
4. 任务规划系统
5. 与OpenAI API的集成

让我创建一个Python项目，包含以下文件：
1. main.py - 主入口
2. core/agi_engine.py - AGI核心引擎
3. memory/memory_system.py - 记忆系统
4. tools/tool_manager.py - 工具管理器
5. planner/task_planner.py - 任务规划器
6. config.py - 配置文件
7. requirements.txt - 依赖

我会用JSON格式返回所有代码文件。
</think>

```json
{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "openai>=1.0.0\npython-dotenv>=1.0.0\nnumpy>=1.24.0\nredis>=4.5.0\nsqlalchemy>=2.0.0\npydantic>=2.0.0\ntiktoken>=0.4.0\nloguru>=0.7.0\n"
        },
        {
            "filename": ".env.example",
            "content": "# OpenAI API配置\nOPENAI_API_KEY=your_api_key_here\nOPENAI_BASE_URL=https://api.openai.com/v1\n\n# 模型配置\nOPENAI_MODEL=gpt-4-turbo-preview\nOPENAI_MAX_TOKENS=4096\nOPENAI_TEMPERATURE=0.7\n\n# 记忆系统配置\nMEMORY_DB_PATH=./data/memory.db\nREDIS_HOST=localhost\nREDIS_PORT=6379\n\n# 系统配置\nDEBUG=true\nLOG_LEVEL=INFO\n"
        },
        {
            "filename": "config.py",
            "content": "\"\"\"\n配置文件 - 管理系统所有配置项\n\"\"\"\nimport os\nfrom pathlib import Path\nfrom dotenv import load_dotenv\nfrom pydantic import BaseModel\n\n# 加载环境变量\nload_dotenv()\n\n\nclass OpenAIConfig(BaseModel):\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    base_url: str = os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\")\n    model: str = os.getenv(\"OPENAI_MODEL\", \"gpt-4-turbo-preview\")\n    max_tokens: int = int(os.getenv(\"OPENAI_MAX_TOKENS\", \"4096\"))\n    temperature: float = float(os.getenv(\"OPENAI_TEMPERATURE\", \"0.7\"))\n\n\nclass MemoryConfig(BaseModel):\n    \"\"\"记忆系统配置\"\"\"\n    db_path: str = os.getenv(\"MEMORY_DB_PATH\", \"./data/memory.db\")\n    redis_host: str = os.getenv(\"REDIS_HOST\", \"localhost\")\n    redis_port: int = int(os.getenv(\"REDIS_PORT\", \"6379\"))\n    max_memory_items: int = int(os.getenv(\"MAX_MEMORY_ITEMS\", \"10000\"))\n\n\nclass SystemConfig(BaseModel):\n    \"\"\"系统配置\"\"\"\n    debug: bool = os.getenv(\"DEBUG\", \"true\").lower() == \"true\"\n    log_level: str = os.getenv(\"LOG_LEVEL\", \"INFO\")\n\n\nclass Config:\n    \"\"\"配置管理单例\"\"\"\n    \n    def __init__(self):\n        self.openai = OpenAIConfig()\n        self.memory = MemoryConfig()\n        self.system = SystemConfig()\n    \n    def validate(self) -> bool:\n        \"\"\"验证配置有效性\"\"\"\n        if not self.openai.api_key:\n            raise ValueError(\"OpenAI API key未配置，请在.env文件中设置OPENAI_API_KEY\")\n        return True\n\n\n# 全局配置实例\nconfig = Config()\n"
        },
        {
            "filename": "core/__init__.py",
            "content": "\"\"\"\n核心模块 - AGI系统核心组件\n\"\"\"\nfrom .agi_engine import AGIEngine\nfrom .message import Message, MessageRole\n\n__all__ = ['AGIEngine', 'Message', 'MessageRole']\n"
        },
        {
            "filename": "core/message.py",
            "content": "\"\"\"\n消息模块 - 定义对话消息结构\n\"\"\"\nfrom enum import Enum\nfrom dataclasses import dataclass, field\nfrom typing import Optional, List, Dict, Any\nfrom datetime import datetime\nimport uuid\n\n\nclass MessageRole(str, Enum):\n    \"\"\"消息角色枚举\"\"\"\n    SYSTEM = \"system\"\n    USER = \"user\"\n    ASSISTANT = \"assistant\"\n    TOOL = \"tool\"\n\n\n@dataclass\nclass Message:\n    \"\"\"对话消息数据类\"\"\"\n    role: MessageRole\n    content: str\n    message_id: str = field(default_factory=lambda: str(uuid.uuid4()))\n    timestamp: datetime = field(default_factory=datetime.now)\n    metadata: Dict[str, Any] = field(default_factory=dict)\n    tool_calls: Optional[List[Dict]] = None\n    tool_call_id: Optional[str] = None\n    \n    def to_dict(self) -> Dict[str, Any]:\n        \"\"\"转换为字典格式\"\"\"\n        return {\n            \"role\": self.role.value,\n            \"content\": self.content,\n            \"message_id\": self.message_id,\n            \"timestamp\": self.timestamp.isoformat(),\n            \"metadata\": self.metadata\n        }\n    \n    @classmethod\n    def from_dict(cls, data: Dict[str, Any]) -> 'Message':\n        \"\"\"从字典创建消息\"\"\"\n        return cls(\n            role=MessageRole(data[\"role\"]),\n            content=data[\"content\"],\n            message_id=data.get(\"message_id\", str(uuid.uuid4())),\n            timestamp=datetime.fromisoformat(data[\"timestamp\"]) if \"timestamp\" in data else datetime.now(),\n            metadata=data.get(\"metadata\", {})\n        )\n\n\n@dataclass  \nclass ConversationContext:\n    \"\"\"对话上下文管理\"\"\"\n    conversation_id: str = field(default_factory=lambda: str(uuid.uuid4()))\n    messages: List[Message] = field(default_factory=list)\n    max_messages: int = 50\n    \n    def add_message(self, message: Message):\n        \"\"\"添加消息到上下文\"\"\"\n        self.messages.append(message)\n        # 保持消息数量在限制内\n        if len(self.messages) > self.max_messages:\n            # 保留系统消息和最近的对话\n            system_messages = [m for m in self.messages if m.role == MessageRole.SYSTEM]\n            recent_messages = self.messages[-self.max_messages + len(system_messages):]\n            self.messages = system_messages + recent_messages\n    \n    def get_messages_for_api(self) -> List[Dict[str, str]]:\n        \"\"\"获取适合API调用的消息格式\"\"\"\n        return [{\"role\": m.role.value, \"content\": m.content} for m in self.messages]\n    \n    def clear(self):\n        \"\"\"清空上下文\"\"\"\n        system_messages = [m for m in self.messages if m.role == MessageRole.SYSTEM]\n        self.messages = system_messages\n"
        },
        {
            "filename": "core/agi_engine.py",
            "content": "\"\"\"\nAGI核心引擎 - 实现通用人工智能的核心逻辑\n\n该模块实现了：\n1. 与OpenAI API的集成\n2. 工具调用机制\n3. 任务规划和执行\n4. 记忆管理和学习\n5. 反思和自我改进能力\n\"\"\"\nimport json\nimport asyncio\nfrom typing import Dict, Any, List, Optional, Callable\nfrom loguru import logger\nfrom openai import OpenAI\nfrom openai.types.chat import ChatCompletionMessageToolCall\n\nfrom config import config\nfrom .message import Message, MessageRole, ConversationContext\nfrom memory.memory_system import MemorySystem\nfrom planner.task_planner import TaskPlanner\nfrom tools.tool_manager import ToolManager\n\n\nclass AGIEngine:\n    \"\"\"\n    AGI核心引擎类\n    \n    这是整个AGI系统的核心，负责协调各个子系统：\n    - 记忆系统：存储和检索长期/短期记忆\n    - 工具管理器：管理和执行各种工具\n    - 任务规划器：规划和执行复杂任务\n    - LLM集成：与OpenAI API交互\n    \"\"\"\n    \n    def __init__(self):\n        \"\"\"初始化AGI引擎\"\"\"\