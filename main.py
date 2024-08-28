from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load the models
pca = joblib.load('pca_model.joblib')
kmeans = joblib.load('kmeans_model.joblib')

app = FastAPI()

# test 
@app.get("/")
def root():
    return {"message": "Hi there, check out my first model deployemnt ;) "}

# data model for incoming requests
class PlayerData(BaseModel):
    appearance: int
    goals: int
    assists: int
    minutes_played: float
    age: int
    award: int

@app.post("/predict-cluster/")
def predict_cluster(player_data: PlayerData):
    # extracting data from request and convert it to a numpy array
    data = np.array([[player_data.appearance, 
                      player_data.goals, 
                      player_data.assists, 
                      player_data.minutes_played, 
                      player_data.age, 
                      player_data.award]])
    
    # transform data using PCA
    data_pca = pca.transform(data)
    # predict the cluster
    cluster = kmeans.predict(data_pca)
    # return the cluster as a response
    return {"predicted_cluster": int(cluster[0])}

# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# what does the prediction cluster number mean?
# Cluster 0: Players with moderate current_value
# Cluster 1: High-value players
# Cluster 2: Low-value
# Cluster 3: Elite players
# Cluster 4: Lower-value players
# Cluster 5: Above-average players 