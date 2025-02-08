

---

# 📌 **Flight Delay Prediction using Machine Learning**  

📊 **A machine learning model to predict airline arrival delays using a dataset of 4500 rows and 21 features.**  

## 📝 **Project Overview**  
This project aims to predict **flight arrival delays** using a **Random Forest Regressor**. It involves **data preprocessing, feature engineering, model training, and evaluation** to achieve high accuracy in delay predictions.  

## 📂 **Dataset Information**  
- **Source**: `Airline_Delay_Cause.csv`  
- **Size**: 4500 rows, 21 features  
- **Target Variable**: `arr_delay` (arrival delay in minutes)  
- **Features**: Various flight attributes affecting delays  

## ⚙️ **Technologies Used**  
✅ Python 🐍  
✅ Pandas 🏷️  
✅ Scikit-learn 🤖  
✅ Matplotlib & Seaborn 📊  
✅ Joblib 🗂️  
✅ **FastAPI** 🚀  

## 🌐 **API Deployment**  
The trained model is deployed using **FastAPI**. You can access the API and test predictions via:  

🔗 **[FastAPI Documentation](https://machine-learning-4-usey.onrender.com/docs)**  

## 📊 **Exploratory Data Analysis (EDA)**  
✔️ Data Cleaning (handling missing values, encoding categorical features)  
✔️ Feature Correlation Heatmap  
✔️ Arrival Delay Distribution Plot  

## 🚀 **Model Selection & Training**  
- **Algorithm Used**: `RandomForestRegressor(n_estimators=100, random_state=42)` 🌲  
- **Feature Scaling**: StandardScaler  
- **Data Split**: 80% training, 20% testing  

## 🎯 **Model Performance Metrics**  
| Metric  | Value  |  
|---------|--------|  
| 📉 **RMSE** | `1685.14` |  
| 📊 **R² Score** | `0.9874` |  
| 📏 **MAE (Mean Absolute Error)** | `485.43` |  
| 🔄 **Cross-Validated RMSE** | `2858.48 ± 1366.38` |  

## 🔍 **Why is RMSE High?**  
The RMSE is **1685.14**, which is relatively high due to:  
- **Extreme values (outliers)**: Some flights have delays up to **37,080 minutes** ⏳  
- **Wide range of delays**: Many flights have minimal delays, while some are extremely delayed  
- **Inherent unpredictability**: Flight delays depend on various external factors like weather, mechanical issues, and air traffic  

### ✅ **Is the Model Performing Well?**  
Yes! Despite the **high RMSE**, the **R² score of 0.9874** shows that the model explains **98.74%** of the variance in flight delays, meaning it performs exceptionally well in predicting delays, except for extreme cases.  

## 📌 **How to Use the Model**  
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Beza-16/machine-learning.git  

```  
2️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt  
```  
3️⃣ **Run the Script**  
```bash
python main.py  
```  
4️⃣ **Model Output & Evaluation**  
- The model will **train on the dataset** and save:  
  - `flight_delay_model.pkl` (Trained Model)  
  - `scaler.pkl` (Feature Scaler)  
  - `label_encoders.pkl` (Encoded categorical features)  

## 📈 **Visualizations Included**  
📌 **Feature Importance Plot**  
📌 **Arrival Delay Distribution**  
📌 **Actual vs. Predicted Delay Scatter Plot**  

## 🔍 **Example Predictions**  
The model receives flight data and predicts whether a flight will be delayed.  

### ✈️ **Example 1: No Delay**  
**Input:**  
```json
{
    "year": 2023,
    "month": 8,
    "carrier": "9E",
    "carrier_name": "Endeavor Air Inc.",
    "airport": "CRW",
    "airport_name": "Charleston/Dunbar, WV: West Virginia International Yeager",
    "arr_flights": 5,
    "arr_del15": 0,
    "carrier_ct": 0.0,
    "weather_ct": 0.0,
    "nas_ct": 0.0,
    "security_ct": 0.0,
    "late_aircraft_ct": 0.0,
    "arr_cancelled": 0,
    "arr_diverted": 0,
    "arr_delay": 0,
    "carrier_delay": 0,
    "weather_delay": 0,
    "nas_delay": 0,
    "security_delay": 0,
    "late_aircraft_delay": 0
}
```
**Prediction Output:**  
```json
{
    "message": "Prediction received!",
    "delay": "No"
}
```

### ✈️ **Example 2: Delayed Flight**  
**Input:**  
```json
{
    "year": 2023,
    "month": 8,
    "carrier": "9E",
    "carrier_name": "Endeavor Air Inc.",
    "airport": "ABE",
    "airport_name": "Allentown/Bethlehem/Easton, PA: Lehigh Valley International",
    "arr_flights": 89,
    "arr_del15": 13,
    "carrier_ct": 2.25,
    "weather_ct": 1.6,
    "nas_ct": 3.16,
    "security_ct": 0.0,
    "late_aircraft_ct": 5.99,
    "arr_cancelled": 2,
    "arr_diverted": 1,
    "arr_delay": 1375,
    "carrier_delay": 71,
    "weather_delay": 761,
    "nas_delay": 118,
    "security_delay": 0,
    "late_aircraft_delay": 425
}
```
**Prediction Output:**  
```json
{
    "message": "Prediction received!",
    "delay": "Yes"
}
```

## 🔮 **Future Improvements**  
✔️ Handle outliers using transformations (e.g., log-scaling)  
✔️ Try advanced models like XGBoost or LSTM for better accuracy  
✔️ Improve model generalization using more training data  

## 💻 **Contributors**  
👤 **Bezawit Desalegn**  
📩 Contact: dbeza20@gmail.com  

🚀 **Project Repository**: [https://github.com/Beza-16/machine-learning.git]  

---

