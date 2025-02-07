import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import os

# Load dataset
file_path = "./data/IMDB Dataset.csv"

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Dataset not found at {file_path}")

data = pd.read_csv(file_path)

# Check required columns
if 'review' not in data.columns or 'sentiment' not in data.columns:
    raise ValueError("Dataset must have 'review' and 'sentiment' columns.")

# Convert sentiment to numerical
data['sentiment'] = data['sentiment'].map({'positive': 1, 'negative': 0})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data['review'], data['sentiment'], test_size=0.2, random_state=42
)

# Train model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Save model correctly
model_dir = "model"
os.makedirs(model_dir, exist_ok=True)
model_path = os.path.join(model_dir, "sentiment_model.pkl")

joblib.dump(model, model_path)
print(f"Model trained and saved at {model_path}!")
