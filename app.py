import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline

# ==========================
# Page Configuration
# ==========================

st.set_page_config(
    page_title="Women's Fashion Trends Dashboard",
    page_icon="👗",
    layout="wide"
)

st.title("👗 Women's Fashion Trends Dashboard")
st.write("Upload a CSV file and analyze fashion product trends with AI.")

# ==========================
# Cache Sentiment Model
# ==========================

@st.cache_resource
def load_model():
    return pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english"
    )

sentiment_model = load_model()

# ==========================
# CSV Upload
# ==========================

st.header("📂 Upload CSV Dataset")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    try:

        # Read CSV
        df = pd.read_csv(uploaded_file)

        st.success("✅ File Uploaded Successfully")

        # ==========================
        # Dataset Preview
        # ==========================

        st.subheader("📊 Dataset Preview")
        st.dataframe(df.head())

        # ==========================
        # Dataset Shape
        # ==========================

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Rows", df.shape[0])

        with col2:
            st.metric("Columns", df.shape[1])

        # ==========================
        # Missing Values
        # ==========================

        st.subheader("📝 Missing Values")

        missing_values = df.isnull().sum().reset_index()
        missing_values.columns = ["Column", "Missing Values"]

        st.dataframe(missing_values)

        # ==========================
        # Summary Statistics
        # ==========================

        st.subheader("📈 Summary Statistics")

        st.dataframe(
            df.describe(include="all")
        )

        # ==========================
        # Rating Distribution
        # ==========================

        if "rating" in df.columns:

            st.subheader("⭐ Rating Distribution")

            fig = px.histogram(
                df,
                x="rating",
                title="Rating Distribution",
                color="rating"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ==========================
        # Price vs Units Sold
        # ==========================

        if (
            "price" in df.columns
            and
            "units_sold" in df.columns
        ):

            st.subheader("💰 Price vs Units Sold")

            fig2 = px.scatter(
                df,
                x="price",
                y="units_sold",
                color="rating"
                if "rating" in df.columns
                else None,
                title="Price vs Units Sold"
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        # ==========================
        # CSV Sentiment Analysis
        # ==========================

        if "title" in df.columns:

            st.subheader("🤖 Sentiment Analysis on Product Titles")

            if st.button("Run Sentiment Analysis"):

                sample_df = df.copy()

                sentiments = []

                progress_bar = st.progress(0)

                total_rows = len(sample_df)

                for i, text in enumerate(sample_df["title"]):

                    try:

                        prediction = sentiment_model(
                            str(text)[:512]
                        )[0]["label"]

                        sentiments.append(prediction)

                    except:

                        sentiments.append("UNKNOWN")

                    progress_bar.progress(
                        (i + 1) / total_rows
                    )

                sample_df["Sentiment"] = sentiments

                st.success(
                    "✅ Sentiment Analysis Completed"
                )

                st.dataframe(
                    sample_df[
                        ["title", "Sentiment"]
                    ].head(20)
                )

                # Pie Chart

                fig3 = px.pie(
                    sample_df,
                    names="Sentiment",
                    title="Sentiment Distribution"
                )

                st.plotly_chart(
                    fig3,
                    use_container_width=True
                )

        else:

            st.warning(
                "'title' column not found. CSV sentiment prediction requires a title column."
            )

    except Exception as e:

        st.error(
            f"Error reading file: {e}"
        )

# ==========================
# Custom Text Sentiment
# ==========================

st.header("💬 Custom Text Sentiment Analysis")

user_text = st.text_area(
    "Enter Product Title or Review"
)

if st.button("Analyze Sentiment"):

    if user_text.strip() != "":

        result = sentiment_model(user_text)[0]

        sentiment = result["label"]
        score = result["score"]

        if sentiment == "POSITIVE":

            st.success(
                f"😊 Positive ({score:.2%})"
            )

        else:

            st.error(
                f"😞 Negative ({score:.2%})"
            )

    else:

        st.warning(
            "Please enter some text."
        )

