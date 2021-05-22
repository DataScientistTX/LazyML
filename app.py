# -*- coding: utf-8 -*-
"""
Created on Fri May 21 21:28:10 2021

@author: serca
"""
from lazypredict.Supervised import LazyClassifier, LazyRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import streamlit as st
import base64

#Define functions for download links, and xlsx conversions---------------------
def to_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1',index=False)
    writer.save()
    processed_data = output.getvalue()
    return processed_data

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    val = to_excel(df)
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="example_data.xlsx">Please click here to download an example dataset for this app as an excel file.</a>' # decode b'abc' => abc


def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

@st.cache(allow_output_mutation=True)
def load_data(file):
    df = pd.read_csv(file)
    return df

st.header("Lazy Machine Learning for Regression and Classification Problems")
st.write("Upload your csv data from the left panel and investigate ML prediction results with no-code.")

result = st.checkbox("Click here to change ML mode to Regression")

if result:
    st.write("Current Mode:  Regression")
else:
    st.write("Current Mode:  Classification")

st.sidebar.title("Upload data")    
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    df = load_data(uploaded_file)
    n = len(df.columns)
    X = df.iloc[:,0:n-1].to_numpy() 
    y = df.iloc[:,n-1].to_numpy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2, random_state=42)

    if result == False:
        clf = LazyClassifier(predictions=True)
        models, predictions = clf.fit(X_train, X_test, y_train, y_test)

    if result == True:
        reg = LazyRegressor(predictions=True)
        models, predictions = reg.fit(X_train, X_test, y_train, y_test)
    predictions["y_test"] = y_test
    st.write(models)
    st.write(predictions)

    if st.button('Download Model List as CSV'):
        tmp_download_link_1 = download_link(models, 'model_list.csv', 'Click here to download the model list!')
        st.markdown(tmp_download_link_1, unsafe_allow_html=True)

    if st.button('Download Prediction Results as CSV'):
        tmp_download_link_2 = download_link(predictions, 'prediction_results.csv', 'Click here to download the prediction results!')
        st.markdown(tmp_download_link_2, unsafe_allow_html=True)

else:
    st.write("Please upload the data first")
    
st.write("Developer: Sercan Gul (sercan.gul@gmail.com, https://github.com/sercangul)")
st.write("Source code: https://github.com/sercangul/viscometerapi")