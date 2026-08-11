import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("penguins")

print("Original Penguin Dataset:")
print(df.head(10))

print("\nAre missing values present?")
print(df.isnull().any())

print("\nTotal missing values in each column:")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
plt.title("Missing Values in the Penguins Dataset")
plt.xlabel("Dataset Columns")
plt.ylabel("Penguin Records")
plt.show()

df = df.dropna(how="all")
print("\nDataset after removing completely empty rows:")
print(df.head())

categorical_columns = ["species", "island", "sex"]
for column in categorical_columns:
    most_common_value = df[column].mode()[0]
    df[column] = df[column].fillna(most_common_value)

numerical_columns = ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
df[numerical_columns] = df[numerical_columns].interpolate()
df[numerical_columns] = df[numerical_columns].bfill().ffill()

print("\nMissing values after data cleaning:")
print(df.isnull().sum())

print("\nCleaned Penguin Dataset:")
print(df.head(10))

complete_penguins = df.dropna()
print("\nNumber of complete penguin records:")
print(len(complete_penguins))
