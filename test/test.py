import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("weight-height.csv")

# ---------------- Data Cleaning ----------------
# 1. Column names strip (remove spaces)
data.columns = data.columns.str.strip()

# 2. Drop duplicates
data = data.drop_duplicates()

# 3. Drop missing values
data = data.dropna()

# 4. Remove unrealistic values
# Remove unrealistic values for inches and pounds
data = data[(data['Height'] > 50) & (data['Height'] < 90)]   # Height in inches
data = data[(data['Weight'] > 50) & (data['Weight'] < 400)]  # Weight in pounds



print("Cleaned Data Shape:", data.shape)
print(data.head())

# ---------------- Model Training ----------------
# Only using Height as feature
X = data[['Height']]   # Feature
y = data['Weight']     # Target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# ---------------- Prediction ----------------
height = [[172]]  # Example input
predicted_weight = model.predict(height)
print(f"Predicted Weight for Height 172 cm: {predicted_weight[0]:.2f} kg")

# ---------------- Visualization ----------------
plt.figure(figsize=(8, 5))
plt.scatter(data['Height'], data['Weight'], c=data['Gender'].map({'Male':'blue','Female':'pink'}), alpha=0.6, label="Data")
plt.plot(data['Height'], model.predict(data[['Height']]), color="red", label="Best Fit Line")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.legend()
plt.show()
