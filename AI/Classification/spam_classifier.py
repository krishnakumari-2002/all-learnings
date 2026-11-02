
import re
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


# ==================================================
# 1. LOAD THE DATASET
# ==================================================

print("Loading dataset...")

df = pd.read_csv("spam.csv", encoding="latin-1")

print("\nOriginal dataset shape:", df.shape)
print("Dataset columns:", df.columns.tolist())


# ==================================================
# 2. IDENTIFY THE MESSAGE AND LABEL COLUMNS
# ==================================================

# Support common column names used in spam datasets.

label_candidates = ["label", "category", "v1", "class", "target"]
message_candidates = ["message", "text", "sms", "v2", "email"]

label_column = next(
    (
        col for col in df.columns
        if col.strip().lower() in label_candidates
    ),
    None
)

message_column = next(
    (
        col for col in df.columns
        if col.strip().lower() in message_candidates
    ),
    None
)

# If the column names are different, use the first two columns.
if label_column is None or message_column is None:

    if len(df.columns) < 2:
        raise ValueError(
            "The CSV must contain message and label columns."
        )

    print("\nColumn names not recognized.")
    print("Using the first column as the label.")
    print("Using the second column as the message.")

    label_column = df.columns[0]
    message_column = df.columns[1]

# Keep only the required columns.
df = df[[label_column, message_column]].copy()

df.columns = ["label", "message"]


# ==================================================
# 3. DATA CLEANING
# ==================================================

# Remove rows with missing labels or messages.
df = df.dropna(subset=["label", "message"])

# Convert labels and messages to strings.
df["label"] = df["label"].astype(str).str.strip().str.lower()
df["message"] = df["message"].astype(str).str.strip()



# Keep only spam and ham labels.
df = df[df["label"].isin(["spam", "ham"])]

# Remove empty messages.
df = df[df["message"] != ""]

# Remove duplicate messages with the same label.
df = df.drop_duplicates(subset=["label", "message"])

# Ensure both classes are present.
if df["label"].nunique() != 2:
    raise ValueError(
        "The dataset must contain both 'spam' and 'ham' labels. "
        "Check your CSV label values."
    )

print("\nCleaned dataset shape:", df.shape)

print("\nNumber of messages in each class:")
print(df["label"].value_counts())


# ==================================================
# 4. TEXT PREPROCESSING
# ==================================================

def clean_text(text):
    """
    Clean a message before converting it into
    numerical features.
    """

    # Convert uppercase letters to lowercase.
    text = text.lower()

    # Remove URLs.
    text = re.sub(
        r"https?://\S+|www\.\S+",
        " ",
        text
    )

    # Remove email addresses.
    text = re.sub(
        r"\S+@\S+",
        " ",
        text
    )

    # Remove punctuation and special characters.
    # Keep letters, digits, and whitespace.
    text = re.sub(
        r"[^a-z0-9\s]",
        " ",
        text
    )

    # Replace repeated spaces with one space.
    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# Apply text preprocessing to every message.
df["clean_message"] = df["message"].apply(clean_text)

# Remove messages that become empty after cleaning.
df = df[df["clean_message"] != ""]

print("\nExample of text preprocessing:")

if not df.empty:
    print("Original:", df["message"].iloc[0])
    print("Cleaned :", df["clean_message"].iloc[0])


# ==================================================
# 5. SEPARATE INPUT FEATURES AND TARGET
# ==================================================

# X contains the message text.
X = df["clean_message"]

# y contains the expected category.
y = df["label"]

print("\nTotal messages:", len(df))
print("Input feature: Message text")
print("Target classes: spam and ham")


# ==================================================
# 6. SPLIT TRAINING AND TESTING DATA
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining messages:", len(X_train))
print("Testing messages:", len(X_test))


# ==================================================
# 7. TEXT VECTORIZATION AND MODEL TRAINING
# ==================================================

# TF-IDF converts text into numerical features.
# Multinomial Naive Bayes performs classification.
# Pipeline connects these two steps.

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=False,
            stop_words="english",
            max_features=5000
        )
    ),
    (
        "classifier",
        MultinomialNB()
    )
])

print("\nTraining the model...")

# Learn the vocabulary and train the classifier.
model.fit(X_train, y_train)

print("Model training completed successfully!")


# ==================================================
# 8. PREDICT TEST MESSAGES
# ==================================================

# Predict labels for messages not used during training.
y_pred = model.predict(X_test)


# ==================================================
# 9. MODEL PERFORMANCE METRICS
# ==================================================

accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    pos_label="spam",
    zero_division=0
)

print("\n" + "=" * 45)
print("MODEL PERFORMANCE")
print("=" * 45)

print(f"Accuracy : {accuracy:.4f} ({accuracy * 100:.2f}%)")
print(f"Precision: {precision:.4f} ({precision * 100:.2f}%)")
print(f"Recall   : {recall:.4f} ({recall * 100:.2f}%)")
print(f"F1-score : {f1:.4f} ({f1 * 100:.2f}%)")


# ==================================================
# 10. CLASSIFICATION REPORT
# ==================================================

print("\nClassification Report:")

print(
    classification_report(
        y_test,
        y_pred,
        labels=["ham", "spam"],
        zero_division=0
    )
)


# ==================================================
# 11. CONFUSION MATRIX
# ==================================================

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["ham", "spam"]
)

cm_df = pd.DataFrame(
    cm,
    index=["Actual Ham", "Actual Spam"],
    columns=["Predicted Ham", "Predicted Spam"]
)

print("\nConfusion Matrix:")
print(cm_df)

# Extract confusion matrix values.
tn, fp, fn, tp = cm.ravel()

print("\nConfusion Matrix Details:")
print("True Negatives  (TN):", tn)
print("False Positives (FP):", fp)
print("False Negatives (FN):", fn)
print("True Positives  (TP):", tp)


# ==================================================
# 12. TEST WITH NEW, UNSEEN MESSAGES
# ==================================================

new_messages = [
    "Congratulations! You have won a free prize. Claim now!",
    "Hi, are we meeting for lunch today?",
    "URGENT! You have won a cash reward. Call now!",
    "Please send me the project report by evening."
]

print("\n" + "=" * 45)
print("NEW MESSAGE PREDICTIONS")
print("=" * 45)

for message in new_messages:

    cleaned_message = clean_text(message)

    # Predict the message category.
    prediction = model.predict([cleaned_message])[0]

    # Calculate the model's estimated spam probability.
    probabilities = model.predict_proba([cleaned_message])[0]
    class_names = list(model.named_steps["classifier"].classes_)

    spam_index = class_names.index("spam")
    spam_probability = probabilities[spam_index]

    print("\nMessage:", message)
    print("Predicted category:", prediction.upper())
    print(f"Estimated spam probability: {spam_probability:.2%}")


# ==================================================
# 13. INTERACTIVE SPAM CLASSIFIER
# ==================================================

print("\n" + "=" * 45)
print("TRY YOUR OWN MESSAGE")
print("Type 'exit' to stop.")
print("=" * 45)

while True:

    user_message = input("\nEnter a message: ").strip()

    # Stop the program when the user types exit.
    if user_message.lower() == "exit":
        print("Spam classifier stopped.")
        break

    # Check for empty input.
    if not user_message:
        print("Please enter a message.")
        continue

    # Preprocess the user's message.
    cleaned_message = clean_text(user_message)

    # Predict the category.
    prediction = model.predict([cleaned_message])[0]

    print("Prediction:", prediction.upper())
