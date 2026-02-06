"""
Utility Functions

Various helper functions for the AGI project.
"""

import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

# Example utility function
def format_response(response: str) -> str:
    """Format the response for better readability."""
    return response.strip()