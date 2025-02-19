import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
import joblib

# Load the data from the CSV file
data = pd.read_csv("D:\\Final_Project_Working\\normalised_data.csv")

# Separate the features (X) and labels (y)
X = data.iloc[:, :14]  # Assuming the first 14 columns are the features
y = data.iloc[:, 14]   # Assuming the 15th column is the label

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear', random_state=42)  # You can change the kernel as needed

# Train the classifier
svm_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = svm_classifier.predict(X_test)

# Evaluate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Save the trained model to a file
joblib.dump(svm_classifier, "D:\\Final_Project_Working\\svm_algo.pkl")

