
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("rental_price_prediction_model_v1_0.joblib")

model = load_model()

# Streamlit UI for Price Prediction
st.title("Airbnb Rental Price Prediction App")
st.write("This tool predicts the price of an Airbnb listing based on the property details.")

st.subheader("Enter the listing details:")

# Collect user input
room_type = st.selectbox("Room Type", ["Entire home/apt", "Private room", "Shared room"])
accommodates = st.number_input("Accommodates (Number of guests)", min_value=1, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, step=1, value=2)
cancellation_policy = st.selectbox("Cancellation Policy (kind of cancellation policy)", ["strict", "flexible", "moderate"])
cleaning_fee = st.selectbox("Cleaning Fee Charged?", ["True", "False"])
instant_bookable = st.selectbox("Instantly Bookable?", ["False", "True"])
review_scores_rating = st.number_input("Review Score Rating", min_value=0.0, max_value=100.0, step=1.0, value=90.0)
bedrooms = st.number_input("Bedrooms", min_value=0, step=1, value=1)
beds = st.number_input("Beds", min_value=0, step=1, value=1)

# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'room_type': room_type,
    'accommodates': accommodates,
    'bathrooms': bathrooms,
    'cancellation_policy': cancellation_policy,
    'cleaning_fee': cleaning_fee,
    'instant_bookable': 'f' if instant_bookable=="False" else "t",
    'review_scores_rating': review_scores_rating,
    'bedrooms': bedrooms,
    'beds': beds
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write(f"The predicted price of the rental property is ${np.exp(prediction)[0]:.2f}.")
