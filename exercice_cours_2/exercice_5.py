import pandas as pd

df=pd.read_csv('../datasets/WineQT.csv')
print(df.head())
print(df.info())
print(df.describe())

print(df.isnull().sum())

colonnes_numeriques = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
print(colonnes_numeriques)
# Suppression des colonnes contenant plus de 30% de valeurs manquantes
seuil = 0.3  
df = df[df.isnull().mean(axis=1) < seuil]
for col in colonnes_numeriques:
    df[col] = df[col].fillna(df[col].mean())
    numeriques = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeriques:
    mediane = df[col].median()
    df[col] = df[col].fillna(mediane)