"""
This module contains utility functions for the Lazy Machine Learning app.
"""

from .data_processing import load_data, prepare_data
from .file_operations import get_table_download_link, get_download_link, to_excel

__all__ = [
    'load_data',
    'prepare_data',
    'get_table_download_link',
    'get_download_link',
    'to_excel'
]

# You can add any package-level initialization code here if needed

def get_version():
    """
    Returns the version of the utils package.
    """
    return "1.0.0"

# You can add more utility functions here if needed