# agi

<think>用户要求我作为中级工程师为项目"agi"生成代码。项目目标是实现一个真正意义上的AGI（通用人工智能），使用OpenAI API。

我需要生成可运行的、遵循最佳实践的代码，包含必要的注释和文档。由于我是中级工程师，代码应该是实现代码，而不是架构设计。

让我规划一下这个项目的结构：

1. **核心架构**：
   - 主控制器（Orchestrator）
   - 任务规划器（Task Planner）
   - 记忆系统（Memory System）
   - 工具调用系统（Tool System）
   - 推理引擎（Reasoning Engine）

2. **主要文件**：
   - `main.py` - 主入口
   - `orchestrator.py` - 核心编排器
   - `memory.py` - 记忆管理系统
   - `tools.py` - 工具调用系统
   - `planner.py` - 任务规划器
   - `reasoning.py` - 推理引擎
   - `config.py` - 配置文件
   - `utils.py` - 工具函数

让我开始编写代码：

首先，我需要创建一个完整的AGI系统框架。这应该是一个模块化、可扩展的系统。

让我按照JSON格式返回这些文件。
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "\"\"\"\nAGI项目配置模块\n包含所有系统配置参数和常量定义\n\n作者: AGI Team\n版本: 1.0.0\n\"\"\"\n\nimport os\nfrom typing import Dict, List, Optional\nfrom dataclasses import dataclass, field\nfrom enum import Enum\n\n\nclass ModelType(Enum):\n    \"\"\"支持的模型类型\"\"\"\n    GPT4 = \"gpt-4\"\n    GPT4_TURBO = \"gpt-4-turbo\"\n    GPT35 = \"gpt-3.5-turbo\"\n\n\nclass TaskType(Enum):\n    \"\"\"任务类型枚举\"\"\"\n    REASONING = \"reasoning\"\n    CREATIVE = \"creative\"\n    ANALYSIS = \"analysis\"\n    EXECUTION = \"execution\"\n    LEARNING = \"learning\"\n    PLANNING = \"planning\"\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API配置\"\"\"\n    api_key: str = field(default_factory=lambda: os.getenv(\"OPENAI_API_KEY\", \"\"))\n    model: str = \"gpt-4-turbo\"\n    max_tokens: int = 8192\n    temperature: float = 0.7\n    timeout: int = 60\n    retry_times: int = 3\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"记忆系统配置\"\"\"\n    max_short_term_items: int = 100\n    max_long_term_items: int = 10000\n    embedding_model: str = \"text-embedding-3-small\"\n    similarity_threshold: float = 0.7\n\n\n@dataclass\nclass ToolConfig:\n    \"\"\"工具系统配置\"\"\"\n    max_concurrent_tools: int = 5\n    timeout_per_tool: int = 30\n    allowed_tools: List[str] = field(default_factory=list)\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"AGI系统主配置\"\"\"\n    openai: OpenAIConfig = field(default_factory=OpenAIConfig)\n    memory: MemoryConfig = field(default_factory=MemoryConfig)\n    tool: ToolConfig = field(default_factory=ToolConfig)\n    \n    # 系统行为配置\n    enable_self_learning: bool = True\n    enable_memory_consolidation: bool = True\n    max_iteration_depth: int = 10\n    debug_mode: bool = False\n    \n    # 会话配置\n    session_id: Optional[str] = None\n    user_id: Optional[str] = None\n\n\ndef load_config(config_dict: Optional[Dict] = None) -> AGIConfig:\n    \"\"\"\n    从字典加载配置\n    \n    Args:\n        config_dict: 配置字典，如果为None则使用默认配置\n        \n    Returns:\n        AGIConfig: 配置对象\n    \"\"\"\n    if config_dict is None:\n        return AGIConfig()\n    \n    config = AGIConfig()\n    \n    # 解析OpenAI配置\n    if \"openai\" in config_dict:\n        openai_dict = config_dict[\"openai\"]\n        config.openai = OpenAIConfig(\n            api_key=openai_dict.get(\"api_key\", config.openai.api_key),\n            model=openai_dict.get(\"model\", config.openai.model),\n            max_tokens=openai_dict.get(\"max_tokens\", config.openai.max_tokens),\n            temperature=openai_dict.get(\"temperature\", config.openai.temperature),\n            timeout=openai_dict.get(\"timeout\", config.openai.timeout),\n            retry_times=openai_dict.get(\"retry_times\", config.openai.retry_times)\n        )\n    \n    # 解析记忆配置\n    if \"memory\" in config_dict:\n        memory_dict = config_dict[\"memory\"]\n        config.memory = MemoryConfig(\n            max_short_term_items=memory_dict.get(\"max_short_term_items\", config.memory.max_short_term_items),\n            max_long_term_items=memory_dict.get(\"max_long_term_items\", config.memory.max_long_term_items),\n            embedding_model=memory_dict.get(\"embedding_model\", config.memory.embedding_model),\n            similarity_threshold=memory_dict.get(\"similarity_threshold\", config.memory.similarity_threshold)\n        )\n    \n    # 解析工具配置\n    if \"tool\" in config_dict:\n        tool_dict = config_dict[\"tool\"]\n        config.tool = ToolConfig(\n            max_concurrent_tools=tool_dict.get(\"max_concurrent_tools\", config.tool.max_concurrent_tools),\n            timeout_per_tool=tool_dict.get(\"timeout_per_tool\", config.tool.timeout_per_tool),\n            allowed_tools=tool_dict.get(\"allowed_tools\", config.tool.allowed_tools)\n        )\n    \n    # 解析系统行为配置\n    config.enable_self_learning = config_dict.get(\"enable_self_learning\", config.enable_self_learning)\n    config.enable_memory_consolidation = config_dict.get(\"enable_memory_consolidation\", config.enable_memory_consolidation)\n    config.max_iteration_depth = config_dict.get(\"max_iteration_depth\", config.max_iteration_depth)\n    config.debug_mode = config_dict.get(\"debug_mode\", config.debug_mode)\n    \n    return config\n"
        },
        {
            "filename": "memory.py",
            "content": "\"\"\"\nAGI记忆管理系统\n负责短期记忆、长期记忆的管理和检索\n\n作者: AGI Team\n版本: 1.0.0\n\"\"\"\n\nimport os\nimport json\nimport time\nimport hashlib\nfrom typing import Dict, List, Optional, Any, Tuple\nfrom dataclasses import dataclass, field\nfrom datetime import datetime\nfrom collections import OrderedDict\nimport numpy as np\n\n# 尝试导入openai嵌入，如果不可用则使用简单哈希\ntry:\n    from openai import OpenAI\n    OPENAI_AVAILABLE = True\nexcept ImportError:\n    OPENAI_AVAILABLE = False\n\n\n@dataclass\nclass MemoryItem:\n    \"\"\"记忆项数据结构\"\"\"\n    content: str\n    memory_type: str  # 'short_term', 'long_term', 'working'\n    importance: float = 0.5  # 重要性评分 0-1\n    created_at: float = field(default_factory=time.time)\n    last_accessed: float = field(default_factory=time.time)\n    access_count: int = 0\n    metadata: Dict = field(default_factory=dict)\n    embedding: Optional[List[float]] = None\n    tags: List[str] = field(default_factory=list)\n\n\nclass EmbeddingManager:\n    \"\"\"嵌入向量管理器\"\"\"\n    \n    def __init__(self, api_key: str, model: str = \"text-embedding-3-small\"):\n        self.api_key = api_key\n        self.model = model\n        self.client = None\n        if OPENAI_AVAILABLE and api_key:\n            self.client = OpenAI(api_key=api_key)\n    \n    def get_embedding(self, text: str) -> List[float]:\n        \"\"\"\n        获取文本的嵌入向量\n        \n        Args:\n            text: 输入文本\n            \n        Returns:\n            嵌入向量列表\n        \"\"\"\n        if self.client:\n            try:\n                response = self.client.embeddings.create(\n                    model=self.model,\n                    input=text\n                )\n                return response.data[0].embedding\n            except Exception as e:\n                print(f\"嵌入生成失败: {e}\")\n        \n        # 回退到简单哈希（仅用于测试）\n        return self._simple_embedding(text)\n    \n    def _simple_embedding(self, text: str, dim: int = 384) -> List[float]:\n        \"\"\"\n        简单嵌入方法（基于哈希）\n        用于没有API访问时的回退方案