import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Tuple

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: Loaded dataframe.
    """
    return pd.read_csv(file_path)

def prepare_data(df: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """
    Prepare data for model training.

    Args:
    df (pd.DataFrame): Input dataframe.
    test_size (float): Proportion of the dataset to include in the test split.
    random_state (int): Controls the shuffling applied to the data before applying the split.

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]: X_train, X_test, y_train, y_test
    """
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)