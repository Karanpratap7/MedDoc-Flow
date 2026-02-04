"""Chat utilities for MedDoc Flow.

This module provides functions for interacting with the Euri AI chat model.
"""

from euriai.langchain import create_chat_model
from typing import Any


def get_chat_model(api_key: str) -> Any:
    """Initialize and return a chat model.
    
    Args:
        api_key: Euri AI API key.
        
    Returns:
        Any: Initialized chat model instance.
    """
    chat_model = create_chat_model(
        model_name="gpt-4.1-nano",
        api_key=api_key,
        temperature=0.7
    )
    
    return chat_model


def ask_chat_model(chat_model: Any, prompt: str) -> str:
    """Send a prompt to the chat model and get a response.
    
    Args:
        chat_model: Initialized chat model instance.
        prompt: The prompt to send to the model.
        
    Returns:
        str: The model's response.
    """
    response = chat_model.invoke(prompt)
    
    # Extract content from the response
    if hasattr(response, 'content'):
        return response.content
    else:
        return str(response)
