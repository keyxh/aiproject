#!/usr/bin/env python3
"""
Module for managing tasks in the AGI system.
This class handles task storage, processing, and interaction with OpenAI.
"""

from openai_integration import call_openai_api

class TaskManager:
    """
    Manages a list of tasks and processes them using OpenAI API.
    """
    
    def __init__(self):
        """
        Initialize the TaskManager with an empty task list.
        """
        self.tasks = []
    
    def add_task(self, task_description):
        """
        Add a new task to the list.
        
        Args:
            task_description (str): Description of the task.
        """
        self.tasks.append(task_description)
        print(f"Task added: {task_description}")
    
    def process_tasks(self):
        """
        Process all tasks in the list by calling OpenAI API.
        
        Returns:
            list: A list of responses for each task.
        """
        results = []
        for task in self.tasks:
            result = self._process_single_task(task)
            results.append(result)
        return results
    
    def _process_single_task(self, task):
        """
        Process a single task using OpenAI API.
        This can be extended for complex task decomposition.
        
        Args:
            task (str): The task description.
        
        Returns:
            str: The response from OpenAI.
        """
        # Construct a prompt for the task
        prompt = f"As an AGI, solve the following task: {task}. Provide a clear and comprehensive response."
        return call_openai_api(prompt)
    
    def clear_tasks(self):
        """
        Clear all tasks from the list.
        """
        self.tasks.clear()
        print("All tasks cleared.")