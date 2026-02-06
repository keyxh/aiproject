# agi

{
    "files": [
        {
            "filename": "requirements.txt",
            "content": "openai>=1.0.0\npython-dotenv>=1.0.0"
        },
        {
            "filename": ".env",
            "content": "OPENAI_API_KEY=your-api-key-here"
        },
        {
            "filename": "config.yaml",
            "content": "model: gpt-4o\ntemperature: 0.7\nmax_tokens: 1024\n"
        },
        {
            "filename": "agi.py",
            "content": "#!/usr/bin/env python3\n\"\"\"Simple AGI orchestrator using OpenAI API.\n\nThis module provides a lightweight wrapper around the OpenAI ChatCompletion\nendpoint, aiming to demonstrate how higher‑level tasks could be composed.\n\nIt is **not** a true AGI; it merely forwards prompts to a powerful LLM and\nreturns the response. The design is intentionally simple to match the role of\na junior engineer.\n\"\"\"\n\nimport os\nimport yaml\nimport openai\nfrom dotenv import load_dotenv\nfrom typing import List, Dict, Any\n\n# Load environment variables from .env (API key)\nload_dotenv()\n\n# ---------------------------------------------------------------------------\n# Configuration handling\n# ---------------------------------------------------------------------------\n\ndef load_config(path: str = \"config.yaml\") -> Dict[str, Any]:\n    \"\"\"Load YAML configuration.\n\n    Args:\n        path: Path to the YAML config file.\n\n    Returns:\n        A dictionary with configuration values.\n    \"\"\"\n    if not os.path.exists(path):\n        raise FileNotFoundError(f\"Configuration file '{path}' not found.\")\n    with open(path, \"r\", encoding=\"utf-8\") as f:\n        cfg = yaml.safe_load(f)\n    # Provide defaults if missing\n    cfg.setdefault(\"model\", \"gpt-4o\")\n    cfg.setdefault(\"temperature\", 0.7)\n    cfg.setdefault(\"max_tokens\", 1024)\n    return cfg\n\n# ---------------------------------------------------------------------------\n# Core AGI class\n# ---------------------------------------------------------------------------\n\nclass SimpleAGI:\n    \"\"\"A minimal orchestrator for interacting with OpenAI's chat models.\n\n    The class encapsulates request construction, error handling and a very\n    simple memory buffer that can be used to maintain context across calls.\n    \"\"\"\n\n    def __init__(self, config: Dict[str, Any]):\n        self.model = config[\"model\"]\n        self.temperature = config[\"temperature\"]\n        self.max_tokens = config[\"max_tokens\"]\n        # Simple in‑memory conversation history\n        self.history: List[Dict[str, str]] = []\n        # Ensure the API key is present\n        api_key = os.getenv(\"OPENAI_API_KEY\")\n        if not api_key:\n            raise EnvironmentError(\"OPENAI_API_KEY not set in environment.\")\n        openai.api_key = api_key\n\n    def _prepare_messages(self, user_input: str) -> List[Dict[str, str]]:\n        \"\"\"Combine history with the new user input.\n\n        Args:\