
import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
  page_title="Women's Fashion Trends",
    layout="wide"
) 
# Dataset
df = pd.read_csv(
    "summer-products.csv"
)

df['popular'] = np.where(
    df['units_sold'] > df['units_sold'].median(),
    1,
    0
)

features = [
    'price',
    'retail_price',
    'rating',
    'rating_count',
    'uses_ad_boosts',
    'merchant_rating'
]

X = df[features]
y = df['popular']



)

df['popular'] = np.where(
    df['units_sold'] > df['units_sold'].median(),
    1,
    0
)

features = [
    'price',
    'retail_price',
    'rating',
    'rating_count',
    'uses_ad_boosts',
    'merchant_rating'
]

X = df[features]
y = df['popular']

X = X.fillna(X.mean())

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

models = {
    "Logistic Regression":
        LogisticRegression(max_iter=1000),

    "Random Forest":
        RandomForestClassifier(
            n_estimators=100,
            random_state=42
        ),

    "XGBoost":
        XGBClassifier(
            eval_metric='logloss',
            random_state=42
        )
}

trained_models = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    trained_models[name] = model
    page_title="Women's Fashion Trends Dashboard",
    layout="wide"
)

st.title("Women's Fashion Trends Dashboard")

st.write(
    "Welcome to the Women's Fashion Trends Analysis Dashboard"
)
