import pandas as pd

file_path = "data/raw/Traffic_Violations.csv"

df = pd.read_csv(file_path, nrows=10000)

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns.tolist())

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)