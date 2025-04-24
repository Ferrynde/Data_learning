import pandas as pd

df=pd.read_csv("../datasets/diabetes.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

# 2. Imputation par la médiane pour les colonnes numériques
numeriques = df.select_dtypes(include=['float64', 'int64']).columns

for col in numeriques:
    mediane = df[col].median()
    df[col] = df[col].fillna(mediane)
    # 3. Imputation par le mode pour les colonnes catégorielles (object ou string)
    
catégorielles = df.select_dtypes(include=['object', 'string']).columns

for col in catégorielles:
    mode_val = df[col].mode()[0]  # mode() renvoie une série, on prend la première valeur
    df[col] = df[col].fillna(mode_val)

print("Valeurs manquantes restantes :")
print(df.isnull().sum())