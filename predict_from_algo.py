import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np

# Load the trained Random Forest model
rf_classifier = joblib.load("D:\\Final_Project_Working\\randforalgo.pkl")

# Load the normalized input data from a CSV file
input_data = pd.read_csv("D:\\Final_Project_Working\\to_predict_norm_disease.csv")

# Prepare the input data for prediction
new_data = input_data[['Mean', 'Variance', 'Standard deviation', 'Skewness', 'Kurtosis',
                       'Root mean square', 'Crest factor', 'Zero crossing rate',
                       'Peak-to-peak amplitude', 'Spectral centroid', 'Spectral spread',
                       'Spectral flatness', 'Maximum', 'Minimum']]

# Make predictions on the new data
predicted_labels = rf_classifier.predict(new_data)

# Display the predicted labels
if 'Normal' in predicted_labels:
    print("No possibility of disorder is Predicted")
else:
    print("Possibility of", ", ".join(predicted_labels), "is Predicted")

# Plot radar chart
labels = ['Normal', 'Hypertension', 'Sugar']
values = [0, 0, 0]

for label in predicted_labels:
    if label == 'Normal':
        values[0] += 1
    elif label == 'Sugar':
        values[2] += 1
    elif label == 'Hypertension':
        values[1] += 1

# Normalize the values to fit within the range [0, 1]
max_value = max(values)
if max_value > 0:
    values = [v / max_value for v in values]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot radar chart
theta = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values += values[:1]
theta += theta[:1]

ax.fill(theta, values, 'b', alpha=0.1)
ax.plot(theta, values, color='r')

ax.set_ylim(0, 1)
ax.set_yticks([])
ax.set_xticks(theta[:-1])
ax.set_xticklabels(labels)

plt.title('Predicted Disease Distribution (Triangle Radar Chart)')
plt.show()






