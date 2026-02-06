# agi

<think>The user wants me to generate code for a project called "agi" (Artificial General Intelligence) as a junior engineer. The project aims to implement a true AGI using OpenAI API.

As a junior engineer, I should:
1. Generate practical, runnable code
2. Follow best practices
3. Include necessary comments and documentation
4. Focus on implementation rather than high-level architecture

The code should be in JSON format with a "files" array containing objects with "filename" and "content" properties.

Let me think about what a junior engineer would create for an AGI project using OpenAI API. A reasonable implementation would include:

1. A main entry point / orchestrator
2. A client wrapper for OpenAI API
3. A simple agent structure
4. Basic memory/context management
5. Configuration management
6. Some example usage

I'll create a modular but simple structure that demonstrates the core concepts of building an AGI-like system with OpenAI API.

Files to create:
1. config.yaml - Configuration
2. requirements.txt - Dependencies
3. openai_client.py - OpenAI API wrapper
4. memory.py - Simple memory/context management
5. agent.py - Core agent logic
6. main.py - Main entry point
7. examples.py - Example usage

Let me write comprehensive code with proper comments and documentation.
</think>

```json
{
    "files": [
        {
            "filename": "config.yaml",
            "content": "# AGI项目配置文件\n# 项目: 实现真正意义上的AGI\n# 作者: 初级工程师\n\n# OpenAI API配置\nopenai:\n  api_key: \"YOUR_API_KEY_HERE\"  # 请替换为您的OpenAI API密钥\n  model: \"gpt-4\"                 # 使用的模型\n  temperature: 0.7               # 温度参数，控制生成随机性\n  max_tokens: 4096               # 最大生成token数\n  timeout: 30                    # 请求超时时间（秒）\n\n# Agent配置\nagent:\n  name: \"AGI-Assistant\"\n  system_prompt: \"你是一个通用人工智能助手，具备强大的推理能力和学习能力。你可以帮助用户解决各种问题，包括编程、分析、创作等。请始终尽力提供准确、有帮助的回答。\"\n  max_context_length: 8192       # 最大上下文长度\n  memory_size: 100               # 记忆容量\n\n# 系统配置\nsystem:\n  debug: true                    # 调试模式\n  log_level: \"INFO\"              # 日志级别\n  save_memory: true              # 是否保存记忆到磁盘\n  memory_file: \"memory.json\"     # 记忆文件路径\n"
        },
        {
            "filename": "requirements.txt",
            "content": "# AGI项目依赖\n# 项目: 实现真正意义上的AGI\n\n# 核心依赖\nopenai>=1.0.0\npyyaml>=6.0\n\n# 日志和工具\npython-dotenv>=1.0.0\ncolorlog>=6.7.0\n\n# 异步支持\nasyncio\n\n# 类型检查（开发依赖）\nmypy>=1.0.0\ntypes-pyyaml>=6.0.0\n"
        },
        {
            "filename": "openai_client.py",
            "content": "\"\"\"\nOpenAI API客户端封装\n\n这个模块封装了与OpenAI API的交互，提供了简洁的接口来调用GPT模型。\n作为初级工程师，我遵循了以下最佳实践：\n1. 错误处理和异常捕获\n2. 配置外部化\n3. 清晰的接口设计\n4. 异步支持\n\n作者: 初级工程师\n创建日期: 2024-01-01\n\"\"\"\n\nimport os\nimport yaml\nimport logging\nfrom typing import Optional, List, Dict, Any\nfrom openai import OpenAI, AsyncOpenAI\nfrom openai.types.chat import ChatCompletion\n\n# 配置日志\nlogger = logging.getLogger(__name__)\n\n\nclass OpenAIClient:\n    \"\"\"\n    OpenAI API客户端类\n    \n    封装了OpenAI API的常见操作，包括同步和异步调用。\n    \n    属性:\n        client: 同步OpenAI客户端\n        async_client: 异步OpenAI客户端\n        config: 配置字典\n    \"\"\"\n\n    def __init__(self, config_path: str = \"config.yaml\"):\n        \"\"\"\n        初始化OpenAI客户端\n        \n        参数:\n            config_path: 配置文件路径\n        \"\"\"\n        self.config = self._load_config(config_path)\n        self.client = self._create_sync_client()\n        self.async_client = self._create_async_client()\n        \n        logger.info(\"OpenAI客户端初始化完成\")\n\n    def _load_config(self, config_path: str) -> Dict[str, Any]:\n        \"\"\"\n        加载配置文件\n        \n        参数:\n            config_path: 配置文件路径\n            \n        返回:\n            配置字典\n        \"\"\"\n        try:\n            with open(config_path, 'r', encoding='utf-8') as f:\n                config = yaml.safe_load(f)\n                return config.get('openai', {})\n        except FileNotFoundError:\n            logger.warning(f\"配置文件 {config_path} 未找到，使用默认配置\")\n            return {}\n        except Exception as e:\n            logger.error(f\"加载配置文件失败: {e}\")\n            raise\n\n    def _create_sync_client(self) -> OpenAI:\n        \"\"\"\n        创建同步OpenAI客户端\n        \n        返回:\n            OpenAI客户端实例\n        \"\"\"\n        api_key = self.config.get('api_key') or os.getenv('OPENAI_API_KEY')\n        \n        if not api_key:\n            raise ValueError(\"未设置OpenAI API密钥，请在config.yaml中设置或设置环境变量OPENAI_API_KEY\")\n        \n        return OpenAI(\n            api_key=api_key,\n            timeout=self.config.get('timeout', 30)\n        )\n\n    def _create_async_client(self) -> AsyncOpenAI:\n        \"\"\"\n        创建异步OpenAI客户端\n        \n        返回:\n            异步OpenAI客户端实例\n        \"\"\"\n        api_key = self.config.get('api_key') or os.getenv('OPENAI_API_KEY')\n        \n        return AsyncOpenAI(\n            api_key=api_key,\n            timeout=self.config.get('timeout', 30)\n        )\n\n    def chat(\n        self,\n        messages: List[Dict[str, str]],\n        model: Optional[str] = None,\n        temperature: Optional[float] = None,\n        max_tokens: Optional[int] = None\n    ) -> ChatCompletion:\n        \"\"\"\n        同步聊天请求\n        \n        参数:\n            messages: 消息列表，格式为[{\"role\": \"user\", \"content\": \"你好\"}]\n            model: 模型名称，默认使用配置文件中的模型\n            temperature: 温度参数\n            max_tokens: 最大token数\n            \n        返回:\n            ChatCompletion响应对象\n        \"\"\"\n        try:\n            # 使用默认值或配置文件中的值\n            model = model or self.config.get('model', 'gpt-4')\n            temperature = temperature if temperature is not None else self.config.get('temperature', 0.7)\n            max_tokens = max_tokens or self.config.get('max_tokens', 4096)\n\n            logger.debug(f\"发送请求到模型: {model}\")\n            \n            response = self.client.chat.completions.create(\n                model=model,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=max_tokens\n            )\n            \n            logger.debug(f\"模型响应完成，消耗tokens: {response.usage.total_tokens}\")\n            return response\n\n        except Exception as e:\n            logger.error(f\"API请求失败: {e}\")\n            raise\n\n    async def async_chat(\n        self,\n        messages: List[Dict[str, str]],\n        model: Optional[str] = None,\n        temperature: Optional[float] = None,\n        max_tokens: Optional[int] = None\n    ) -> ChatCompletion:\n        \"\"\"\n        异步聊天请求\n        \n        参数:\n            messages: 消息列表\n            model: 模型名称\n            temperature: 温度参数\n            max_tokens: 最大token数\n            \n        返回:\n            ChatCompletion响应对象\n        \"\"\"\n        try:\n            model = model or self.config.get('model', 'gpt-4')\n            temperature = temperature if temperature is not None else self.config.get('temperature', 0.7)\n            max_tokens = max_tokens or self.config.get('max_tokens', 4096)\n\n            response = await self.async_client.chat.completions.create(\n                model=model,\n                messages=messages,\n                temperature=temperature,\n                max_tokens=max_tokens\n            )\n            \n            return response\n\n        except Exception as e:\n            logger.error(f\"异步API请求失败: {e}\")\n            raise\n\n    def get_response_content(self, response: ChatCompletion) -> str:\n        \"\"