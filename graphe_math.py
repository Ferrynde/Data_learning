import matplotlib.pyplot as mpt
import pandas as pd

df= pd.read_csv('./dataset/StudentsPerformance.csv')

mpt.figure(figsize=(10,5))
mpt.title("Graphe de la colonne des notes en maths")
mpt.xlabel("Index")
mpt.ylabel("Valeurs")
mpt.plot(df["math score"])
mpt.grid()
mpt.show()