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

## Example
Run:

