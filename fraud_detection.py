import streamlit as st
import pandas as pd
import joblib

model = joblib.load("fraud_detection_pipeline.pkl")

st.title("Fraud Detection Prediction System")

st.markdown("Please enter the transaction details and use the predict button")

st.divider()

transaction_type = st.selectbox("Transaction Type", ["CASH_OUT", "TRANSFER", "CASH_IN", "DEPOSIT", "PAYMENT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
old_balance_org = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
new_balance_org = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
old_balance_dest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
new_balance_dest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        "type": [transaction_type],
        "amount": [amount],
        "oldbalanceOrg": [old_balance_org],
        "newbalanceOrig": [new_balance_org],
        "oldbalanceDest": [old_balance_dest],
        "newbalanceDest": [new_balance_dest]
    })

    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction: '{int(prediction)}'")

    if prediction == 1:
        st.error("This transaction is likely to be fraudulent")
    else:
        st.success("This transaction is likely to be legitimate")