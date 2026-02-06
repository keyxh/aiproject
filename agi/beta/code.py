# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) with the following requirements:
1. The project should implement a true AGI using OpenAI API
2. I should generate actual, runnable code following best practices
3. Include necessary comments and documentation
4. As a junior engineer, I should generate implementation code rather than architecture design
5. Return the response in JSON format

Since I'm acting as a junior engineer, I should focus on practical implementation code. For an AGI project using OpenAI API, I should create:
1. A basic project structure
2. Configuration management (API key handling)
3. Core AGI components (though true AGI doesn't exist yet, we can create a framework)
4. Example usage code
5. Documentation

Let me create a practical, runnable implementation that demonstrates the concept while being realistic about current AI limitations.

I'll structure this as:
- config.py - Configuration management
- core/agi_core.py - Main AGI core logic
- core/agent.py - Agent implementation
- services/openai_service.py - OpenAI API integration
- main.py - Entry point
- requirements.txt - Dependencies
- README.md - Documentation
- .env.example - Environment variables template

This provides a solid foundation for building AGI-like systems while being practical and runnable.
</think>

```json
{
    "files": [
        {
            "filename": "config.py",
            "content": "\"\"\"\n配置管理模块\n负责加载和管理项目配置，支持环境变量和配置文件\n\"\"\"\n\nimport os\nfrom pathlib import Path\nfrom typing import Optional\nfrom dotenv import load_dotenv\n\n\nclass Config:\n    \"\"\"\n    配置管理类\n    \n    负责从环境变量和.env文件加载配置，提供统一的配置访问接口\n    \"\"\"\n    \n    def __init__(self, config_path: Optional[str] = None):\n        \"\"\"\n        初始化配置管理\n        \n        Args:\n            config_path: 可选的配置文件路径\n        \"\"\"\n        # 加载.env文件\n        if config_path is None:\n            config_path = Path(__file__).parent / \".env\"\n        \n        if Path(config_path).exists():\n            load_dotenv(config_path)\n        \n        # OpenAI API配置\n        self.openai_api_key = os.getenv(\"OPENAI_API_KEY\", \"\")\n        self.openai_model = os.getenv(\"OPENAI_MODEL\", \"gpt-4\")\n        self.openai_api_base = os.getenv(\"OPENAI_API_BASE\", \"https://api.openai.com/v1\")\n        \n        # AGI系统配置\n        self.max_tokens = int(os.getenv(\"MAX_TOKENS\", 4000))\n        self.temperature = float(os.getenv(\"TEMPERATURE\", 0.7))\n        self.timeout = int(os.getenv(\"TIMEOUT\", 60))\n        \n        # 系统配置\n        self.debug = os.getenv(\"DEBUG\", \"false\").lower() == \"true\"\n        self.log_level = os.getenv(\"LOG_LEVEL\", \"INFO\")\n    \n    def validate(self) -> bool:\n        \"\"\"\n        验证配置是否有效\n        \n        Returns:\n            bool: 配置是否有效\n        \"\"\"\n        if not self.openai_api_key:\n            raise ValueError(\"OPENAI_API_KEY is not set. Please set it in .env file or environment variables.\")\n        \n        return True\n\n\n# 全局配置实例\nconfig = Config()\n"
        },
        {
            "filename": "requirements.txt",
            "content": "# AGI项目依赖\n# 基础依赖\nopenai>=1.0.0\npython-dotenv>=1.0.0\npydantic>=2.0.0\n\n# 日志和监控\nloguru>=0.7.0\n\n# 异步支持\naiohttp>=3.8.0\n\n# 工具库\nPyYAML>=6.0\ntqdm>=4.65.0\n\n# 开发依赖\npytest>=7.0.0\npytest-asyncio>=0.21.0\nblack>=23.0.0\nflake8>=6.0.0\n"
        },
        {
            "filename": "services/openai_service.py",
            "content": "\"\"\"\nOpenAI服务模块\n封装OpenAI API的调用，提供统一的接口\n\"\"\"\n\nimport asyncio\nimport logging\nfrom typing import Optional, Dict, Any, List\nfrom openai import AsyncOpenAI, OpenAIError\nfrom pydantic import BaseModel\n\nfrom config import config\n\n\nlogger = logging.getLogger(__name__)\n\n\nclass Message(BaseModel):\n    \"\"\"消息模型\"\"\"\n    role: str\n    content: str\n    \n    \nclass ChatRequest(BaseModel):\n    \"\"\"聊天请求模型\"\"\"\n    messages: List[Message]\n    max_tokens: Optional[int] = None\n    temperature: Optional[float] = None\n    model: Optional[str] = None\n\n\nclass ChatResponse(BaseModel):\n    \"\"\"聊天响应模型\"\"\"\n    content: str\n    model: str\n    usage: Dict[str, int]\n    \n\nclass OpenAIService:\n    \"\"\"\n    OpenAI服务类\n    \n    封装所有OpenAI API的调用，提供异步和同步两种接口\n    \"\"\"\n    \n    def __init__(self):\n        \"\"\"初始化OpenAI服务\"\"\"\n        self.client = AsyncOpenAI(\n            api_key=config.openai_api_key,\n            base_url=config.openai_api_base,\n            timeout=config.timeout\n        )\n        self.default_model = config.openai_model\n    \n    async def chat(self, request: ChatRequest) -> ChatResponse:\n        \"\"\"\n        异步发送聊天请求\n        \n        Args:\n            request: 聊天请求对象\n            \n        Returns:\n            ChatResponse: 聊天响应\n            \n        Raises:\n            OpenAIError: API调用失败时抛出\n        \"\"\"\n        try:\n            # 构建请求参数\n            messages = [msg.model_dump() for msg in request.messages]\n            \n            response = await self.client.chat.completions.create(\n                model=request.model or self.default_model,\n                messages=messages,\n                max_tokens=request.max_tokens or config.max_tokens,\n                temperature=request.temperature or config.temperature\n            )\n            \n            # 构建响应\n            content = response.choices[0].message.content\n            usage = {\n                \"prompt_tokens\": response.usage.prompt_tokens,\n                \"completion_tokens\": response.usage.completion_tokens,\n                \"total_tokens\": response.usage.total_tokens\n            }\n            \n            return ChatResponse(\n                content=content,\n                model=response.model,\n                usage=usage\n            )\n            \n        except OpenAIError as e:\n            logger.error(f\"OpenAI API错误: {e}\")\n            raise\n    \n    async def chat_simple(self, user_message: str, system_message: Optional[str] = None) -> ChatResponse:\n        \"\"\"\n        简单聊天接口\n        \n        Args:\n            user_message: 用户消息\n            system_message: 可选的系统消息\n            \n        Returns:\n            ChatResponse: 聊天响应\n        \"\"\"\n        messages = []\n        \n        if system_message:\n            messages.append(Message(role=\"system\", content=system_message))\n        \n        messages.append(Message(role=\"user\", content=user_message))\n        \n        request = ChatRequest(messages=messages)\n        return await self.chat(request)\n    \n    async def close(self):\n        \"\"\"关闭异步客户端\"\"\"\n        await self.client.close()\n\n\n# 服务实例\n_openai_service: Optional[OpenAIService] = None\n\n\ndef get_openai_service() -> OpenAIService:\n    \"\"\"获取OpenAI服务单例\"\"\"\n    global _openai_service\n    \n    if _openai_service is None:\n        _openai_service = OpenAIService()\n    \n    return _openai_service\n"
        },
        {
            "filename": "core/agent.py",
            "content": "\"\"\"\nAgent模块\n实现AGI的核心代理功能，包括推理、规划和执行\n\"\"\"\n\nimport asyncio\nimport logging\nfrom typing import Optional, List, Dict, Any\nfrom abc import ABC, abstractmethod\nfrom enum import Enum\n\nfrom services.openai_service import OpenAIService, ChatRequest, Message\n\n\nlogger = logging.getLogger(__name__)\n\n\nclass AgentState(Enum):\n    \"\"\"代理状态枚举\"\"\"\n    IDLE = \"idle\"\n    THINKING = \"thinking\"\n    ACTING = \"acting\"\n    LEARNING = \"learning\"\n    ERROR = \"error\"\n\n\nclass BaseAgent(ABC):\n    \"\"\"\n    基础代理类\n    \n    定义代理的基本接口和通用功能\n    \"\"\"\n   