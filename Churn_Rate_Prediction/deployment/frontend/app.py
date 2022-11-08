import json
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st
import requests

# load pipeline
pipe = pickle.load(open("model/data_pipeline.pkl", "rb"))

img = plt.imread("model/churn.png")
st.image(img)

st.title("Aplikasi Pengecekan Telco Customer Churn")
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ['Yes', 'No'])
dependent = st.selectbox("Dependent", ['Yes', 'No'])
tenure = st.number_input("Tenure")
online_sec = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])
online_back = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])
dev_protect = st.selectbox("Device Protection", ['Yes', 'No', 'No internet service'])
tech_sup = st.selectbox("Tech Support", ['Yes', 'No', 'No internet service'])
contract = st.selectbox("Contract", ["Month-to-month", 'One year', 'Two year'])
pbilling = st.selectbox("Paperless Billing", ['Yes', 'No'])
pmethod = st.selectbox("Payment Method", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

new_data = {'SeniorCitizen': senior,
         'Partner': partner,
         'Dependents' : dependent,
         'tenure' :tenure,
         'OnlineSecurity' : online_sec,
         'OnlineBackup' : online_back,
         'DeviceProtection' : dev_protect,
         'TechSupport' : tech_sup,
         'Contract' : contract,
         'PaperlessBilling' : pbilling,
         'PaymentMethod' : pmethod,
         'MonthlyCharges' : monthly,
         'TotalCharges' : total}
new_data = pd.DataFrame([new_data])

# build feature
new_data = pipe.transform(new_data)
new_data = new_data.tolist()

# inference
URL = 'http://churn-model-ml1p2-frontend.herokuapp.com/v1/models/churn_model:predict'
param = json.dumps({
        "signature_name":"serving_default",
        "instances":new_data
    })
r = requests.post(URL, data=param)

if r.status_code == 200:
    res = r.json()
    if res['predictions'][0][0] > 0.5:
        st.title("Churn")
    else:
        st.title("Not Churn")
else:
    st.title("Unexpected Error")