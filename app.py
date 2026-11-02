
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
        col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])
            st.subheader("Missing Values")

    st.dataframe(
        df.isnull().sum().reset_index()
    )
    st.subheader("Summary Statistics")

    st.dataframe(
        df.describe()
    )
    if "rating" in df.columns:

        fig = px.histogram(
            df,
            x="rating",
            title="Rating Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
