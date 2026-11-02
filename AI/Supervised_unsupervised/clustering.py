from sklearn.cluster import KMeans

# 6 customers: [age, money spent]
customers = [
    [20, 100],
    [22, 120],
    [25, 110],
    [50, 900],
    [52, 950],
    [55, 880],
]

# Create the model: make 2 groups
# n_init=10      -> try 10 different random starts and keep the best
# random_state=0 -> make the random choices the same every run
model = KMeans(n_clusters=2, n_init=10, random_state=0)

# Learn the groups from the data
model.fit(customers)

# Show which group each customer belongs to
print("Groups:", model.labels_)

# Predict the group of a new customer
new_customer = [[23, 130]]
print("New customer group:", model.predict(new_customer))