import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# Set page configuration
st.set_page_config(page_title="Water Quality",
                   layout="wide",
                   page_icon="💧")

water_model = pickle.load(open('water_potability.pkl', 'rb'))

# Water quality Prediction Page
# Page title
st.title('Water Quality Classification')

col1, col2, col3 = st.columns(3)

with col1:
    ph = st.text_input('ph')

with col2:
    Hardness = st.text_input('Hardness')

with col3:
    Solids = st.text_input('Solids')

with col1:
    Chloramines = st.text_input('Chloramines')

with col2:
    Sulfate = st.text_input('Sulfate')

with col3:
    Conductivity = st.text_input('Conductivity')

with col1:
    Organic_carbon = st.text_input('Organic_carbon')

with col2:
    Trihalomethanes = st.text_input('Trihalomethanes')

with col3:
    Turbidity = st.text_input('Turbidity')

# Code for Prediction
water_potability = ''

# Creating a button for Prediction
if st.button('Predict Water potability'):
    # Check if any input field is empty
    user_input = [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]
    
    if '' in user_input:
        water_potability = 'Kindly fill all the input fields'
    else:
        if water_model is not None:
            try:
                user_input = [float(x) for x in user_input]  # Convert input to float

                water_prediction = water_model.predict([user_input])

                if water_prediction[0] == 1:
                    water_potability = 'The water is potable'
                elif water_prediction[0] == 0:
                    water_potability = 'The water is not potable'
            except Exception as e:
                water_potability = f"Error in prediction: {e}"
        else:
            water_potability = "Water potability model not available."

    st.success(water_potability)
