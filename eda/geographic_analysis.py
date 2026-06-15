import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/processed/cleaned_traffic_violations.csv"
)

top_states = (
    df["Driver State"]
    .value_counts()
    .head(10)
)

print(top_states)

plt.figure(figsize=(10,5))

top_states.plot(
    kind="bar"
)

plt.title(
    "Top Driver States"
)

plt.tight_layout()

plt.savefig(
    "reports/charts/top_driver_states.png"
)

plt.show()