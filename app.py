
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
    st.title("Women's Fashion Trends Dashboard")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Total Products", "15730")

    with col2:
        st.metric("Topics Identified", "7")

elif page == "Sentiment Analysis":
    st.title("Sentiment Analysis")
    st.write("Positive vs Negative Keyword Analysis")

elif page == "Topic Modeling":
    st.title("Topic Modeling")
    st.write("LDA Topic Modeling Results")

elif page == "About":
    st.title("About")
    st.write("Brainy Beam Internship Project")
