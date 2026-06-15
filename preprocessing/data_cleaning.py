import pandas as pd
import numpy as np

print("Loading Dataset...")

df = pd.read_csv(
    "data/raw/Traffic_Violations.csv"
)

print("Original Shape:", df.shape)

# ------------------------------------------------
# Remove duplicates
# ------------------------------------------------

df.drop_duplicates(inplace=True)

# ------------------------------------------------
# Date Conversion
# ------------------------------------------------

df["Date Of Stop"] = pd.to_datetime(
    df["Date Of Stop"],
    errors="coerce"
)

# ------------------------------------------------
# Year Conversion
# ------------------------------------------------

df["Year"] = pd.to_numeric(
    df["Year"],
    errors="coerce"
)

df["Year"] = df["Year"].fillna(
    df["Year"].median()
)
# ------------------------------------------------
# Fill Missing Values
# ------------------------------------------------

df["Color"] = df["Color"].fillna("UNKNOWN")

df["Article"] = df["Article"].fillna("UNKNOWN")

df["Search Conducted"] = (
    df["Search Conducted"]
    .fillna("No")
)

df["Search Disposition"] = (
    df["Search Disposition"]
    .fillna("Not Applicable")
)

df["Search Outcome"] = (
    df["Search Outcome"]
    .fillna("Not Applicable")
)

df["Search Reason"] = (
    df["Search Reason"]
    .fillna("Not Applicable")
)

df["Search Reason For Stop"] = (
    df["Search Reason For Stop"]
    .fillna("Not Applicable")
)

df["Search Type"] = (
    df["Search Type"]
    .fillna("Not Applicable")
)

df["Search Arrest Reason"] = (
    df["Search Arrest Reason"]
    .fillna("Not Applicable")
)

# ------------------------------------------------
# Convert Yes/No to Boolean
# ------------------------------------------------

boolean_columns = [
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
    "Search Conducted"
]

for col in boolean_columns:
    df[col] = df[col].map({
        "Yes": True,
        "No": False
    })

# ------------------------------------------------
# Coordinate Validation
# ------------------------------------------------

df.loc[df["Latitude"] == 0, "Latitude"] = np.nan
df.loc[df["Longitude"] == 0, "Longitude"] = np.nan

# ------------------------------------------------
# Standardize Text Columns
# ------------------------------------------------

df["Gender"] = (
    df["Gender"]
    .str.upper()
)

df["Race"] = (
    df["Race"]
    .str.upper()
)

df["Make"] = (
    df["Make"]
    .str.upper()
)

df["Color"] = (
    df["Color"]
    .str.upper()
)

# ------------------------------------------------
# Feature Engineering
# ------------------------------------------------

df["Month"] = (
    df["Date Of Stop"]
    .dt.month
)

df["Day"] = (
    df["Date Of Stop"]
    .dt.day_name()
)

# ------------------------------------------------
# Save Cleaned File
# ------------------------------------------------

output_file = (
    "data/processed/"
    "cleaned_traffic_violations.csv"
)

df.to_csv(
    output_file,
    index=False
)

print("Cleaning Completed")

print("Final Shape:", df.shape)