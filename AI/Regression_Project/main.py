
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load the dataset
data = pd.read_csv("StudentsPerformance.csv")

# 2. Separate input features and target
X = data.drop(columns=["math score"])
y = data["math score"]

# 3. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# 4. Identify categorical and numerical columns
categorical_columns = X.select_dtypes(
    include=["str", "object", "category"]
).columns.tolist()

numerical_columns = X.select_dtypes(
    include=["number"]
).columns.tolist()

# 5. Prepare preprocesssing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_columns
        ),
        (
            "numerical",
            "passthrough",
            numerical_columns
        )
    ]
)

# 6. Create the complete machine learning pipeline
model = Pipeline(
    steps=[
        ("preprocessing", preprocessor),
        ("regression", LinearRegression())
    ]
)

# 7. Train the model
model.fit(X_train, y_train)

print("Model training completed successfully!")

# 8. Predict math scores for the test data
y_pred = model.predict(X_test)

print("\nFirst 10 actual math scores:")
print(y_test.head(10).to_list())

print("\nFirst 10 predicted math scores:")
print(y_pred[:10].round(2))




# 9. Evaluate model performance
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Model Evaluation ---")
print("Mean Absolute Error (MAE):", round(mae, 2))
print("Mean Squared Error (MSE):", round(mse, 2))
print("R2 Score:", round(r2, 4))
print("R2 Percentage:", round(r2 * 100, 2), "%")





# 10. Predict the math score for a new student

new_student = pd.DataFrame([{
    "gender": "female",
    "race/ethnicity": "group B",
    "parental level of education": "bachelor's degree",
    "lunch": "standard",
    "test preparation course": "completed",
    "reading score": 75,
    "writing score": 80
}])

predicted_score = model.predict(new_student)[0]

print("\n--- New Student Prediction ---")
print("Reading score: 75")
print("Writing score: 80")
print("Predicted math score:", round(predicted_score, 2))
