import pickle
import numpy as np

def get_model():
    with open ("lgbm_model.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    return loaded_model

def get_prediction(data):
    model = get_model()
    pred_class = model.predict(data)[0]
    pred_prob = list(model.predict_proba(data)[:,1])[0]
    return{
        "class" : pred_class,
        "probability" : pred_prob
    }