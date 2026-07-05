import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
data = pd.read_csv("data/housing.csv")

# Features and Target
X = data[['area', 'bedrooms', 'bathrooms']]
y = data['price']

# Train Model
model = LinearRegression()
model.fit(X, y)

# Create model folder if not exists
os.makedirs("model", exist_ok=True)

# Save Model
joblib.dump(model, "model/house_model.pkl")

print("✅ Model trained successfully!")
print("✅ Saved as model/house_model.pkl")