import pandas as pd

df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv",
    nrows=10000
)

columns = [
    "Accident",
    "Belts",
    "Personal Injury",
    "Property Damage",
    "Fatal",
    "Commercial License",
    "HAZMAT",
    "Commercial Vehicle",
    "Alcohol",
    "Work Zone",
    "Search Conducted",
    "Contributed To Accident"
]

for col in columns:
    print(f"\n{col}")
    print(df[col].value_counts(dropna=False))