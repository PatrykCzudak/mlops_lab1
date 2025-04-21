from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict

app = FastAPI(title="Iris Classification API")

@app.get("/", response_class=FileResponse)
def get_ui():
    return "static/index.html"

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def health():
    return {"status": "ok"}

model = load_model("model.joblib")

@app.post("/predict", response_model=PredictResponse)
def predict_endpoint(request: PredictRequest):
    prediction = predict(model, request.dict())
    return PredictResponse(prediction=prediction)
