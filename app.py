import streamlit as st
from skops.io import load
import pandas as pd

st.title("House Price Prediction App")

# Load the trained model
model=load("model/model.skops")


# User input 
area=st.number_input("Put Area of land")
bedrooms=st.number_input("Number of beds")
age=st.number_input("Age of house")

user_data=pd.DataFrame({
    'Area_sqft':[area],
    'Bedrooms':[bedrooms],
    'Age_years':[age]
})

# prediction of house price
if st.button("Predict"):
    if area > 0 and bedrooms > 0 and age > 0:
        prediction = model.predict(user_data)
        st.write(f'The predicted house price is: {prediction}')
    else:
        st.write(f'Please enter values greater than 0 for all fields to proceed')