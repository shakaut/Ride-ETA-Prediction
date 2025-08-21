import streamlit as st
import joblib
import numpy as np

model = joblib.load('ride_eta_model.pkl')
encoder = joblib.load('encoder.pkl')

st.subheader('Ride ETA Prediction App')

distance = st.number_input('Distance (km)', min_value=0.5, max_value=15.0, step=0.5)
traffic = st.selectbox('Traffic', ['low', 'medium', 'high'])
timeofday = st.selectbox('Time of Day', ['morning', 'noon', 'evening', 'night'])
weather = st.selectbox('Weather', ['clear', 'rainy'])

if st.button('Predict ETA'):
    encoded_features = encoder.transform([[traffic, timeofday, weather]])
    features = np.hstack([[distance], encoded_features[0]])

    prediction = model.predict([features])[0]

    # Enforce realistic minimum at prediction time too
    min_possible = distance * 2.5
    prediction = max(prediction, min_possible)


    st.success(f'Estimated Time of Arrival: {round(prediction, 1)} minutes')

