from fastapi import FastAPI, Query
from app.predict_helper import predict_dish_health, recommend_with_alternatives, recommend_by_goals

app = FastAPI(
    title="Smart Food Recommendation API",
    description="API for predicting health category and recommending dishes based on nutrition & goals",
    version="1.0"
)

@app.get("/")
def home():
    return {"message": "Welcome to Smart Food Recommendation API"}

@app.get("/predict")
def predict(dish: str = Query(..., description="Dish name to predict health category")):
    """
    Predict health category (Healthy, Moderate, Unhealthy) for a given dish name.
    """
    return predict_dish_health(dish)

@app.get("/recommend_by_label")
def recommend_by_label(
    label: str = Query(..., description="Health label: Healthy, Moderate, or Unhealthy"),
    top_n: int = Query(5, description="Number of dishes to return")
):
    """
    Recommend dishes based on a given health label and suggest healthy alternatives.
    """
    return recommend_with_alternatives(label, top_n)

@app.get("/recommend_by_goals")
def recommend_goals_endpoint(
    health_pref: str = Query("any", description="Health preference: Healthy, Moderate, Unhealthy or any"),
    max_calories: float = Query(None, description="Maximum calories (kcal)"),
    min_protein: float = Query(None, description="Minimum protein (grams)"),
    max_sugar: float = Query(None, description="Maximum sugar (grams)"),
    top_n: int = Query(5, description="Number of dishes to return")
):
    """
    Recommend dishes based on health preference and custom nutritional goals.
    """
    return recommend_by_goals(health_pref, max_calories, min_protein, max_sugar, top_n)

