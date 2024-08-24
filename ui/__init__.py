"""
This module contains UI-related functions and components for the Lazy Machine Learning app.
"""

from .streamlit_ui import render_ui, render_sidebar, render_results

__all__ = ['render_ui', 'render_sidebar', 'render_results']

# You can add any package-level initialization code here if needed

def get_version():
    """
    Returns the version of the UI package.
    """
    return "1.0.0"

# You can add more utility functions here if needed