# agi

<think>用户要求我作为一个初级工程师，为项目"agi"生成代码。项目描述是实现一个真正意义上的AGI，使用OpenAI API。

根据要求，我需要：
1. 生成实际的代码
2. 代码应该是可运行的，遵循最佳实践
3. 包含必要的注释和文档
4. 作为初级工程师，生成实现代码而非架构设计
5. 用JSON格式返回

由于这是一个AGI项目，我需要设计一个能够实现通用人工智能的系统框架。作为初级工程师，我应该生成实际的实现代码，而不是过于复杂的架构设计。

我会创建一个基于OpenAI API的AGI系统，包含以下组件：
1. 主程序入口
2. 核心AGI引擎
3. 提示词管理器
4. 工具调用系统
5. 记忆系统
6. 配置文件

让我开始编写代码。
</think>

```json
{
    "files": [
        {
            "filename": "config.yaml",
            "content": "# AGI项目配置文件\n# 作者：初级工程师\n# 描述：AGI系统的配置参数\n\n# OpenAI API配置\nopenai:\n  api_key: \"your-api-key-here\"\n  base_url: \"https://api.openai.com/v1\"\n  model: \"gpt-4-turbo-preview\"\n  temperature: 0.7\n  max_tokens: 4096\n  timeout: 30\n\n# 系统配置\nsystem:\n  name: \"AGI Assistant\"\n  version: \"1.0.0\"\n  debug: true\n  log_level: \"INFO\"\n\n# 记忆系统配置\nmemory:\n  max_history: 100\n  summary_interval: 10\n  storage_type: \"sqlite\"\n  database_path: \"./data/memory.db\"\n\n# 工具系统配置\ntools:\n  enabled: true\n  max_tools_per_request: 5\n  timeout: 10\n\n# 会话配置\nsession:\n  max_concurrent: 10\n  timeout: 3600\n  auto_save: true\n"
        },
        {
            "filename": "requirements.txt",
            "content": "# AGI项目依赖\n# 作者：初级工程师\n# 描述：项目所需的Python依赖包\n\nopenai>=1.0.0\npyyaml>=6.0\nsqlite3\njson\ndatetime\ntyping\nasyncio\nlogging\nhashlib\n"
        },
        {
            "filename": "agi_core/__init__.py",
            "content": "\"\"\"\nAGI核心模块\n作者：初级工程师\n描述：AGI系统的核心功能模块\n\"\"\"\n\nfrom .engine import AGIEngine\nfrom .memory import MemorySystem\nfrom .tool_manager import ToolManager\nfrom .prompt_manager import PromptManager\nfrom .config import Config\n\n__version__ = \"1.0.0\"\n__all__ = ['AGIEngine', 'MemorySystem', 'ToolManager', 'PromptManager', 'Config']\n"
        },
        {
            "filename": "agi_core/config.py",
            "content": "\"\"\"\n配置管理模块\n作者：初级工程师\n描述：负责加载和管理系统配置\n\"\"\"\n\nimport yaml\nimport os\nfrom typing import Any, Dict, Optional\nimport logging\n\nlogger = logging.getLogger(__name__)\n\n\nclass Config:\n    \"\"\"配置管理类，负责加载和管理系统配置\"\"\"\n    \n    def __init__(self, config_path: str = \"config.yaml\"):\n        \"\"\"\n        初始化配置管理器\n        \n        Args:\n            config_path: 配置文件路径\n        \"\"\"\n        self.config_path = config_path\n        self.config: Dict[str, Any] = {}\n        self._load_config()\n    \n    def _load_config(self) -> None:\n        \"\"\"加载配置文件\"\"\"\n        try:\n            if os.path.exists(self.config_path):\n                with open(self.config_path, 'r', encoding='utf-8') as f:\n                    self.config = yaml.safe_load(f) or {}\n                logger.info(f\"配置加载成功: {self.config_path}\")\n            else:\n                logger.warning(f\"配置文件不存在，使用默认配置: {self.config_path}\")\n                self._set_defaults()\n        except Exception as e:\n            logger.error(f\"加载配置失败: {e}\")\n            self._set_defaults()\n    \n    def _set_defaults(self) -> None:\n        \"\"\"设置默认配置\"\"\"\n        self.config = {\n            \"openai\": {\n                \"api_key\": \"\",\n                \"base_url\": \"https://api.openai.com/v1\",\n                \"model\": \"gpt-4-turbo-preview\",\n                \"temperature\": 0.7,\n                \"max_tokens\": 4096,\n                \"timeout\": 30\n            },\n            \"system\": {\n                \"name\": \"AGI Assistant\",\n                \"version\": \"1.0.0\",\n                \"debug\": True,\n                \"log_level\": \"INFO\"\n            },\n            \"memory\": {\n                \"max_history\": 100,\n                \"summary_interval\": 10,\n                \"storage_type\": \"sqlite\",\n                \"database_path\": \"./data/memory.db\"\n            },\n            \"tools\": {\n                \"enabled\": True,\n                \"max_tools_per_request\": 5,\n                \"timeout\": 10\n            },\n            \"session\": {\n                \"max_concurrent\": 10,\n                \"timeout\": 3600,\n                \"auto_save\": True\n            }\n        }\n    \n    def get(self, key: str, default: Any = None) -> Any:\n        \"\"\"\n        获取配置值\n        \n        Args:\n            key: 配置键，支持点号分隔的嵌套键\n            default: 默认值\n            \n        Returns:\n            配置值\n        \"\"\"\n        keys = key.split('.')\n        value = self.config\n        \n        for k in keys:\n            if isinstance(value, dict) and k in value:\n                value = value[k]\n            else:\n                return default\n        \n        return value\n    \n    def set(self, key: str, value: Any) -> None:\n        \"\"\"\n        设置配置值\n        \n        Args:\n            key: 配置键，支持点号分隔的嵌套键\n            value: 配置值\n        \"\"\"\n        keys = key.split('.')\n        config = self.config\n        \n        for k in keys[:-1]:\n            if k not in config:\n                config[k] = {}\n            config = config[k]\n        \n        config[keys[-1]] = value\n    \n    def reload(self) -> None:\n        \"\"\"重新加载配置\"\"\"\n        self._load_config()\n    \n    def save(self, path: Optional[str] = None) -> None:\n        \"\"\"\n        保存配置到文件\n        \n        Args:\n            path: 保存路径，默认为配置文件路径\n        \"\"\"\n        save_path = path or self.config_path\n        try:\n            with open(save_path, 'w', encoding='utf-8') as f:\n                yaml.dump(self.config, f, allow_unicode=True)\n            logger.info(f\"配置保存成功: {save_path}\")\n        except Exception as e:\n            logger.error(f\"保存配置失败: {e}\")\n"
        },
        {
            "filename": "agi_core/memory.py",
            "content": "\"\"\"\n记忆系统模块\n作者：初级工程师\n描述：负责管理AGI的长期和短期记忆\n\"\"\"\n\nimport json\nimport os\nimport sqlite3\nfrom datetime import datetime\nfrom typing import List, Dict, Any, Optional\nfrom collections import deque\nimport logging\n\nlogger = logging.getLogger(__name__)\n\n\nclass MemorySystem:\n    \"\"\"记忆系统类，负责管理短期和长期记忆\"\"\"\n    \n    def __init__(self, config: 'Config'):\n        \"\"\"\n        初始化记忆系统\n        \n        Args:\n            config: 配置对象\n        \"\"\"\n        self.config = config\n        self.max_history = config.get('memory.max_history', 100)\n        self.summary_interval = config.get('memory.summary_interval', 10)\n        self.database_path = config.get('memory.database_path', './data/memory.db')\n        \n        # 短期记忆：使用队列存储最近的对话\n        self.short_term_memory: deque = deque(maxlen=self.max_history)\n        \n        # 初始化长期记忆数据库\n        self._init_database()\n    \n    def _init_database(self) -> None:\n        \"\"\"初始化长期记忆数据库\"\"\"\n        try:\n            # 确保数据库目录存在\n            db_dir = os.path.dirname(self.database_path)\n            if db_dir and not os.path.exists(db_dir):\n                os.makedirs(db_dir)\n            \n            conn = sqlite3.connect(self.database_path)\n            cursor = conn.cursor()\n            \n            # 创建记忆表\n            cursor.execute('''