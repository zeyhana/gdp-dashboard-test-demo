import streamlit as st

st.title("✈️ Travel Insurance Prediction")

st.write("Simple Decision Tree Based on PPT")

# =========================
# INPUT
# =========================
income = st.selectbox(
    "Annual Income",
    ["Low / Medium", "High"]
)

travel_abroad = st.selectbox(
    "Ever Travelled Abroad?",
    ["No", "Yes"]
)

frequent_flyer = st.selectbox(
    "Frequent Flyer?",
    ["No", "Yes"]
)

employment = st.selectbox(
    "Private / Self Employee?",
    ["No", "Yes"]
)

graduate = st.selectbox(
    "Graduate?",
    ["No", "Yes"]
)

age = st.selectbox(
    "Age 30-34?",
    ["No", "Yes"]
)

# =========================
# DECISION TREE LOGIC
# =========================
if st.button("Predict"):

    # Annual Income
    if income == "Low / Medium":
        st.error("NO BUY ❌")

    else:

        # Ever Travelled Abroad
        if travel_abroad == "No":
            st.error("NO BUY ❌")

        else:

            # Frequent Flyer
            if frequent_flyer == "Yes":
                st.success("BUY ✅")

            else:

                # Employment Type
                if employment == "Yes":

                    # Age 30-34
                    if age == "Yes":
                        st.success("BUY ✅")
                    else:
                        st.error("NO BUY ❌")

                else:

                    # Graduate
                    if graduate == "Yes":
                        st.success("BUY ✅")
                    else:
                        st.error("NO BUY ❌")
