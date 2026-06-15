import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv"
)

# Top 10 Violation Types
top_violations = (
    df["Violation Type"]
    .value_counts()
    .head(10)
)

print(top_violations)

plt.figure(figsize=(10, 6))
top_violations.plot(kind="bar")

plt.title("Top 10 Violation Types")
plt.xlabel("Violation Type")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig(
    "reports/charts/top_violation_types.png"
)

plt.show()