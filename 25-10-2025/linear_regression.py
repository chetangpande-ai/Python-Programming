from sklearn.linear_model import LinearRegression
import numpy as np

# Sample features and labels
X = np.array([[1000], [1500], [2000], [2500], [3000]])
y = np.array([300000, 450000, 600000, 750000, 900000])

# Model training
model = LinearRegression()
model.fit(X, y)

# Prediction
print(model.predict(np.array([[2200]])))
