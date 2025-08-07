# 🥗 Smart Food Recommendation System

An AI-powered system that helps users make informed food choices by predicting the healthiness category of Indian dishes and recommending smart alternatives based on nutritional goals.

---
### 📺 Demo Preview


[![Watch the demo](https://i.ytimg.com/vi/0e9u4apbOKs/hqdefault.jpg)](https://youtu.be/F2rR2-ECtck)

---

## 🚀 Key Features

- Predicts health category: **Healthy**, **Moderate**, **Unhealthy**  
- Recommend dishes from a chosen health label  
- Personalized recommendations based on nutritional filters (calories, protein, sugar)  
- Backend: **FastAPI** | Frontend: **Streamlit** with animation, styled UI, health badges, and CSV export  

---

## 📂 Project Structure

```
smart_food/
├── .gitignore
├── ANALYSIS.md
├── LICENSE
├── README.md
├── app.py
├── requirements.txt
├── notebook/
|   └──main.ipynb
├── images/
│   └── main_image.jpg
├── dataset/
│   ├── Indian_Food_Nutrition.csv
│   └── README.txt
├── artifacts/
│   ├── best_model.pkl
│   ├── feature_list.json
│   └── scaler.pkl
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── predict_helper.py
```

---

## 📊 Dataset Overview  

- **Source**: Kaggle – Indian Food Nutrition dataset  
- **Key Nutrient Fields**: calories, protein, sugar, fiber, sodium, iron, vitamin C, folate, etc.

---

## 📦 Installation & Setup

```bash
git clone https://github.com/sarthak1409/Helathy_Bites_Smart_diet_guide
cd Helathy_Bites_Smart_diet_guide
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. **FastAPI backend**  
   ```bash
   uvicorn app.main:app --reload
   ```

2. **Streamlit frontend** (in a separate terminal)  
   ```bash
   streamlit run app/frontend.py
   ```

---

## 📁 Deployment & Packaging

- `predict_helper.py` is used for serving prediction and recommendation routes in the FastAPI backend  
- You can containerize the app using **Docker** and orchestrate services using **docker-compose**

---

## 📄 License

- **MIT License**  
- Dataset credit: Kaggle  
- © 2025 Sarthak Maddi
