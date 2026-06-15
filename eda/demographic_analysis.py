import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv"
)

gender_counts = (
    df["Gender"]
    .value_counts()
)

print(gender_counts)

plt.figure(figsize=(6,6))

gender_counts.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Violations By Gender"
)

plt.ylabel("")

plt.savefig(
    "reports/charts/gender_distribution.png"
)

plt.show()