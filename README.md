# Fraud Detection System

## Overview
This repository contains a machine learning system designed to detect fraudulent financial transactions. The project includes data analysis, model training, and a Streamlit web application for making real-time predictions.

## Dataset
The system is trained on a large financial transaction dataset (`AIML Dataset.csv`) from Kaggle containing over 6.3 million records with the following features:
- Transaction step (time)
- Transaction type (CASH_OUT, TRANSFER, CASH_IN, DEPOSIT, PAYMENT)
- Transaction amount
- Origin account information
- Destination account information
- Fraud labels

## Project Structure
- `analysis_model.ipynb`: Jupyter notebook containing exploratory data analysis and model development
- `fraud_detection.py`: Streamlit web application for making fraud predictions
- `fraud_detection_pipeline.pkl`: Serialized machine learning pipeline
- `AIML Dataset.csv`: Dataset used for training (471MB)

## Key Findings
- Only 0.13% of transactions in the dataset are fraudulent
- Fraudulent transactions primarily occur in TRANSFER and CASH_OUT transaction types
- The model identified patterns where accounts are emptied (balance becomes zero) after fraudulent transfers
- Features like transaction type, amount, and balance changes are strong predictors of fraud

## Model
The system uses a Logistic Regression classifier with:
- Preprocessing pipeline for numeric and categorical features
- Class balancing to handle the highly imbalanced dataset
- Evaluation metrics focused on fraud detection capability

Performance metrics:
- 94% recall for detecting fraudulent transactions
- 95% overall accuracy

## Web Application
The Streamlit application allows users to:
- Input transaction details (type, amount, balances)
- Get immediate predictions on whether a transaction is likely fraudulent
- View prediction results with visual indicators

## How to Run

### Prerequisites
- Python 3.x
- Required packages: pandas, numpy, matplotlib, seaborn, scikit-learn, streamlit, joblib

### Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/fraud-detection-system.git
cd fraud-detection-system

# Install dependencies
pip install -r requirements.txt
```

### Running the Application
```bash
streamlit run fraud_detection.py
```

### Retraining the Model
To retrain the model or explore the data analysis:
```bash
jupyter notebook analysis_model.ipynb
```

## Future Improvements
- Implement more sophisticated models (Random Forest, XGBoost)
- Add feature engineering for better fraud detection
- Implement real-time monitoring capabilities
- Add model explanation features for transparency # Fraud-Detection-System
