import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("country_vaccinations.csv")

print(df.head(10))
print(df.isnull().any())

subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values Heatmap")
plt.show()

df_cleaned = df.dropna(how="all")
df_bfill = df_cleaned.fillna(method="bfill")
df_interpolated = df_cleaned.interpolate()
df_dropped = df_cleaned.dropna()

print(df_cleaned.head(10))
print(df_bfill.head(10))
print(df_interpolated.head(10))
print(df_dropped.head(10))
