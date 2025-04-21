from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict

app = FastAPI(title="Iris Classification API")

# 1×: załaduj model raz przy starcie
model = load_model("model.joblib")

@app.get("/")
def root():
    return {"message": "Welcome to the Iris ML API"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest):
    prediction = predict(model, request.dict())
    return PredictResponse(prediction=prediction)