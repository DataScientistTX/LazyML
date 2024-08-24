import streamlit as st
import pandas as pd
import os
from typing import Optional
from utils.file_operations import get_table_download_link

def render_ui():
    """Render the main UI components."""
    st.set_page_config(page_title="Lazy Machine Learning App", page_icon="🤖", layout="wide")
    st.header("Lazy Machine Learning for Regression and Classification Problems")
    st.write("Upload your CSV data from the left panel or use the example dataset to investigate ML prediction results with no-code.")

def render_sidebar() -> Optional[pd.DataFrame]:
    """
    Render the sidebar UI components.
    
    Returns:
    Optional[pd.DataFrame]: The loaded dataframe if an example dataset is used, otherwise None.
    """
    st.sidebar.title("Data Selection")
    st.sidebar.info("You can use the example dataset or upload your own CSV file.")
    
    use_example_data = st.sidebar.checkbox("Use example dataset")
    
    if use_example_data:
        example_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dataset.csv')
        df = pd.read_csv(example_data_path)
        st.sidebar.success("Using example dataset!")
        st.sidebar.markdown(get_table_download_link(df), unsafe_allow_html=True)
        return df
    else:
        uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.sidebar.success("Dataset uploaded successfully!")
            return df
    
    return None

def render_data_info(df: pd.DataFrame):
    """Render information about the loaded dataset."""
    st.subheader("Dataset Information")
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")
    
    st.write("First few rows of the dataset:")
    st.write(df.head())
    
    st.write("Summary statistics:")
    st.write(df.describe())

def render_model_selection():
    """Render the model selection UI components."""
    st.subheader("Model Selection")
    is_regression = st.checkbox("Use Regression Models", value=False)
    mode = "Regression" if is_regression else "Classification"
    st.write(f"Current Mode: {mode}")
    return is_regression

def render_results(models: pd.DataFrame, predictions: pd.DataFrame):
    """Render the results of the machine learning models."""
    st.subheader("Model Performance")
    st.write(models)
    
    st.subheader("Predictions")
    st.write(predictions)

    # Add download buttons for results
    st.download_button(
        label="Download Model Performance as CSV",
        data=models.to_csv().encode('utf-8'),
        file_name="model_performance.csv",
        mime="text/csv"
    )
    st.download_button(
        label="Download Predictions as CSV",
        data=predictions.to_csv().encode('utf-8'),
        file_name="predictions.csv",
        mime="text/csv"
    )

def render_feature_importance(feature_importance: Optional[pd.DataFrame]):
    """Render feature importance if available."""
    if feature_importance is not None:
        st.subheader("Feature Importance")
        st.bar_chart(feature_importance.set_index('feature')['importance'])

def render_footer():
    """Render the footer with developer information."""
    st.markdown("---")
    st.write("Developer: Sercan Gul (sercan.gul@gmail.com, https://github.com/sercangul)")
    st.write("Source code: https://github.com/sercangul/viscometerapi")

def render_error(message: str):
    """Render an error message."""
    st.error(message)

# Main UI function that calls all the other functions
def render_main_ui():
    render_ui()
    df = render_sidebar()
    
    if df is not None:
        render_data_info(df)
        is_regression = render_model_selection()
        return df, is_regression
    else:
        render_error("Please upload a dataset or use the example dataset to proceed.")
        return None, None