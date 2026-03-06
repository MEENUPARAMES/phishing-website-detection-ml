import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Function to extract features from URL
def extract_features(url):
    url_length = len(url)
    num_dots = url.count(".")
    num_hyphen = url.count("-")
    https = 1 if url.startswith("https") else 0
    
    return [url_length, num_dots, num_hyphen, https]

# Take URL input from user
url = input("Enter a URL to check: ")

features = extract_features(url)

prediction = model.predict([features])

if prediction[0] == 1:
    print("Result: This URL is PHISHING")
else:
    print("Result: This URL is LEGITIMATE")
