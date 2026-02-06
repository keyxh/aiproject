# agi

<think>用户要求我作为中级工程师为项目"agi"生成代码，项目目标是实现一个真正意义上的AGI（通用人工智能），使用OpenAI API。

我需要：
1. 生成实际可运行的代码
2. 遵循最佳实践
3. 包含必要的注释和文档
4. 以JSON格式返回

作为中级工程师，我应该生成实现代码，而不是架构设计。我需要创建一个基本的AGI框架代码结构。

考虑到AGI的复杂性，我会创建一个模块化的框架，包括：
1. 主程序入口
2. 核心AGI引擎
3. 工具调用系统
4. 记忆系统
5. 任务规划系统
6. 对话系统
7. OpenAI API集成

让我开始编写代码。
</think>

```json
{
    "files": [
        {
            "filename": "agi/__init__.py",
            "content": "\"\"\"\nAGI (Artificial General Intelligence) 项目主包\n\n实现一个真正意义上的通用人工智能系统，\n具备理解、学习、推理和自主行动的能力。\n\"\"\"\n\n__version__ = \"1.0.0\"\n__author__ = \"AGI Development Team\"\n\nfrom .core.engine import AGIEngine\nfrom .core.config import AGIConfig\nfrom .tools.tool_manager import ToolManager\nfrom .memory.memory_system import MemorySystem\nfrom .planning.task_planner import TaskPlanner\nfrom .dialogue.conversation import ConversationManager\n\n__all__ = [\n    'AGIEngine',\n    'AGIConfig', \n    'ToolManager',\n    'MemorySystem',\n    'TaskPlanner',\n    'ConversationManager'\n]\n"
        },
        {
            "filename": "agi/core/config.py",
            "content": "\"\"\"\nAGI 配置模块\n\n管理系统的所有配置参数，包括API密钥、模型设置、系统参数等。\n\"\"\"\n\nimport os\nfrom dataclasses import dataclass, field\nfrom typing import Optional\nimport json\n\n\n@dataclass\nclass ModelConfig:\n    \"\"\"模型配置\"\"\"\n    model: str = \"gpt-4-turbo-preview\"\n    temperature: float = 0.7\n    max_tokens: int = 4096\n    top_p: float = 1.0\n    frequency_penalty: float = 0.0\n    presence_penalty: float = 0.0\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"记忆系统配置\"\"\"\n    max_short_term_memory: int = 100\n    max_long_term_memory: int = 10000\n    memory_persistence_path: str = \"./data/memory\"\n    embedding_model: str = \"text-embedding-3-small\"\n\n\n@dataclass\nclass ToolConfig:\n    \"\"\"工具系统配置\"\"\"\n    max_concurrent_tools: int = 10\n    tool_timeout_seconds: int = 30\n    allowed_tools: list = field(default_factory=list)\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"\n    AGI系统主配置类\n    \n    Attributes:\n        openai_api_key: OpenAI API密钥\n        model_config: 模型相关配置\n        memory_config: 记忆系统配置\n        tool_config: 工具系统配置\n        system_prompt: 系统提示词\n        debug_mode: 调试模式开关\n        log_level: 日志级别\n    \"\"\"\n    \n    openai_api_key: Optional[str] = None\n    model_config: ModelConfig = field(default_factory=ModelConfig)\n    memory_config: MemoryConfig = field(default_factory=MemoryConfig)\n    tool_config: ToolConfig = field(default_factory=ToolConfig)\n    \n    system_prompt: str = \"\"\"你是一个通用人工智能助手，具备强大的推理、学习和理解能力。\n    你能够理解复杂的概念，解决难题，并从经验中学习。\n    你的目标是通过提供准确、有帮助的回答来协助用户。\"\"\"\n    \n    debug_mode: bool = False\n    log_level: str = \"INFO\"\n    \n    def __post_init__(self):\n        \"\"\"初始化后处理，从环境变量加载API密钥\"\"\"\n        if self.openai_api_key is None:\n            self.openai_api_key = os.getenv(\"OPENAI_API_KEY\")\n            \n        if self.openai_api_key is None:\n            raise ValueError(\"OpenAI API密钥未设置，请通过环境变量OPENAI_API_KEY或配置参数提供\")\n    \n    @classmethod\n    def from_file(cls, config_path: str) -> \"AGIConfig\":\n        \"\"\"\n        从JSON文件加载配置\n        \n        Args:\n            config_path: 配置文件路径\n            \n        Returns:\n            AGIConfig实例\n        \"\"\"\n        with open(config_path, 'r', encoding='utf-8') as f:\n            config_data = json.load(f)\n            \n        # 构建嵌套配置\n        model_config = ModelConfig(**config_data.get('model', {}))\n        memory_config = MemoryConfig(**config_data.get('memory', {}))\n        tool_config = ToolConfig(**config_data.get('tool', {}))\n        \n        return cls(\n            openai_api_key=config_data.get('openai_api_key'),\n            model_config=model_config,\n            memory_config=memory_config,\n            tool_config=tool_config,\n            system_prompt=config_data.get('system_prompt', cls().system_prompt),\n            debug_mode=config_data.get('debug_mode', False),\n            log_level=config_data.get('log_level', 'INFO')\n        )\n    \n    def to_file(self, config_path: str):\n        \"\"\"\n        将配置保存到JSON文件\n        \n        Args:\n            config_path: 配置文件路径\n        \"\"\"\n        config_data = {\n            'model': {\n                'model': self.model_config.model,\n                'temperature': self.model_config.temperature,\n                'max_tokens': self.model_config.max_tokens,\n                'top_p': self.model_config.top_p,\n                'frequency_penalty': self.model_config.frequency_penalty,\n                'presence_penalty': self.model_config.presence_penalty\n            },\n            'memory': {\n                'max_short_term_memory': self.memory_config.max_short_term_memory,\n                'max_long_term_memory': self.memory_config.max_long_term_memory,\n                'memory_persistence_path': self.memory_config.memory_persistence_path,\n                'embedding_model': self.memory_config.embedding_model\n            },\n            'tool': {\n                'max_concurrent_tools': self.tool_config.max_concurrent_tools,\n                'tool_timeout_seconds': self.tool_config.tool_timeout_seconds,\n                'allowed_tools': self.tool_config.allowed_tools\n            },\n            'system_prompt': self.system_prompt,\n            'debug_mode': self.debug_mode,\n            'log_level': self.log_level\n        }\n        \n        with open(config_path, 'w', encoding='utf-8') as f:\n            json.dump(config_data, f, indent=4, ensure_ascii=False)\n"
        },
        {
            "filename": "agi/core/engine.py",
            "content": "\"\"\"\nAGI 核心引擎\n\n系统的核心处理单元，协调各个子系统的工作，\n实现通用人工智能的主要功能。\n\"\"\"\n\nimport logging\nfrom typing import Dict, List, Any, Optional\nfrom datetime import datetime\nimport uuid\n\nfrom .config import AGIConfig\nfrom ..tools.tool_manager import ToolManager\nfrom ..memory.memory_system import MemorySystem\nfrom ..planning.task_planner import TaskPlanner\nfrom ..dialogue.conversation import ConversationManager\nfrom ..utils.openai_client import OpenAIClient\n\n\nclass AGIEngine:\n    \"\"\"\n    AGI核心引擎类\n    \n    这是整个AGI系统的主控制器，负责协调：\n    - 对话管理\n    - 任务规划\n    - 记忆存储和检索\n    - 工具调用\n    - 推理和决策\n    \n    Attributes:\n        config: 系统配置\n        openai_client: OpenAI API客户端\n        memory_system: 记忆系统\n        tool_manager: 工具管理器\n        task_planner: 任务规划器\n        conversation_manager: 对话管理器\n        session_id: 当前会话ID\n    \"\"\"\n    \n    def __init__(self, config: AGIConfig):\n        \"\"\"\n        初始化AGI引擎\n        \n        Args:\n            config: AGI配置对象\n        \"\"\"\n        self.config = config\n        self.session_id = str(uuid.uuid4())\n        \n        # 初始化日志\n        self._setup_logging()\n        \n        # 初始化各个子系统\n        self.logger.info(\"正在初始化AGI核心引擎...\")\n        \n        # 初始化OpenAI客户端\n        self.openai_client = OpenAIClient(\n            api_key=config.openai_api_key,\n            model=config.model_config.model,\n            temperature=config.model_config.temperature,\n            max_tokens=config.model_config.max_tokens\n        )\n        \n        # 初始化记忆系统\n        self.memory_system = MemorySystem(config.memory_config)\n        \n        # 初始化工具管理器\n