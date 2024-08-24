import base64
import pandas as pd
from io import BytesIO

def to_excel(df: pd.DataFrame) -> bytes:
    """
    Convert a dataframe to Excel format.

    Args:
    df (pd.DataFrame): Input dataframe.

    Returns:
    bytes: Excel file content.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    return output.getvalue()

def get_table_download_link(df: pd.DataFrame) -> str:
    """
    Generate a download link for a dataframe as an Excel file.

    Args:
    df (pd.DataFrame): Input dataframe.

    Returns:
    str: HTML string containing the download link.
    """
    val = to_excel(df)
    b64 = base64.b64encode(val).decode()
    return f'<a href="data:application/octet-stream;base64,{b64}" download="data.xlsx">Download Excel file</a>'

def get_download_link(object_to_download, download_filename: str, download_link_text: str) -> str:
    """
    Generate a download link for any object.

    Args:
    object_to_download: Object to be downloaded.
    download_filename (str): Name of the file to be downloaded.
    download_link_text (str): Text to display for the download link.

    Returns:
    str: HTML string containing the download link.
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'