import joblib
import json
import pandas as pd
from difflib import get_close_matches
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model = joblib.load(os.path.join(BASE_DIR, "artifacts", "best_model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "artifacts", "scaler.pkl"))

feature_list = ['calories', 'carbs', 'protein', 'sugar', 'fiber', 'sodium', 'calcium', 'iron', 'vitamin_c', 'folate']

dataset_path = os.path.join(BASE_DIR, "dataset", "Indian_Food_Nutrition_Processed.csv")
df = pd.read_csv(dataset_path)

rename_map = {
    'Dish Name': 'dish',
    'Calories (kcal)': 'calories',
    'Carbohydrates (g)': 'carbs',
    'Protein (g)': 'protein',
    'Fats (g)': 'fat',
    'Free Sugar (g)': 'sugar',
    'Fibre (g)': 'fiber',
    'Sodium (mg)': 'sodium',
    'Calcium (mg)': 'calcium',
    'Iron (mg)': 'iron',
    'Vitamin C (mg)': 'vitamin_c',
    'Folate (µg)': 'folate'
}
df.rename(columns=rename_map, inplace=True)

label_map = {0: "Unhealthy", 1: "Moderate", 2: "Healthy"}
label_map_text_to_num = {"unhealthy": 0, "moderate": 1, "healthy": 2}

def predict_dish_health(dish_name: str):
    dish_row = df[df['dish'].str.lower() == dish_name.lower()]

    if dish_row.empty:
        all_dishes = df['dish'].str.lower().tolist()
        close_matches = get_close_matches(dish_name.lower(), all_dishes, n=3, cutoff=0.4)
        return {
            "status": "error",
            "message": f"Dish '{dish_name}' not found",
            "suggestions": close_matches
        }

    features = dish_row[feature_list]
    features_scaled = scaler.transform(features)
    pred_label = model.predict(features_scaled)[0]

    return {
        "status": "success",
        "dish": dish_name,
        "predicted_category": label_map[pred_label]
    }

def recommend_with_alternatives(label: str, top_n: int = 5):
    if label.lower() not in label_map_text_to_num:
        return {"status": "error", "message": "Invalid label. Use Healthy, Moderate, or Unhealthy."}

    numeric_label = label_map_text_to_num[label.lower()]

    if 'health_label' not in df.columns:
        features = df[feature_list]
        features_scaled = scaler.transform(features)
        df['health_label'] = model.predict(features_scaled)

    selected_df = df[df['health_label'] == numeric_label]

    if selected_df.empty:
        return {"status": "error", "message": f"No dishes found for {label}."}

    selected_top = selected_df.sort_values(by='calories').head(top_n)
    response = {
        "status": "success",
        "selected": selected_top[['dish', 'calories', 'protein', 'sugar']].to_dict(orient='records')
    }

    if numeric_label != 2:
        healthy_df = df[df['health_label'] == 2]
        healthy_top = healthy_df.sort_values(by='calories').head(top_n)
        response["alternatives"] = healthy_top[['dish', 'calories', 'protein', 'sugar']].to_dict(orient='records')

    return response

def recommend_by_goals(health_pref: str = "any", max_calories: float = None, min_protein: float = None, max_sugar: float = None, top_n: int = 5):
    filtered_df = df.copy()

    if health_pref.lower() in label_map_text_to_num:
        filtered_df = filtered_df[filtered_df['health_label'] == label_map_text_to_num[health_pref.lower()]]

    if max_calories is not None:
        filtered_df = filtered_df[filtered_df['calories'] <= max_calories]
    if min_protein is not None:
        filtered_df = filtered_df[filtered_df['protein'] >= min_protein]
    if max_sugar is not None:
        filtered_df = filtered_df[filtered_df['sugar'] <= max_sugar]

    filtered_df = filtered_df.sort_values(by='calories').head(top_n)

    if filtered_df.empty:
        return {"status": "error", "message": "No dishes match your criteria."}

    return {
        "status": "success",
        "recommendations": filtered_df[['dish', 'calories', 'protein', 'sugar']].to_dict(orient='records')
    }
