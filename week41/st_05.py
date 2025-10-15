import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl

def load_data():
    try:
        df_load = pd.read_csv('loan_dataset.csv')
        st.write(df_load.head())
        st.bar_chart(df_load['Property_Area'].value_counts())
    except FileNotFoundError:
        st.error('File not found')
        return
    
def predict_loan():
    income = st.sidebar.slider('Income', min_value=0, max_value=13000, value=500)
    loan_amount = st.sidebar.slider('Loan Amount', min_value=0, max_value=400, value=50)

    try:
        model = pkl.load(open('Random_Forest.sav', 'rb'))
    except FileNotFoundError:
        st.error('Model not found')
        return

    if st.sidebar.button('Predict'):
        loan_predict = model.predict([[income, loan_amount]])

        if loan_predict[0] == 1:
            st.success('Loan Approved')
        else:
            st.error('Loan Rejected')

st.title('Loan Prediction')

choice = st.sidebar.selectbox('Select a page', ['Load Data', 'Predict Loan'])

if choice == 'Load Data':
    load_data()
elif choice == 'Predict Loan':
    predict_loan()