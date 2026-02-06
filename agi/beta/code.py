# agi

<think>用户要求我作为中级工程师为项目"agi"生成代码。项目描述是实现一个真正意义上的AGI，使用OpenAI API。

我需要生成实际可运行的代码，包含必要的注释和文档。作为中级工程师，我应该生成实现代码，而不是架构设计。

让我思考一下AGI系统需要哪些核心组件：

1. 主控制器 - 协调各个模块
2. 提示词管理器 - 构建和管理系统提示
3. 记忆系统 - 短期和长期记忆
4. 工具使用系统 - 能够调用外部工具
5. 学习系统 - 能够从经验中学习
6. 规划系统 - 能够制定和执行计划
7. 会话管理 - 管理多个对话

我会创建一个模块化的AGI系统，包含以下文件：
1. main.py - 主入口
2. config.py - 配置文件
3. core/controller.py - 核心控制器
4. memory/memory_system.py - 记忆系统
5. tools/tool_manager.py - 工具管理系统
6. prompt/prompt_builder.py - 提示词构建器
7. learning/learning_system.py - 学习系统
8. utils/logger.py - 日志工具

让我开始生成这些代码文件。
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\nAGI项目配置文件\n\"\"\"\n\nimport os\nfrom pathlib import Path\n\nclass Config:\n    \"\"\"AGI系统配置类\"\"\"\n    \n    # OpenAI API配置\n    OPENAI_API_KEY = os.getenv(\"OPENAI_API_KEY\", \"\")\n    OPENAI_MODEL = os.getenv(\"OPENAI_MODEL\", \"gpt-4-turbo-preview\")\n    OPENAI_BASE_URL = os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\")\n    \n    # API参数配置\n    API_TEMPERATURE = float(os.getenv(\"API_TEMPERATURE\", \"0.7\"))\n    API_MAX_TOKENS = int(os.getenv(\"API_MAX_TOKENS\", \"8192\"))\n    API_TOP_P = float(os.getenv(\"API_TOP_P\", \"1.0\"))\n    API_FREQUENCY_PENALTY = float(os.getenv(\"API_FREQUENCY_PENALTY\", \"0.0\"))\n    API_PRESENCE_PENALTY = float(os.getenv(\"API_PRESENCE_PENALTY\", \"0.0\"))\n    \n    # 系统配置\n    SYSTEM_NAME = \"AGI-Core\"\n    SYSTEM_VERSION = \"1.0.0\"\n    DEBUG_MODE = os.getenv(\"DEBUG_MODE\", \"False\").lower() == \"true\"\n    \n    # 记忆配置\n    MEMORY_MAX_SHORT_TERM = int(os.getenv(\"MEMORY_MAX_SHORT_TERM\", \"50\"))\n    MEMORY_MAX_LONG_TERM = int(os.getenv(\"MEMORY_MAX_LONG_TERM\", \"1000\"))\n    MEMORY_VECTOR_DIM = int(os.getenv(\"MEMORY_VECTOR_DIM\", \"1536\"))\n    \n    # 工具配置\n    TOOLS_DIR = Path(__file__).parent / \"tools\"\n    MAX_TOOL_CALLS_PER_TURN = int(os.getenv(\"MAX_TOOL_CALLS_PER_TURN\", \"10\"))\n    \n    # 日志配置\n    LOG_LEVEL = os.getenv(\"LOG_LEVEL\", \"INFO\")\n    LOG_DIR = Path(__file__).parent / \"logs\"\n    \n    @classmethod\n    def validate(cls) -> bool:\n        \"\"\"验证配置是否有效\"\"\"\n        if not cls.OPENAI_API_KEY:\n            raise ValueError(\"OpenAI API密钥未设置，请设置环境变量OPENAI_API_KEY\")\n        return True\n    \n    @classmethod\n    def get_api_params(cls) -> dict:\n        \"\"\"获取API调用参数\"\"\"\n        return {\n            \"temperature\": cls.API_TEMPERATURE,\n            \"max_tokens\": cls.API_MAX_TOKENS,\n            \"top_p\": cls.API_TOP_P,\n            \"frequency_penalty\": cls.API_FREQUENCY_PENALTY,\n            \"presence_penalty\": cls.API_PRESENCE_PENALTY\n        }\n\n# 创建全局配置实例\nconfig = Config()\n"
        },
        {
            "filename": "utils/logger.py",
            "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\n日志工具模块\n\"\"\"\n\nimport logging\nimport sys\nfrom datetime import datetime\nfrom pathlib import Path\nfrom typing import Optional\n\nclass LoggerManager:\n    \"\"\"日志管理器\"\"\"\n    \n    _instance: Optional['LoggerManager'] = None\n    _loggers: dict = {}\n    \n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance\n    \n    def __init__(self):\n        if not hasattr(self, '_initialized'):\n            self._initialized = True\n            self._setup_default_logger()\n    \n    def _setup_default_logger(self):\n        \"\"\"设置默认日志器\"\"\"\n        self.get_logger(\"AGI\")\n    \n    def get_logger(self, name: str) -> logging.Logger:\n        \"\"\"获取日志器实例\"\"\"\n        if name in self._loggers:\n            return self._loggers[name]\n        \n        logger = logging.getLogger(name)\n        logger.setLevel(logging.DEBUG)\n        \n        # 创建控制台处理器\n        console_handler = logging.StreamHandler(sys.stdout)\n        console_handler.setLevel(logging.INFO)\n        \n        # 创建格式化器\n        formatter = logging.Formatter(\n            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n            datefmt='%Y-%m-%d %H:%M:%S'\n        )\n        console_handler.setFormatter(formatter)\n        \n        # 添加处理器\n        if not logger.handlers:\n            logger.addHandler(console_handler)\n        \n        self._loggers[name] = logger\n        return logger\n    \n    def set_log_file(self, name: str, log_path: Path):\n        \"\"\"设置日志文件\"\"\"\n        logger = self.get_logger(name)\n        \n        # 确保日志目录存在\n        log_path.parent.mkdir(parents=True, exist_ok=True)\n        \n        file_handler = logging.FileHandler(log_path, encoding='utf-8')\n        file_handler.setLevel(logging.DEBUG)\n        file_handler.setFormatter(logging.Formatter(\n            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',\n            datefmt='%Y-%m-%d %H:%M:%S'\n        ))\n        \n        logger.addHandler(file_handler)\n\n# 全局日志管理器实例\nlogger_manager = LoggerManager()\n\ndef get_logger(name: str) -> logging.Logger:\n    \"\"\"获取日志器的便捷函数\"\"\"\n    return logger_manager.get_logger(name)\n"
        },
        {
            "filename": "memory/memory_system.py",
            "content": "#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n\"\"\"\n记忆系统模块\n提供短期记忆和长期记忆管理功能\n\"\"\"\n\nfrom abc import ABC, abstractmethod\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\nfrom typing import List, Optional, Dict, Any\nfrom collections import deque\nimport json\nimport hashlib\nimport re\n\nfrom utils.logger import get_logger\n\nlogger = get_logger(\"MemorySystem\")\n\n@dataclass\nclass MemoryItem:\n    \"\"\"记忆项数据类\"\"\"\n    content: str\n    memory_type: str  # 'short_term', 'long_term', 'working'\n    importance: float = 0.5  # 重要性评分 0-1\n    timestamp: datetime = field(default_factory=datetime.now)\n    metadata: Dict[str, Any] = field(default_factory=dict)\n    embedding: Optional[List[float]] = None\n    access_count: int = 0\n    last_accessed: datetime = field(default_factory=datetime.now)\n    \n    def to_dict(self) -> Dict[str, Any]:\n        \"\"\"转换为字典\"\"\"\n        return {\n            'content': self.content,\n            'memory_type': self.memory_type,\n            'importance': self.importance,\n            'timestamp': self.timestamp.isoformat(),\n            'metadata': self.metadata,\n            'access_count': self.access_count,\n            'last_accessed': self.last_accessed.isoformat()\n        }\n    \n    @classmethod\n    def from_dict(cls, data: Dict[str, Any]) -> 'MemoryItem':\n        \"\"\"从字典创建实例\"\"\"\n        return cls(\n            content=data['content'],\n            memory_type=data['memory_type'],\n            importance=data['import