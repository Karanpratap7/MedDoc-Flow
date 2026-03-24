"""Configuration module for MedDoc Flow.

This module contains API key configuration for the Euri AI service.
The API key is read from the EURI_API_KEY environment variable first,
falling back to a placeholder value if not set.
"""

import os

# Euri AI API Key - set via EURI_API_KEY environment variable or replace the
# placeholder below with your actual key.
EURI_API_KEY = os.getenv("EURI_API_KEY", "your_euri_api_key_here")
