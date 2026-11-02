
from sklearn.linear_model import LinearRegression

# Input: years of experience
X = [[1], [2], [3], [4], [5]]

# Output: salary in lakhs7
y = [2, 3, 4, 5, 6]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict salary for 3.5 years of experience
prediction = model.predict([[3.5]])

print("Predicted salary:", prediction[0], "lakhs")
