import streamlit as st
import requests
import pandas as pd
import time
import base64

API_URL = "https://helathy-bites-smart-diet-guide-1.onrender.com/"

st.set_page_config(page_title="Healthy Bytes: Smart Diet Guide", page_icon="🥗", layout="wide")

def add_bg_from_local(image_file):
    with open(image_file, "rb") as file:
        encoded_image = base64.b64encode(file.read()).decode()
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: url("data:image/jpg;base64,{encoded_image}") no-repeat center center fixed;
                background-size: cover;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("images/main_image.jpg")

with st.sidebar:
    st.title("📌 About This Project")
    st.info("🎯 Healthy Bytes: Smart Diet Guide")
    st.markdown("""
    ### 🎯 Project Details
    **Name:** Healthy Bytes: Smart Diet Guide  
    **Purpose:**  
    - Predict if a dish is *Healthy*, *Moderate*, or *Unhealthy*  
    - Recommend dishes based on **labels** or **health goals**  

    **Features:**  
    ✅ Predict dish health category  
    ✅ Recommend by health label  
    ✅ Recommend by nutritional goals  

    ---
    ⚠️ *For educational purposes only*
    """)

st.markdown("""
    <style>
        .main-title {
            text-align: center;
            font-size: 55px;
            color: #4B3F72;
            font-weight: bold;
            padding: 10px 0;
            backdrop-filter: blur(4px);
        }
        .sub-title {
            text-align: center;
            font-size: 35px;
            color: #2A2A72;
            padding: 5px 0;
            backdrop-filter: blur(4px);
            font-weight: bold;
        }
        h2 {
            text-align: center;
            color: #333333 !important;
            font-weight: 700;
            border-bottom: 2px solid #ccc;
            padding-bottom: 8px;
            margin-bottom: 20px;
        }
        label, div[data-testid="stFormLabel"] > label {
            color: #333333 !important;
            font-weight: 600;
        }
        .stSpinner > div > div {
            font-size: 20px !important;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            color: #000000 !important;
        }
        .alert {
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            margin: 15px auto;
            text-align: center;
            max-width: 600px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .success { background: #d4edda; color: #155724; border: 2px solid #c3e6cb; }
        .warning { background: #fff3cd; color: #856404; border: 2px solid #ffeeba; }
        .error { background: #f8d7da; color: #721c24; border: 2px solid #f5c6cb; }
        .stTabs [role="tablist"] button {
            width: 100% !important;
            background: linear-gradient(45deg, #3498db, #2ecc71) !important;
            color: white !important;
            font-size: 20px;
            font-weight: bold;
            border-radius: 10px;
            margin: 4px;
            transition: all 0.3s ease-in-out;
        }
        .stTabs [role="tablist"] button:hover {
            transform: scale(1.05);
            filter: brightness(1.15);
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2);
        }
        .stTabs [role="tablist"] button[aria-selected="true"] {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }
        div.stButton > button {
            display: block;
            margin: 15px auto;
            background: linear-gradient(45deg, #3498db, #2ecc71);
            color: white;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            padding: 12px 24px;
            transition: 0.3s;
        }
        div.stButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(45deg, #2ecc71, #3498db);
        }
        .badge {
            text-align: center;
            font-size: 28px;
            font-weight: bold;
            color: white;
            padding: 12px;
            border-radius: 10px;
            width: 50%;
            margin: auto;
            animation: fadeIn 1s ease-in-out;
        }
        .center-table {
            display: flex;
            justify-content: center;
            animation: fadeIn 1s ease-in-out;
        }
        .center-download {
            display: flex;
            justify-content: center;
            margin-top: 10px;
            animation: fadeIn 1s ease-in-out;
        }
        div[data-testid="stSelectbox"], 
        div[data-testid="stTextInput"], 
        div[data-testid="stSlider"], 
        div[data-testid="stNumberInput"] {
            max-width: 400px;
            margin: 10px auto;
        }
        h3.center-text {
            text-align: center;
            color: #333333;
            animation: fadeIn 1s ease-in-out;
        }
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>🥗 Healthy Bytes: Smart Diet Guide</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Your AI-powered Health Assistant</div>", unsafe_allow_html=True)
st.markdown("---")

tabs = st.tabs(["🔍 Predict Dish Health", "🥦 Recommend by Label", "🎯 Recommend by Goals"])

with tabs[0]:
    st.markdown("<h2>🔍 Predict Dish Health</h2>", unsafe_allow_html=True)
    dish_name = st.text_input("Enter Dish Name", placeholder="e.g., Rasmalai, Jeera Rice")

    if st.button("Predict Health Category", key="predict_btn"):
        if dish_name.strip():
            with st.spinner("🔍 Wait For Some Seconds"):
                st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>🔍 Step 1: Checking dish name...</p>", unsafe_allow_html=True)
                time.sleep(1.5)
                st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>⚙️ Step 2: Fetching data from model...</p>", unsafe_allow_html=True)
                time.sleep(1.5)
                st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>📊 Step 3: Preparing prediction...</p>", unsafe_allow_html=True)
                time.sleep(1)

            response = requests.get(f"{API_URL}/predict", params={"dish": dish_name})
            result = response.json()

            if result["status"] == "success":
                st.markdown(f"<h3 class='center-text'>✅ Dish: <b>{result['dish']}</b></h3>", unsafe_allow_html=True)
                badge_color = {
                    "Healthy": "#27ae60",
                    "Moderate": "#f39c12",
                    "Unhealthy": "#e74c3c"
                }.get(result['predicted_category'], "#7f8c8d")
                st.markdown(f"<div class='badge' style='background:{badge_color};'>Predicted: {result['predicted_category']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='alert error'><span style='color:#333'>{result['message']}</span></div>", unsafe_allow_html=True)
                if "suggestions" in result and result["suggestions"]:
                    st.markdown(f"<div class='alert warning'><span style='color:#333'>💡 Did you mean: {', '.join(result['suggestions'])}</span></div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='alert warning'><span style='color:#333'>⚠️ Please enter a dish name.</span></div>", unsafe_allow_html=True)

with tabs[1]:
    st.markdown("<h2>🥦 Recommend Dishes by Health Label</h2>", unsafe_allow_html=True)
    label = st.selectbox("Select Health Label", ["Healthy", "Moderate", "Unhealthy"])
    top_n = st.slider("Number of Recommendations", 1, 10, 5, key="label_slider")

    if st.button("Get Recommendations", key="label_btn"):
        with st.spinner("🔄 Wait For Some Seconds"):
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>🔄 Step 1: Validating label...</p>", unsafe_allow_html=True)
            time.sleep(1.5)
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>📦 Step 2: Loading recommendations...</p>", unsafe_allow_html=True)
            time.sleep(1.5)
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>📄 Step 3: Formatting data...</p>", unsafe_allow_html=True)
            time.sleep(1)

        response = requests.get(f"{API_URL}/recommend_by_label", params={"label": label, "top_n": top_n})
        result = response.json()

        if result["status"] == "success":
            st.markdown(f"<h3 class='center-text'>✅ Top {top_n} {label} Dishes</h3>", unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(result["selected"]))
            st.download_button("📥 Download CSV", pd.DataFrame(result["selected"]).to_csv(index=False), "recommendations_label.csv", "text/csv")

            if "alternatives" in result:
                st.markdown("<h3 class='center-text'>💡 Healthy Alternatives</h3>", unsafe_allow_html=True)
                st.dataframe(pd.DataFrame(result["alternatives"]))
        else:
            st.markdown(f"<div class='alert error'><span style='color:#333'>{result['message']}</span></div>", unsafe_allow_html=True)

with tabs[2]:
    st.markdown("<h2>🎯 Personalized Recommendations</h2>", unsafe_allow_html=True)

    st.markdown("### 🧾 Suggested Goal Ranges")
    goal_ranges_df = pd.DataFrame({
        "Health Preference": ["Healthy", "Moderate", "Unhealthy"],
        "Max Calories (kcal)": [500, 800, 1200],
        "Min Protein (g)": [20, 10, 0],
        "Max Sugar (g)": [5, 15, 30]
    })
    st.dataframe(goal_ranges_df, use_container_width=True)

    health_pref = st.selectbox("Health Preference", ["any", "Healthy", "Moderate", "Unhealthy"])
    max_calories = st.number_input("Max Calories (kcal)", min_value=0.0, step=1.0)
    min_protein = st.number_input("Min Protein (g)", min_value=0.0, step=0.1)
    max_sugar = st.number_input("Max Sugar (g)", min_value=0.0, step=0.1)
    top_n_goals = st.slider("Number of Recommendations", 1, 10, 5, key="goal_slider")

    if st.button("Get Goal-Based Recommendations", key="goal_btn"):
        with st.spinner("⚙️ Wait For Some Seconds"):
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>⚙️ Step 1: Reading your preferences...</p>", unsafe_allow_html=True)
            time.sleep(1.5)
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>📊 Step 2: Filtering dishes...</p>", unsafe_allow_html=True)
            time.sleep(1.5)
            st.markdown("<p style='text-align:center; color: black; font-weight:bold;'>✨ Step 3: Finalizing recommendations...</p>", unsafe_allow_html=True)
            time.sleep(1)

        params = {
            "health_pref": health_pref,
            "max_calories": max_calories if max_calories > 0 else None,
            "min_protein": min_protein if min_protein > 0 else None,
            "max_sugar": max_sugar if max_sugar > 0 else None,
            "top_n": top_n_goals
        }
        response = requests.get(f"{API_URL}/recommend_by_goals", params=params)
        result = response.json()

        if result["status"] == "success":
            st.markdown("<h3 class='center-text'>✅ Recommended Dishes</h3>", unsafe_allow_html=True)
            st.dataframe(pd.DataFrame(result["recommendations"]))
            st.download_button("📥 Download CSV", pd.DataFrame(result["recommendations"]).to_csv(index=False), "recommendations_goals.csv", "text/csv")
        else:
            st.markdown(f"<div class='alert error'><span style='color:#333'>{result['message']}</span></div>", unsafe_allow_html=True)