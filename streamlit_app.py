import streamlit as st
import requests

st.set_page_config(page_title="Buy vs Rent", page_icon="🏠")

st.title("🏠 Buy vs Rent Predictor By avadhesh")

st.write("Enter your details:")

monthly_salary = st.number_input("Monthly Salary", min_value=0)
age = st.number_input("Age", min_value=18)
house_price = st.number_input("House Price", min_value=0)
down_payment = st.number_input("Down Payment", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
running_emi = st.number_input("Current EMI", min_value=0)

if st.button("Predict"):
    payload = {
        "monthly_salary": monthly_salary,
        "age": age,
        "house_price": house_price,
        "down_payment": down_payment,
        "loan_amount": loan_amount,
        "running_emi": running_emi
    }

    try:
        response = requests.post(
            "http://localhost:8000/predict",
            json=payload
        )

        if response.status_code == 200:
            result = response.json()

            if "Buy" in result["prediction"]:
                st.success(result["prediction"])
            else:
                st.warning(result["prediction"])

        else:
            st.error("❌ API Error")

    except:
        st.error("🚨 FastAPI not running!")