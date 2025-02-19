import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the data from the CSV file
data = pd.read_csv("D:\\Final_Project_Working\\normalised_data.csv")

# Separate the features (X) and labels (y)
X = data.iloc[:, :14]  # Assuming the first 14 columns are the features
y = data.iloc[:, 14]  # Assuming the 15th column is the label

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Create a Random Forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file
joblib.dump(rf_classifier, "D:\\Final_Project_Working\\randforalgo.pkl")
