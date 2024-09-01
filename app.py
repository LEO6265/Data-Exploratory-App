import streamlit as st
import pandas as pd

st.title('Data Explorer')

st.markdown("### This is a web app for Data Exploration")

uploaded_file = st.file_uploader('Upload your file here')

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.header('Data Statistics')
    st.write(df.describe())

    st.header('First 10 rows of the Data')
    st.write(df.head(10))