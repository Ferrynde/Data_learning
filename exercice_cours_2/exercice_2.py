import pandas as pd

df=pd.read_csv('../datasets/Sales-Export_2019-2020.csv')
df.columns = df.columns.str.strip()  # Pour supprimer les espaces autour des noms

print(df.head())
print(df.info())

# Calcul des bornes IQR
Q1 = df['cost'].quantile(0.25)
Q3 = df['cost'].quantile(0.75)
IQR = Q3 - Q1

borne_min = Q1 - 1.5 * IQR
borne_max = Q3 + 1.5 * IQR

# Filtrer les valeurs aberrantes
outliers = df[(df['cost'] < borne_min) | (df['cost'] > borne_max)]

print(f"Nombre de valeurs aberrantes : {outliers.shape[0]}")
print(outliers[['cost']].head())
