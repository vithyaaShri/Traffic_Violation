import pandas as pd

df = pd.read_csv("data/raw/Traffic_Violations.csv")

print("Total Columns:", len(df.columns))

for i, col in enumerate(df.columns, start=1):
    print(f"{i}. {col}")