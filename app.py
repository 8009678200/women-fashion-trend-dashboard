import pandas as pd
import plotly.express as px

import streamlit as st

st.set_page_config(
    page_title="Women's Fashion Trends",
    layout="wide"
)

st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "Sentiment Analysis", "Topic Modeling", "About"]
)

if page == "Home":
    import streamlit as st

st.title("Home Page")

st.write("Welcome to Women's Fashion Dashboard")


st.title("Women's Fashion Trends Dashboard")

@st.cache_data
def load_data(file):
    return pd.read_csv(file)

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file:

    df = load_data(uploaded_file)

    st.success("Dataset Loaded")

    search = st.text_input("Search Product")

    if search:
        df = df[
            df["title"].astype(str).str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(df)
