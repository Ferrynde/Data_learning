import pandas as pd

df=pd.read_csv('./dataset/StudentsPerformance.csv')
print(df.info())
print(df)
# print(df.head())
print(df.describe())
# print(df.duplicated())
# print("moyenne en math: ",df["math score"].mean())
# print("moyenne en lecture: ",df["reading score"].mean() )
# print("moyenne en écriture: ", df["writing score"].mean())
# print(df.shape)