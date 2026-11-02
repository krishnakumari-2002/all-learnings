from sklearn.tree import DecisionTreeClassifier

# 6 known fruits: [weight in grams, skin (1 = smooth, 0 = bumpy)]
fruits = [
    [150, 1],
    [170, 1],
    [160, 1],
    [140, 0],
    [130, 0],
    [150, 0],
]

# The correct name of each fruit (labels)
names = ["Apple", "Apple", "Apple", "Orange", "Orange", "Orange"]

# Create the model
model = DecisionTreeClassifier(random_state=0)

# Learn from the fruits AND their names
model.fit(fruits, names)

# Predict for 2 new fruits
new_fruits = [[155, 1], [135, 0]]
print("Predictions:", model.predict(new_fruits))