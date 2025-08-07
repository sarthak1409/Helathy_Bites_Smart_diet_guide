# 📊 Dataset Analysis: Indian Food Nutrition

The dataset contains nutritional values for various Indian dishes and has been used to train a classification model.

## 🔍 Features Selected
- Calories (kcal)
- Carbohydrates (g)
- Protein (g)
- Free Sugar (g)
- Fibre (g)
- Sodium (mg)
- Calcium (mg)
- Iron (mg)
- Vitamin C (mg)
- Folate (µg)

## 💡 Insights

- Dishes high in protein and fiber with low sugar and sodium tend to be classified as **Healthy**.
- Popular unhealthy dishes tend to have higher sugar and saturated fats.
- We used MinMaxScaler and a classification model (e.g. RandomForest or similar) trained on these features.