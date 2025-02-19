import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("D:\\Final_Project_Working\\extracted_features.csv")

# Define the columns to be normalized
columns_to_normalize = ['Mean', 'Variance', 'Standard deviation', 'Skewness', 'Kurtosis',
                        'Root mean square', 'Crest factor', 'Zero crossing rate',
                        'Peak-to-peak amplitude', 'Spectral centroid', 'Spectral spread',
                        'Spectral flatness', 'Maximum', 'Minimum']

# Compute the minimum and maximum values of each column
mins = df[columns_to_normalize].min()
maxs = df[columns_to_normalize].max()

# Normalize each ch column by subtracting the minimum value and dividing by the range (i.e., max - min)
df[columns_to_normalize] = (df[columns_to_normalize] - mins) / (maxs - mins)

# Save the normalized data to a new CSV file
df.to_csv("D:\\Final_Project_Working\\to_predict_norm_disease1.csv", index=False)

