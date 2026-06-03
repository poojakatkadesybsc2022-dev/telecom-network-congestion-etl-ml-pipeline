# Telecom Network Congestion Prediction using ETL Pipeline and Machine Learning

## Project Overview

This project demonstrates an end-to-end ETL pipeline and machine learning workflow for predicting telecom network congestion.

The pipeline extracts raw telecom network data from MySQL, performs data cleaning and feature engineering using Python, trains a Random Forest classification model, and loads prediction results back into MySQL.

---

## Tech Stack

- Python
- Pandas
- MySQL
- SQLAlchemy
- PyMySQL
- Scikit-Learn

---

## Dataset Features

- timestamp
- tower_id
- users_connected
- download_speed
- upload_speed
- latency
- weather
- congestion

---

## ETL Workflow

### Extract
- Imported telecom network data from MySQL
- Loaded data into Pandas DataFrame

### Transform
- Missing value validation
- Duplicate record validation
- Datetime conversion
- Feature engineering
- Weather encoding

### Load
- Stored transformed data into MySQL
- Stored prediction results into MySQL

---

## Machine Learning

Model Used:
- Random Forest Classifier

Train-Test Split:
- 80% Training
- 20% Testing

Model Accuracy:
- 99.86%

---

## Feature Importance Analysis

| Feature | Importance |
|----------|----------|
| Users Connected | 44.87% |
| Latency | 43.76% |
| Download Speed | 2.95% |
| Upload Speed | 2.42% |
| Hour | 1.79% |
| Day | 1.74% |
| Weather | 0.88% |

---

## Business Insights

- Network congestion is primarily driven by the number of connected users.
- High latency significantly increases the probability of congestion.
- Weather conditions have minimal impact on congestion prediction.
- The model can help telecom operators proactively identify congestion risks.

---

## Project Results

- Total Records Processed: 3605
- Predictions Generated: 721
- Model Accuracy: 99.86%
