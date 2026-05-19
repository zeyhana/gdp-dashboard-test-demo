import streamlit as st
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

st.title("✈️ Travel Insurance Prediction")
st.write("Simple Decision Tree Prediction")

# =========================
# TRAINING DATA
# =========================
data = {
    "AnnualIncome": [300000, 1500000, 1200000, 400000],
    "EverTravelledAbroad": [0, 1, 1, 0],
    "TravelInsurance": [0, 1, 1, 0]
}

df = pd.DataFrame(data)

X = df[["AnnualIncome", "EverTravelledAbroad"]]
y = df["TravelInsurance"]

# =========================
# MODEL
# =========================
model = DecisionTreeClassifier()
model.fit(X, y)

# =========================
# USER INPUT
# =========================
st.subheader("Input Customer Data")

income = st.number_input(
    "Annual Income",
    min_value=100000,
    max_value=2000000,
    value=500000
)

abroad = st.selectbox(
    "Ever Travelled Abroad?",
    ["No", "Yes"]
)

# Convert Yes/No to 1/0
abroad_value = 1 if abroad == "Yes" else 0

# =========================
# PREDICTION
# =========================
if st.button("Predict"):

    input_data = pd.DataFrame({
        "AnnualIncome": [income],
        "EverTravelledAbroad": [abroad_value]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("BUY ✅")
    else:
        st.error("NO BUY ❌")
