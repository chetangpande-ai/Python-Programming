import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import joblib # Library for saving and loading the model

# Define the filename for the saved model
MODEL_FILENAME = '01-12-2025/naive_bayes_purchase_predictor.pkl'

# =============================================================================
# --- PART 1: DATA PREPARATION AND SPLITTING ---
# =============================================================================
print("--- Part 1: Data Preparation ---")

# 1. Create Dummy Data
# Scenario: Classifying user purchase intent (1=Yes, 0=No) based on Age and Salary.
data = {
    'Age': [25, 30, 35, 40, 45, 22, 50, 60, 28, 42],
    'EstimatedSalary': [30000, 45000, 60000, 80000, 100000, 25000, 110000, 150000, 40000, 95000],
    'Purchased': [0, 0, 0, 0, 1, 0, 1, 1, 0, 1]
}
df = pd.DataFrame(data)

# Separate features (X) and target (y)
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# 2. Split the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print("Data loaded and split into training/testing sets.")
print("-" * 50)

# =============================================================================
# --- PART 2: MODEL TRAINING AND EVALUATION ---
# =============================================================================
print("--- Part 2: Model Training and Evaluation ---")

# 3. Build and Train the Naive Bayes Model
model = GaussianNB()
model.fit(X_train, y_train)

print("Gaussian Naive Bayes Model Training Complete.")

# 4. Evaluate the Model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy on Test Data: {accuracy * 100:.2f}%")
print("-" * 50)

# =============================================================================
# --- PART 3: PERSISTENCE (SAVING AND LOADING) ---
# =============================================================================
print("--- Part 3: Model Persistence (Saving/Loading) ---")

# 5. Save the Trained Model (.pkl file)
joblib.dump(model, MODEL_FILENAME)
print(f"✅ Model successfully saved to disk as: {MODEL_FILENAME}")

# 6. Load the Model from the .pkl file
# We load it into a new variable (loaded_model) to simulate loading it in a future script/app.
loaded_model = joblib.load(MODEL_FILENAME)
print(f"✅ Model successfully loaded from disk.")
print("-" * 50)

# =============================================================================
# --- PART 4: END-TO-END USAGE (PREDICTING WITH THE LOADED MODEL) ---
# =============================================================================
print("--- Part 4: End-to-End Prediction Test ---")

# 7. Define New, Unseen Data
new_user_data = pd.DataFrame({'Age': [38], 'EstimatedSalary': [75000]})

# 8. Predict using the LOADED model
prediction = loaded_model.predict(new_user_data)
prediction_proba = loaded_model.predict_proba(new_user_data)

print(f"Prediction using the loaded model for Age: 38, Salary: 75000:")
print(f"  Predicted Class (0=No, 1=Yes): {prediction[0]}")
print(f"  Probability of No Purchase (Class 0): {prediction_proba[0][0]:.4f}")
print(f"  Probability of Yes Purchase (Class 1): {prediction_proba[0][1]:.4f}")