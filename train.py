from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
iris = load_iris()
X, y = iris.data, iris.target

# Train model (default n_estimators=100)
clf = RandomForestClassifier(n_estimators=200, random_state=42)
clf.fit(X, y)

# Save model
joblib.dump(clf, "model.pkl")
print("Model saved as model.pkl")
