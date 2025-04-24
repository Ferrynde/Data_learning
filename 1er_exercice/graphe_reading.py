import matplotlib.pyplot as mpt
import pandas as pd

df=pd.read_csv('./dataset/StudentsPerformance.csv')

mpt.figure(figsize=(10,5))
mpt.title("graphe des notes de lecture")
mpt.xlabel("Indices")
mpt.ylabel("valeurs")
mpt.plot(df['reading score'])
mpt.grid()
mpt.show()