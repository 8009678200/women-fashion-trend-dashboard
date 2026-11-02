
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Women's Fashion Trends Dashboard",
    layout="wide"
)

st.title("👗 Women's Fashion Trends Dashboard")
uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("✅ File Uploaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())
