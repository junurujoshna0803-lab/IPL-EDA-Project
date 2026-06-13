import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
df = pd.read_csv("data.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
print(df.describe())
plt.hist(df[df.columns[0]])
plt.title("Distribution")
plt.show()
sns.countplot(x=df.columns[0])
plt.xticks(rotation=45)
plt.show()
corr = df.corr(numeric_only=True)
plt.figure(figsize=(10,6))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.show()
sns.boxplot(df[df.columns[1]])
plt.show()