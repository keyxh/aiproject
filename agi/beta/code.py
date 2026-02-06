# agi

<think>用户要求我作为一个初级工程师，为项目"agi"生成代码。项目描述是实现一个真正意义上的AGI，使用OpenAI API。

我需要：
1. 生成实际的、可运行的代码
2. 遵循最佳实践
3. 包含必要的注释和文档
4. 作为初级工程师，代码应该是实现层面的代码，而不是架构设计

由于是初级工程师，我应该生成一些基础的实现代码，比如：
- API客户端封装
- 基本的AGI核心逻辑
- 简单的工具调用实现
- 基础的提示词管理

让我设计一个简单的AGI系统结构：
1. 配置管理
2. OpenAI API客户端
3. 基础的AGI引擎
4. 简单的工具系统
5. 对话管理

我会用Python实现，因为这是最常用的AI开发语言。

让我生成这些代码文件。
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "#!/usr/bin/env python3\n\"\"\"\nAGI项目配置模块\n负责管理API密钥和其他配置信息\n\"\"\"\n\nimport os\nfrom pathlib import Path\nfrom dataclasses import dataclass\nfrom typing import Optional\n\n\n@dataclass\nclass Config:\n    \"\"\"项目配置类\"\"\"\n    \n    # OpenAI API配置\n    openai_api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model_name: str = \"gpt-4\"\n    max_tokens: int = 4000\n    temperature: float = 0.7\n    \n    # 系统配置\n    debug_mode: bool = os.getenv(\"DEBUG_MODE\", \"False\").lower() == \"true\"\n    log_level: str = \"INFO\"\n    \n    # 存储配置\n    data_dir: Path = Path(\"./data\")\n    \n    def __post_init__(self):\n        \"\"\"初始化后处理\"\"\"\n        # 确保数据目录存在\n        self.data_dir.mkdir(parents=True, exist_ok=True)\n    \n    def validate(self) -> bool:\n        \"\"\"\n        验证配置是否有效\n        \n        Returns:\n            bool: 配置是否有效\n        \"\"\"\n        if not self.openai_api_key:\n            raise ValueError(\"OPENAI_API_KEY环境变量未设置\")\n        return True\n\n\n# 全局配置实例\nconfig = Config()\n"
        },
        {
            "filename": "openai_client.py",
            "content": "#!/usr/bin/env python3\n\"\"\"\nOpenAI API客户端封装\n封装了与OpenAI API的交互逻辑\n\"\"\"\n\nimport logging\nfrom typing import List, Dict, Optional, Any\nfrom openai import OpenAI\nfrom config import config\n\n\nlogger = logging.getLogger(__name__)\n\n\nclass OpenAIClient:\n    \"\"\"\n    OpenAI API客户端类\n    负责处理与OpenAI API的所有通信\n    \"\"\"\n    \n    def __init__(self):\n        \"\"\"\n        初始化OpenAI客户端\n        \"\"\"\n        self.client = OpenAI(api_key=config.openai_api_key)\n        self.model_name = config.model_name\n        self.max_tokens = config.max_tokens\n        self.temperature = config.temperature\n    \n    def chat_completion(\n        self,\n        messages: List[Dict[str, str]],\n        system_prompt: Optional[str] = None,\n        temperature: Optional[float] = None,\n        max_tokens: Optional[int] = None\n    ) -> Dict[str, Any]:\n        \"\"\"\n        发送聊天请求到OpenAI API\n        \n        Args:\n            messages: 消息列表\n            system_prompt: 系统提示词\n            temperature: 温度参数\n            max_tokens: 最大token数\n        \n        Returns:\n            Dict: API响应\n        \"\"\"\n        try:\n            # 构建完整的消息列表\n            full_messages = []\n            if system_prompt:\n                full_messages.append({\n                    \"role\": \"system\",\n                    \"content\": system_prompt\n                })\n            full_messages.extend(messages)\n            \n            # 发送请求\n            response = self.client.chat.completions.create(\n                model=self.model_name,\n                messages=full_messages,\n                temperature=temperature or self.temperature,\n                max_tokens=max_tokens or self.max_tokens\n            )\n            \n            logger.info(f\"API调用成功，消耗tokens: {response.usage.total_tokens}\")\n            \n            return {\n                \"success\": True,\n                \"content\": response.choices[0].message.content,\n                \"usage\": {\n                    \"prompt_tokens\": response.usage.prompt_tokens,\n                    \"completion_tokens\": response.usage.completion_tokens,\n                    \"total_tokens\": response.usage.total_tokens\n                }\n            }\n            \n        except Exception as e:\n            logger.error(f\"API调用失败: {str(e)}\")\n            return {\n                \"success\": False,\n                \"error\": str(e)\n            }\n    \n    def get_embedding(self, text: str) -> Optional[List[float]]:\n        \"\"\"\n        获取文本的embedding向量\n        \n        Args:\n            text: 输入文本\n        \n        Returns:\n            List[float]: embedding向量\n        \"\"\"\n        try:\n            response = self.client.embeddings.create(\n                model=\"text-embedding-3-small\",\n                input=text\n            )\n            \n            return response.data[0].embedding\n            \n        except Exception as e:\n            logger.error(f\"Embedding获取失败: {str(e)}\")\n            return None\n\n\n# 全局客户端实例\nopenai_client = OpenAIClient()\n"
        },
        {
            "filename": "tools.py",
            "content": "#!/usr/bin/env python3\n\"\"\"\n工具系统模块\n定义和管理AGI可用的工具\n\"\"\"\n\nimport inspect\nfrom typing import Callable, Any, Dict, List\nfrom abc import ABC, abstractmethod\n\n\nclass Tool(ABC):\n    \"\"\"\n    工具基类\n    所有工具都需要继承这个类并实现execute方法\n    \"\"\"\n    \n    @property\n    @abstractmethod\n    def name(self) -> str:\n        \"\"\"工具名称\"\"\"\n        pass\n    \n    @property\n    @abstractmethod\n    def description(self) -> str:\n        \"\"\"工具描述\"\"\"\n        pass\n    \n    @abstractmethod\n    def execute(self, **kwargs) -> Any:\n        \"\"\"执行工具逻辑\"\"\"\n        pass\n    \n    def get_schema(self) -> Dict[str, Any]:\n        \"\"\"\n        获取工具的JSON Schema\n        用于告诉AI何时以及如何使用工具\n        \n        Returns:\n            Dict: 工具定义\n        \"\"\"\n        return {\n            \"type\": \"function\",\n            \"function\": {\n                \"name\": self.name,\n                \"description\": self.description,\n                \"parameters\": {\n                    \"type\": \"object\",\n                    \"properties\": self._get_parameters_schema(),\n                    \"required\": self._get_required_parameters()\n                }\n            }\n        }\n    \n    def _get_parameters_schema(self) -> Dict[str, Any]:\n        \"\"\"获取参数模式\"\"\"\n        sig = inspect.signature(self.execute)\n        properties = {}\n        \n        for name, param in sig.parameters.items():\n            if name == 'self':\n                continue\n                \n            properties[name] = {\n                \"type\": \"string\",\n                \"description\": param.default if param.default != inspect.Parameter.empty else f\"{name}参数\"\n            }\n        \n        return properties\n    \n    def _get_required_parameters(self) -> List[str]:\n        \"\"\"获取必需参数列表\"\"\"\n        sig = inspect.signature(self.execute)\n        required = []\n        \n        for name, param in sig.parameters.items():\n            if name == 'self':\n                continue\n            if param.default == inspect.Parameter.empty:\n                required.append(name)\n        \n        return required\n\n\nclass CalculatorTool(Tool):\n    \"\"\"计算器工具\"\"\"\n    \n    @property\n    def name(self) -> str:\n        return \"calculator\"\n    \n    @property\n    def description(self) -> str:\n        return \"执行数学计算，支持加减乘除等基本运算\"\n    \n    def execute(self, expression: str) -> str:\n        \"\"\"\n        执行计算\n        \n        Args:\n            expression: 数学表达式，如 \"2 + 3 * 4\"\n        \n        Returns:\n            str: 计算结果\n        \"\"\"\n        try:\n            # 注意：eval存在安全风险，这里简化处理\n            # 生产环境应该使用安全的表达式解析器\n            result = eval(expression, {\"__builtins__\": {}}, {})\n            return f\"计算结果: {