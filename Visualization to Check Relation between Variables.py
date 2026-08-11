import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("students.csv")

print("First 5 rows of the dataset:")
print(df.head())

numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

plt.figure(figsize=(15, 10))
sns.pairplot(df[numeric_columns])
plt.suptitle("Pairplot of Numeric Variables", y=1.02)
plt.show()

plt.figure(figsize=(10, 6))
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

for column in numeric_columns[1:]:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=numeric_columns[0], y=column, data=df)
    plt.title(f"Relationship between {numeric_columns[0]} and {column}")
    plt.show()
