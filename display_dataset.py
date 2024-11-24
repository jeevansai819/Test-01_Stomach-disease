import pandas as pd

# Load the dataset
df = pd.read_csv('stomach_diseases_dataset.csv')

# Display basic information about the dataset
print("Dataset Loaded Successfully!")
print("Number of Rows:", len(df))
print("Number of Columns:", len(df.columns))
print("Preview of the Dataset:")
print(df.head())
