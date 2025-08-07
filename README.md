# 🥗 Smart Food Recommendation System

This is an AI-powered system that helps users make informed food choices by predicting the healthiness of Indian dishes and recommending alternatives based on health goals.

## 🚀 Features

- Predicts health category: Healthy, Moderate, Unhealthy
- Recommends dishes based on health label
- Personalized recommendations using nutritional filters
- Built using FastAPI (backend) and Streamlit (frontend)
- Includes animated, styled UI with CSV export and health badges

## 📂 Project Structure

```
smart_food_project/
│
├── app/                        # FastAPI and Streamlit app logic
├── dataset/                   # Processed CSV dataset used for training and prediction
├── artifacts/                 # Trained ML model and scaler files
├── requirements.txt           # Python dependencies
├── README.md                  # Project overview
├── ANALYSIS.md                # Dataset analysis and insights
├── LICENSE                    # License file
├── .gitignore                 # Files and folders to ignore in Git
└── dataset_README.txt         # Dataset source and copyright info
```

## 📊 Dataset

- Source: [Kaggle - Indian Food Nutrition](https://www.kaggle.com/datasets)
- Fields include: Calories, Protein, Sugar, Fiber, Vitamins, etc.

## 📦 Installation

```bash
git clone https://github.com/yourusername/smart-food-recommendation.git
cd smart-food-recommendation
pip install -r requirements.txt
```

## ▶️ Running the App

```bash
# Run API backend
uvicorn main:app --reload

# In another terminal, run the frontend
streamlit run app.py
```

## 📄 License

MIT License. Dataset credit: Kaggle.
© 2025 Sarthak Maddi.