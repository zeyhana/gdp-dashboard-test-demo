import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder

# =========================
# TITLE
# =========================
st.title("✈️ Travel Insurance Prediction - Decision Tree")

st.write("Simple Decision Tree Model for Predicting Travel Insurance Purchase")

# =========================
# LOAD DATA
# =========================
uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # =========================
    # DATA PREPROCESSING
    # =========================
    st.subheader("Data Preprocessing")

    # Encode categorical columns
    label_encoder = LabelEncoder()

    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = label_encoder.fit_transform(df[column])

    st.write("Categorical data encoded successfully ✅")

    # =========================
    # FEATURES & TARGET
    # =========================
    X = df.drop("TravelInsurance", axis=1)
    y = df["TravelInsurance"]

    # Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # =========================
    # MODEL TRAINING
    # =========================
    model = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # =========================
    # EVALUATION
    # =========================
    accuracy = accuracy_score(y_test, y_pred)

    st.subheader("Model Evaluation")

    st.metric("Accuracy", f"{accuracy:.2f}")

    st.text("Classification Report")
    st.text(classification_report(y_test, y_pred))

    # =========================
    # SIMPLE USER INPUT
    # =========================
    st.subheader("Try Prediction")

    age = st.slider("Age", 20, 50, 30)
    income = st.number_input("Annual Income", 100000, 2000000, 500000)
    family = st.slider("Family Members", 1, 6, 2)
    flyer = st.selectbox("Frequent Flyer", [0, 1])
    abroad = st.selectbox("Ever Travelled Abroad", [0, 1])

    if st.button("Predict"):

        input_data = pd.DataFrame({
            "Age": [age],
            "AnnualIncome": [income],
            "FamilyMembers": [family],
            "FrequentFlyer": [flyer],
            "EverTravelledAbroad": [abroad]
        })

        # Menyesuaikan jumlah kolom
        missing_cols = set(X.columns) - set(input_data.columns)

        for col in missing_cols:
            input_data[col] = 0

        input_data = input_data[X.columns]

        prediction = model.predict(input_data)[0]

        if prediction == 1:
            st.success("Customer is likely to BUY travel insurance ✅")
        else:
            st.error("Customer is NOT likely to buy travel insurance ❌")

else:
    st.info("Please upload Travel Insurance CSV dataset first.")
