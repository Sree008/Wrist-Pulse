import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load the data from the CSV file
data = pd.read_csv("D:\\Final_Project_Working\\normalised_data.csv")

# Separate the features (X) and labels (y)
X = data.iloc[:, :14]  # Assuming the first 14 columns are the features
y = data.iloc[:, 14]   # Assuming the 15th column is the label

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create a Neural Network classifier
nn_classifier = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)

# Train the classifier
nn_classifier.fit(X_train_scaled, y_train)

# Make predictions on the test set
y_pred = nn_classifier.predict(X_test_scaled)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file
joblib.dump(nn_classifier, "D:\\Final_Project_Working\\neural_network_classifier.pkl")
