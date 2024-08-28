import streamlit as st
import requests

# Streamlit app title
st.title("Player Value Cluster Prediction")

# Input fields for player data
appearance = st.number_input("Appearance", min_value=0)
goals = st.number_input("Goals", min_value=0)
assists = st.number_input("Assists", min_value=0)
minutes_played = st.number_input("Minutes Played", min_value=0.0)
age = st.number_input("Age", min_value=0)
award = st.number_input("Award", min_value=0)

# Button to trigger prediction
if st.button("Predict Cluster"):
    # Prepare data for API request
    data = {
        "appearance": appearance,
        "goals": goals,
        "assists": assists,
        "minutes_played": minutes_played,
        "age": age,
        "award": award
    }
    
    # Send POST request to FastAPI
    response = requests.post("http://127.0.0.1:8000/predict-cluster/", json=data)
    
    # Parse and display the result
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Cluster: {result['predicted_cluster']}")
    else:
        st.error("Error in prediction. Please try again.")
