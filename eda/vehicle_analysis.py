import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv"
)

top_makes = (
    df["Make"]
    .value_counts()
    .head(10)
)

print(top_makes)

plt.figure(figsize=(10,5))

top_makes.plot(
    kind="bar"
)

plt.title(
    "Top 10 Vehicle Makes"
)

plt.tight_layout()

plt.savefig(
    "reports/charts/top_vehicle_makes.png"
)

plt.show()