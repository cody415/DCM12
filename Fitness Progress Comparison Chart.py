import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

exercise_df = sns.load_dataset("exercise")
running_data = exercise_df.loc[exercise_df["kind"] == "running"]
one_minute_data = running_data.loc[running_data["time"] == "1 min", ["id", "pulse"]]
thirty_minute_data = running_data.loc[running_data["time"] == "30 min", ["id", "pulse"]]

fitness_merge = one_minute_data.merge(thirty_minute_data, on="id", suffixes=("_1_minute", "_30_minutes"))
fitness_merge["pulse_progress"] = fitness_merge["pulse_30_minutes"] - fitness_merge["pulse_1_minute"]
fitness_merge = fitness_merge.sort_values("pulse_progress", ascending=False)

participant_names = ["Participant " + str(pid) for pid in fitness_merge["id"]]
fitness_data = {
    "participant": participant_names,
    "pulse_1_minute": fitness_merge["pulse_1_minute"].tolist(),
    "pulse_30_minutes": fitness_merge["pulse_30_minutes"].tolist(),
    "pulse_progress": fitness_merge["pulse_progress"].tolist()
}
chart_df = pd.DataFrame(fitness_data)

positions = np.arange(len(chart_df["participant"]))
bar_width = 0.35

plt.figure(figsize=(12, 7))
one_minute_bars = plt.bar(positions - bar_width / 2, chart_df["pulse_1_minute"], width=bar_width, label="After 1 minute")
thirty_minute_bars = plt.bar(positions + bar_width / 2, chart_df["pulse_30_minutes"], width=bar_width, label="After 30 minutes")

plt.plot(positions, chart_df["pulse_progress"], color="red", marker="o", linestyle="--", label="Pulse Increase Trend")

plt.title("Running Exercise Pulse Comparison")
plt.xlabel("Participant")
plt.ylabel("Pulse Rate")
plt.xticks(positions, chart_df["participant"], rotation=45)
plt.legend()

for bar in one_minute_bars:
    value = bar.get_height()
    plt.annotate(str(value), (bar.get_x() + bar.get_width() / 2, value), textcoords="offset points", xytext=(0, 5), ha="center")

for bar in thirty_minute_bars:
    value = bar.get_height()
    plt.annotate(str(value), (bar.get_x() + bar.get_width() / 2, value), textcoords="offset points", xytext=(0, 5), ha="center")

plt.tight_layout()
plt.show()
