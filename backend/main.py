from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}

@app.get("/predict")
def predict(hours: int):

    if hours > 5:
        return {"result": "Pass ✅"}

    return {"result": "Fail ❌"}