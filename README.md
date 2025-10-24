Test the App Here: https://ride-eta-prediction.streamlit.app/  This app has gone to sleep due to inactivity

# Ride ETA (Estimated Time of Arrival) Prediction App

A **Streamlit web application** that predicts the **Estimated Time of Arrival (ETA)** for a ride based on:
- Distance (in km)
- Traffic conditions
- Time of day
- Weather conditions

The model is trained on **synthetic data** and uses **Linear Regression** with preprocessing steps to handle categorical variables.

---

## Features
- User-friendly Streamlit interface
- Predicts ETA in **minutes**
- Handles categorical inputs with **OneHotEncoding**
- Ensures **no negative prediction outputs**
- Lightweight and fast

---

## Tech Stack
- **Python 3.9+**
- **Streamlit** for UI
- **scikit-learn** for model training
- **pandas & numpy** for data handling
- **joblib** for model and encoder serialization

---

## Project Structure
- **ride_eta_model.pkl** Trained model file
- **encoder.pkl** OneHotEncoder object
- **streamlit_app.py** Streamlit application
- **requirements.txt** Python dependencies
- **README.md** Project documentation
