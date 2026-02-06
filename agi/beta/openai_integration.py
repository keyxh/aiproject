#!/usr/bin/env python3
"""
Module for handling interactions with the OpenAI API.
This encapsulates API calls to ensure modularity and error handling.
"""

import openai
from config import OPENAI_API_KEY

# Set the API key
openai.api_key = OPENAI_API_KEY

def call_openai_api(prompt, model="gpt-4", max_tokens=1000, temperature=0.7):
    """
    Call the OpenAI API with a given prompt.
    
    Args:
        prompt (str): The input prompt for the model.
        model (str): The OpenAI model to use (default: "gpt-4").
        max_tokens (int): Maximum tokens in the response (default: 1000).
        temperature (float): Sampling temperature (default: 0.7).
    
    Returns:
        str: The model's response or an error message.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return response.choices[0].message.content.strip()
    except openai.error.OpenAIError as e:
        return f"OpenAI API error: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"