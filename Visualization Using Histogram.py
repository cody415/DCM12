import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset (make sure you download the file and save it as 'students.csv')
df = pd.read_csv("students.csv")

print("First 5 rows of the dataset:")
print(df.head())

# Select only numeric columns
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

# Plot histograms for each numeric column
plt.figure(figsize=(15, 10))
for i, column in enumerate(numeric_columns, 1):
    plt.subplot(len(numeric_columns)//2 + 1, 2, i)
    sns.histplot(df[column], kde=True, bins=20, color="skyblue")
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")

plt.tight_layout()
plt.show()
