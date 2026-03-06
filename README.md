# Phishing Website Detection (Machine Learning)

This project demonstrates a simple machine learning approach to classify URLs as **phishing** or **legitimate** using basic URL features.

## Features Used
- URL length
- Number of dots in the URL
- Number of hyphens in the URL
- Whether HTTPS is used

## Technologies
- Python
- Pandas
- Scikit-learn
- NumPy

## Project Structure
phishing-website-detection-ml
│
├── phishing.csv
├── train_model.py
├── predict.py
├── model.pkl
├── requirements.txt
└── README.md

## How It Works
1. `train_model.py` trains a Random Forest model using the dataset.
2. The trained model is saved as `model.pkl`.
3. `predict.py` loads the saved model and predicts whether a URL is phishing or legitimate.

## How to Run

HEAD
Step 1: Install required libraries
pip install -r requirements.txt

Step 2: Train the model
python train_model.py

Step 3: Run prediction
python predict.py

The model will output whether the URL is **Phishing** or **Legitimate**.

Example Output

Model Accuracy: 1.0
This URL is predicted as: Phishing

## Purpose
This project was created as part of academic learning to understand the basics of machine learning model training and prediction using Python.


