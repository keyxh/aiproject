# agi

 ```json
{
  "files": [
    {
      "filename": "requirements.txt",
      "content": "openai>=0.27.0\npython-dotenv>=0.19.0\n"
    },
    {
      "filename": ".env.example",
      "content": "# OpenAI API Configuration\nOPENAI_API_KEY=your_openai_api_key_here\nMODEL_NAME=gpt-4\nMAX_ITERATIONS=10\n"
    },
    {
      "filename": "config.py",
      "content": "\"\"\"\nConfiguration module for AGI project.\nHandles environment variables and global settings.\n\"\"\"\nimport os\nfrom dotenv import load_dotenv\n\n# Load environment variables from .env file\nload_dotenv()\n\n\nclass Config:\n    \"\"\"Configuration class containing all environment settings.\"\"\"\n    \n