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

    if "title" in df.columns:
        sort_col = st.selectbox("Sort By", df.columns)
        df = df.sort_values(sort_col)
    else:
        st.warning("The uploaded CSV does not contain a 'title' column.")
        st.stop()

    st.dataframe(df)

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) > 0:
        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        min_val = float(df[selected_col].min())
        max_val = float(df[selected_col].max())

        selected_range = st.slider(
            "Select Range",
            min_val,
            max_val,
            (min_val, max_val)
        )

        filtered_df = df[
            (df[selected_col] >= selected_range[0]) &
            (df[selected_col] <= selected_range[1])
        ]

        st.subheader("Filtered Dataset")
        st.dataframe(filtered_df)

        fig = px.histogram(
            filtered_df,
            x=selected_col,
            title=f"{selected_col} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )
