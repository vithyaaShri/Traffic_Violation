import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv"
)

print("\nDataset Shape")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

print("\nDuplicate Rows")
print(df.duplicated().sum())

print("\nData Types")
print(df.dtypes)