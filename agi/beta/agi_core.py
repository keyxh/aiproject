"""
AGI Core Module

This module implements the core functionality of a General Artificial Intelligence system
using OpenAI's API as the underlying model provider. It provides a framework for
autonomous reasoning, goal setting, memory management, and task execution.
"""

import asyncio
import json
import logging
import time
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass
from enum import Enum

import openai
from openai import AsyncOpenAI

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = AsyncOpenAI(api_key="YOUR_OPENAI_API_KEY")


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Task:
    id: str
    description: str
    status: TaskStatus
    priority: int = 1
    created_at: float = None
    updated_at: float = None
    result: Optional[str] = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = time.time()
        if self.updated_at is None:
            self.updated_at = time.time()

    def update_status(self, status: TaskStatus, result: str = None):
        self.status = status
        self.result = result
        self.updated_at = time.time()

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "priority": self.priority,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "result": self.result
        }


class Memory:
    """A simple persistent memory system using JSON file storage."""

    def __init__(self, filename: str = "memory.json"):
        self.filename = filename
        self.data = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            logger.info("Memory file not found, creating new one")
            self.data = {}
        except Exception as e:
            logger.error(f"Error loading memory: {e}")
            self.data = {}

    def save(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving memory: {e}")

    def add(self, key: str, value: Any):
        self.data[key] = value
        self.save()

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def remove(self, key: str):
        if key in self.data:
            del self.data[key]
            self.save()

    def clear(self):
        self.data.clear()
        self.save()


class AGI:
    """General Artificial Intelligence Core Implementation"""

    def __init__(self, model_name: str = "gpt-4", max_retries: int = 3):
        self.model_name = model_name
        self.max_retries = max_retries
        self.tasks: List[Task] = []
        self.memory = Memory()
        self.system_prompt = ("You are a general artificial intelligence agent capable of autonomous reasoning, problem solving, and goal achievement. "
                             "You can plan, execute, and reflect on your actions. You have access to memory, tools, and reasoning capabilities. "
                             "Respond concisely and directly to questions. Use markdown formatting when appropriate.")

    async def _call_openai(self, messages: List[Dict], temperature: float = 0.7) -> str:
        """Call OpenAI API with retry logic"""
        for attempt in range(self.max_retries):
            try:
                response = await client.chat.completions.create(
                    model=self.model_name,
                    messages=messages,
                    temperature=temperature,
                    max_tokens=4096,
                    top_p=1.0,
                    frequency_penalty=0.0,
                    presence_penalty=0.0
                )
                return response.choices[0].message.content.strip()
            except Exception as e:
                logger.warning(f"OpenAI API call failed (attempt {attempt + 1}): {e}")
                if attempt == self.max_retries - 1:
                    raise
                await asyncio.sleep(2 ** attempt)  # Exponential backoff

    async def create_task(self, description: str, priority: int = 1) -> Task:
        """Create a new task and add it to the task list"""
        task_id = f"task_{int(time.time() * 1000)}_{len(self.tasks)}"
        task = Task(id=task_id, description=description, priority=priority, status=TaskStatus.PENDING)
        self.tasks.append(task)
        logger.info(f"Created task: {task_id} - {description}")
        return task

    async def execute_task(self, task: Task) -> Task:
        """Execute a single task using AI reasoning"""
        task.update_status(TaskStatus.IN_PROGRESS)

        # Retrieve relevant memory context
        context = self._get_context_for_task(task)

        # Prepare prompt
        prompt = f"{self.system_prompt}\n\nContext:\n{context}\n\nTask: {task.description}\n\nPlease complete this task and provide your result in a concise manner."

        # Call OpenAI API
        try:
            response = await self._call_openai([
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ])

            task.update_status(TaskStatus.COMPLETED, response)
            logger.info(f"Completed task: {task.id} - {response[:50]}...")
            return task
        except Exception as e:
            task.update_status(TaskStatus.FAILED, str(e))
            logger.error(f"Failed to complete task {task.id}: {e}")
            return task

    def _get_context_for_task(self, task: Task) -> str:
        """Get relevant context from memory for the current task"""
        context = """
        Previous tasks and their results:
        """

        # Add recent completed tasks
        recent_tasks = [t for t in self.tasks if t.status == TaskStatus.COMPLETED and t.id != task.id]
        recent_tasks.sort(key=lambda x: x.updated_at, reverse=True)
        for t in recent_tasks[:3]:  # Limit to last 3 completed tasks
            context += f"- Task {t.id}: {t.description[:50]}... Result: {t.result[:100]}\n"

        # Add any relevant memory entries
        memory_keys = self.memory.data.keys()
        relevant_memory = [k for k in memory_keys if task.description.lower() in k.lower() or task.description.lower() in str(self.memory.data[k]).lower()]
        for key in relevant_memory[:2]:  # Limit to 2 relevant memories
            context += f"- Memory: {key}: {self.memory.data[key]}\n"

        return context

    async def run(self, tasks: List[str]) -> List[Task]:
        """Run a list of tasks sequentially"""
        results = []
        for task_desc in tasks:
            task = await self.create_task(task_desc)
            executed_task = await self.execute_task(task)
            results.append(executed_task)
            await asyncio.sleep(1)  # Small delay between tasks

        return results

    async def self_reflection(self) -> str:
        """Perform self-reflection on the AGI's performance"""
        prompt = f"{self.system_prompt}\n\nYou are an AI agent reflecting on your own behavior. Analyze your recent activities and provide insights on what you've learned, what could be improved, and how you might approach future tasks more effectively.\n\nRecent tasks performed: {len([t for t in self.tasks if t.status == TaskStatus.COMPLETED])} completed, {len([t for t in self.tasks if t.status == TaskStatus.FAILED])} failed.\n\nProvide a concise reflection in markdown format."

        try:
            response = await self._call_openai([
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": prompt}
            ])
            self.memory.add("self_reflection", response)
            return response
        except Exception as e:
            logger.error(f"Self-reflection failed: {e}")
            return f"Reflection failed: {e}"

    def get_task_summary(self) -> Dict:
        """Get a summary of all tasks"""
        summary = {
            "total_tasks": len(self.tasks),
            "pending": len([t for t in self.tasks if t.status == TaskStatus.PENDING]),
            "in_progress": len([t for t in self.tasks if t.status == TaskStatus.IN_PROGRESS]),
            "completed": len([t for t in self.tasks if t.status == TaskStatus.COMPLETED]),
            "failed": len([t for t in self.tasks if t.status == TaskStatus.FAILED])
        }
        return summary

    def save_state(self, filename: str = "agi_state.json"):
        """Save the current state of the AGI"""
        state = {
            "tasks": [task.to_dict() for task in self.tasks],
            "memory_data": self.memory.data,
            "model_name": self.model_name,
            "max_retries": self.max_retries
        }
        try:
            with open(filename, "w") as f:
                json.dump(state, f, indent=2)
            logger.info(f"AGI state saved to {filename}")
        except Exception as e:
            logger.error(f"Error saving AGI state: {e}")

    def load_state(self, filename: str = "agi_state.json"):
        """Load the previous state of the AGI"""
        try:
            with open(filename, "r") as f:
                state = json.load(f)
            self.tasks = [Task(**task_data) for task_data in state["tasks"]]
            self.memory.data = state["memory_data"]
            self.model_name = state["model_name"]
            self.max_retries = state["max_retries"]
            logger.info(f"AGI state loaded from {filename}")
        except Exception as e:
            logger.error(f"Error loading AGI state: {e}")
