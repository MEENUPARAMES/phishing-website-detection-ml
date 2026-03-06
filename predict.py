import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Example URL features
# url_length, num_dots, num_hyphens, has_https
sample_url = np.array([[90, 4, 2, 0]])

# Predict
prediction = model.predict(sample_url)

# Print result
if prediction[0] == 1:
    print("This URL is predicted as: Phishing")
else:
    print("This URL is predicted as: Legitimate")
