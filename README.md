# 📡 Telecom Network Congestion Prediction (End-to-End ETL + ML Pipeline)

## 🚀 Project Overview

This project demonstrates an **end-to-end Data Engineering + Machine Learning pipeline** for predicting telecom network congestion using real-world inspired network metrics.

The system extracts data from MySQL, performs data cleaning & feature engineering in Python, trains a Machine Learning model, and stores predictions back into MySQL for analytics and dashboarding.

---

## ⚙️ Architecture

**MySQL → Python ETL → Feature Engineering → ML Model → Predictions → MySQL → Power BI Dashboard**

---

## 🛠️ Tech Stack

- Python
- Pandas, NumPy
- MySQL
- SQLAlchemy, PyMySQL
- Scikit-learn
- Power BI (Visualization)

---

## 📊 Dataset Features

- timestamp
- tower_id
- users_connected
- download_speed
- upload_speed
- latency
- weather
- congestion (Target Variable)

---

## 🔄 ETL Pipeline

### Extract
- Data pulled from MySQL database

### Transform
- Missing value handling
- Duplicate removal
- Timestamp feature extraction (hour, day, month, weekday)
- Weather encoding
- Feature engineering

### Load
- Cleaned dataset stored back into MySQL
- ML predictions stored in `network_predictions` table

---

## 🤖 Machine Learning Model

- Algorithm: Random Forest Classifier
- Train/Test Split: 80/20
- Accuracy: **99.86%**

---

## 📌 Key Insights

- Users connected and latency are the strongest predictors of congestion
- Weather has minimal impact on congestion
- Peak congestion observed during high traffic hours
- Model helps in proactive network optimization

---

## 📈 Power BI Dashboard

- KPI Cards (Users, Latency, Congestion Events)
- Congestion distribution by tower
- Hourly congestion trend
- Weather impact analysis
- Actual vs Predicted congestion comparison

---

## 📁 Project Structure

```
ETL_Telecom/
│
├── extract.py
├── transform.py
├── model.py
├── requirements.txt
├── README.md
```

---

## 🎯 Business Value

- Helps telecom operators predict congestion in advance
- Improves network resource allocation
- Reduces latency and improves user experience

---

## ⭐ Author

Data Engineering + ML Project built for portfolio demonstration
```
