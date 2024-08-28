import streamlit as st
import requests

# Cluster descriptions
cluster_descriptions = {
    0: "Players with moderate current_value",
    1: "High-value players",
    2: "Low-value players",
    3: "Elite players",
    4: "Lower-value players",
    5: "Above-average players"
}

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
        cluster_number = result['predicted_cluster']
        cluster_description = cluster_descriptions.get(cluster_number, "Unknown cluster")
        st.success(f"Predicted Cluster: {cluster_number} - {cluster_description}")
    else:
        st.error("Error in prediction. Please try again.")
