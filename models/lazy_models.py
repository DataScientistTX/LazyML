from typing import Tuple, Dict
import pandas as pd
import numpy as np
from lazypredict.Supervised import LazyClassifier, LazyRegressor
from sklearn.base import BaseEstimator

def run_lazy_model(X_train: np.ndarray, X_test: np.ndarray, y_train: np.ndarray, y_test: np.ndarray, is_regression: bool) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Run lazy machine learning models on the given dataset.

    Args:
    X_train (np.ndarray): Training features.
    X_test (np.ndarray): Testing features.
    y_train (np.ndarray): Training target.
    y_test (np.ndarray): Testing target.
    is_regression (bool): If True, run regression models. If False, run classification models.

    Returns:
    Tuple[pd.DataFrame, pd.DataFrame]: A tuple containing two dataframes:
        - models: Performance metrics for each model
        - predictions: Predictions made by each model
    """
    if is_regression:
        model: BaseEstimator = LazyRegressor(verbose=0, ignore_warnings=True, custom_metric=None, predictions=True)
    else:
        model: BaseEstimator = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None, predictions=True)
    
    models, predictions = model.fit(X_train, X_test, y_train, y_test)

    # Add y_test to predictions for easier comparison
    predictions["y_test"] = y_test

    return models, predictions

def get_best_model(models: pd.DataFrame, metric: str = 'R-Squared' if is_regression else 'Accuracy') -> str:
    """
    Get the name of the best performing model based on the specified metric.

    Args:
    models (pd.DataFrame): DataFrame containing model performance metrics.
    metric (str): The metric to use for selecting the best model. 
                  Defaults to 'R-Squared' for regression and 'Accuracy' for classification.

    Returns:
    str: Name of the best performing model.
    """
    return models.sort_values(by=metric, ascending=False).index[0]

def get_feature_importance(best_model: BaseEstimator, feature_names: List[str]) -> pd.DataFrame:
    """
    Get feature importance for the best model, if available.

    Args:
    best_model (BaseEstimator): The best performing model.
    feature_names (List[str]): List of feature names.

    Returns:
    pd.DataFrame: DataFrame with feature importances, or None if not available.
    """
    if hasattr(best_model, 'feature_importances_'):
        importances = best_model.feature_importances_
        return pd.DataFrame({'feature': feature_names, 'importance': importances}).sort_values('importance', ascending=False)
    return None

# You can add more helper functions here as needed