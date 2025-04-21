import joblib
import numpy as np
from sklearn.base import BaseEstimator

def load_model(path="model.joblib") -> BaseEstimator:
    model = joblib.load(path)
    print(f"Model loaded from {path}")
    return model

def predict(model, features: dict) -> str:
    arr = np.array([[
        features["sepal_length"],
        features["sepal_width"],
        features["petal_length"],
        features["petal_width"],
    ]])
    pred_index = model.predict(arr)[0]
    target_names = ["setosa", "versicolor", "virginica"]
    return target_names[pred_index]