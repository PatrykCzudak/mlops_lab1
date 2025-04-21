from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

def load_data():
    data = load_iris(as_frame=True)
    X = data.data
    y = data.target
    return X, y

def train_model(X, y):
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model

def save_model(model, path="model.joblib"):
    joblib.dump(model, path)
    print(f"Model saved to {path}")

if __name__ == "__main__":
    X, y = load_data()
    model = train_model(X, y)
    save_model(model)