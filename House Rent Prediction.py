import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

HouseDF = pd.read_csv('USA_Housing.csv')

print(HouseDF.head())
print(HouseDF.info())
print(HouseDF.columns)

sns.pairplot(HouseDF)
plt.show()

sns.heatmap(HouseDF.corr(), annot=True)
plt.show()
