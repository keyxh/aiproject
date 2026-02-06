# agi

<think>The user is asking me to generate code for a project called "agi" (Artificial General Intelligence) that aims to implement a true AGI using OpenAI API. They want me to act as a senior engineer and generate practical, runnable code following best practices with necessary comments and documentation.

The response should be in JSON format with a "files" array containing objects with "filename" and "content" keys.

Let me think about what a senior engineer would create for such a project:

1. Core AGI orchestration system
2. Memory management system
3. Task planning and execution
4. Tool/function calling capabilities
5. Configuration management
6. Main entry point
7. API wrappers for OpenAI

I'll create a comprehensive AGI framework that includes:
- Main orchestrator that coordinates all components
- Memory system (short-term and long-term)
- Task planning and execution system
- Tool/function calling system
- Configuration file
- Requirements.txt
- API client wrapper
- Main entry point

Let me structure this properly as a senior engineer would, with clean code, good documentation, and best practices.
</think>

```json
{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "# AGI Project Dependencies\nopenai>=1.0.0\npython-dotenv>=1.0.0\npydantic>=2.0.0\nloguru>=0.7.0\ncolorama>=0.4.6\n\n# For memory persistence (optional)\nchromadb>=0.4.0\n\n# For async operations\nasyncio\nhttpx>=0.25.0"
        },
        {
            "filename": ".env.example",
            "content": "# AGI Configuration Template\n# Copy this file to .env and fill in your values\n\n# OpenAI API Configuration\nOPENAI_API_KEY=your_api_key_here\nOPENAI_MODEL=gpt-4-turbo-preview\nOPENAI_BASE_URL=https://api.openai.com/v1\n\n# AGI Configuration\nAGI_NAME=Assistant\nAGI_DEBUG=true\nAGI_MAX_TOKENS=4096\nAGI_TEMPERATURE=0.7\n\n# Memory Configuration\nAGI_MEMORY_TYPE=vector  # options: vector, simple\nAGI_PERSIST_DIR=./data/memory\n\n# Task Configuration\nAGI_MAX_ITERATIONS=100\nAGI_TIMEOUT_SECONDS=300"
        },
        {
            "filename": "config/settings.py",
            "content": "\"\"\"\nAGI Project Configuration Module\nHandles all configuration management with environment variable support.\n\"\"\"\n\nimport os\nfrom pathlib import Path\nfrom typing import Optional\nfrom dataclasses import dataclass, field\n\nfrom dotenv import load_dotenv\n\n# Load environment variables from .env file\nload_dotenv()\n\n\n@dataclass\nclass OpenAIConfig:\n    \"\"\"OpenAI API configuration.\"\"\"\n    api_key: str = os.getenv(\"OPENAI_API_KEY\", \"\")\n    model: str = os.getenv(\"OPENAI_MODEL\", \"gpt-4-turbo-preview\")\n    base_url: str = os.getenv(\"OPENAI_BASE_URL\", \"https://api.openai.com/v1\")\n    max_tokens: int = int(os.getenv(\"AGI_MAX_TOKENS\", \"4096\"))\n    temperature: float = float(os.getenv(\"AGI_TEMPERATURE\", \"0.7\"))\n\n    def validate(self) -> bool:\n        \"\"\"Validate that required configuration is present.\"\"\"\n        if not self.api_key:\n            raise ValueError(\"OPENAI_API_KEY is required\")\n        return True\n\n\n@dataclass\nclass MemoryConfig:\n    \"\"\"Memory system configuration.\"\"\"\n    memory_type: str = os.getenv(\"AGI_MEMORY_TYPE\", \"vector\")\n    persist_dir: Path = Path(os.getenv(\"AGI_PERSIST_DIR\", \"./data/memory\"))\n    max_memories: int = int(os.getenv(\"AGI_MAX_MEMORIES\", \"1000\"))\n\n    def __post_init__(self):\n        \"\"\"Ensure persist directory exists.\"\"\"\n        self.persist_dir.mkdir(parents=True, exist_ok=True)\n\n\n@dataclass\nclass TaskConfig:\n    \"\"\"Task execution configuration.\"\"\"\n    max_iterations: int = int(os.getenv(\"AGI_MAX_ITERATIONS\", \"100\"))\n    timeout_seconds: int = int(os.getenv(\"AGI_TIMEOUT_SECONDS\", \"300\"))\n    checkpoint_interval: int = 10\n\n\n@dataclass\nclass AGIConfig:\n    \"\"\"Main AGI configuration combining all subsystems.\"\"\"\n    name: str = os.getenv(\"AGI_NAME\", \"Assistant\")\n    debug: bool = os.getenv(\"AGI_DEBUG\", \"true\").lower() == \"true\"\n    \n    openai: OpenAIConfig = field(default_factory=OpenAIConfig)\n    memory: MemoryConfig = field(default_factory=MemoryConfig)\n    task: TaskConfig = field(default_factory=TaskConfig)\n\n    def __post_init__(self):\n        \"\"\"Validate configuration on initialization.\"\"\"\n        self.openai.validate()\n\n\ndef get_config() -> AGIConfig:\n    \"\"\"Get the AGI configuration instance.\"\"\"\n    return AGIConfig()\n"
        },
        {
            "filename": "core/openai_client.py",
            "content": "\"\"\"\nOpenAI API Client Wrapper\nProvides a clean interface for interacting with OpenAI models.\n\"\"\"\n\nimport asyncio\nfrom typing import Optional, List, Dict, Any\nfrom loguru import logger\n\nfrom openai import OpenAI, AsyncOpenAI\nfrom openai.types.chat import ChatCompletion, ChatCompletionMessage\n\nfrom config.settings import OpenAIConfig\n\n\nclass OpenAIClient:\n    \"\"\"\n    Wrapper for OpenAI API with synchronous and asynchronous support.\n    \n    Attributes:\n        client: Synchronous OpenAI client\n        async_client: Asynchronous OpenAI client\n        config: OpenAI configuration\n    \"\"\"\n\n    def __init__(self, config: OpenAIConfig):\n        \"\"\"\n        Initialize the OpenAI client.\n        \n        Args:\n            config: OpenAI configuration object\n        \"\"\"\n        self.config = config\n        \n        # Initialize synchronous client\n        self.client = OpenAI(\n            api_key=config.api_key,\n            base_url=config.base_url,\n        )\n        \n        # Initialize asynchronous client\n        self.async_client = AsyncOpenAI(\n            api_key=config.api_key,\n            base_url=config.base_url,\n        )\n        \n        logger.info(f\"OpenAI client initialized with model: {config.model}\")\n\n    def chat(\n        self,\n        messages: List[Dict[str, str]],\n        temperature: Optional[float] = None,\n        max_tokens: Optional[int] = None,\n    ) -> ChatCompletion:\n        \"\"\"\n        Send a synchronous chat request.\n        \n        Args:\n            messages: List of message dictionaries with 'role' and 'content'\n            temperature: Optional temperature override\n            max_tokens: Optional max tokens override\n            \n        Returns:\n            ChatCompletion response object\n        \"\"\"\n        try:\n            response = self.client.chat.completions.create(\n                model=self.config.model,\n                messages=messages,\n                temperature=temperature or self.config.temperature,\n                max_tokens=max_tokens or self.config.max_tokens,\n            )\n            \n            logger.debug(f\"Received response: {response.usage}\")\n            return response\n            \n        except Exception as e:\n            logger.error(f\"Error in chat request: {e}\")\n            raise\n\n    async def async_chat(\n        self,\n        messages: List[Dict[str, str]],\n        temperature: Optional[float] = None,\n        max_tokens: Optional[int] = None,\n    ) -> ChatCompletion:\n        \"\"\"\n        Send an asynchronous chat request.\n        \n        Args:\n            messages: List of message dictionaries with 'role' and 'content'\n            temperature: Optional temperature override\n            max_tokens: Optional max tokens override\n            \n        Returns:\n            ChatCompletion response object\n        \"\"\"\n        try:\n            response = await self.async_client.chat.completions.create(\n                model=self.config.model,\n                messages=messages,\n                temperature=temperature or self.config.temperature,\n                max_tokens=max_tokens or self.config.max_tokens,\n            )\n            \n            logger.debug(f\"Received async response: {response.usage}\")\n            return response\n            \n        except Exception as e:\n            logger.error(f\"Error in async chat request: {e}\")\n            raise\n\n    def extract_content(self, response: ChatCompletion) -> str:\n        \"\"\"\n        Extract text content from a chat completion response.\n        \n        Args:\n            response: ChatCompletion response object\n            \n        Returns:\n            Extracted text content\n        \"\"\"\n        if response.choices and response.choices[0].