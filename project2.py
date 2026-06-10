
# Project 2 - Iris Flower Classification using Decision Tree by ali hamza

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
iris = load_iris()

 
X = iris.data# Input features
y = iris.target # output labels

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

# Output results
print(" Iris Flower Classification model ")
print("Model Trained Successfully")
print("Accuracy =", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
