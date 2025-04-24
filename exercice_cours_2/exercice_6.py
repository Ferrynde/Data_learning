import pandas as pd

# 1. Charger le dataset
df=pd.read_csv("../datasets/diabetes.csv")

# 2. Identifier les colonnes avec des valeurs manquantes
colonnes_nan = df.columns[df.isnull().any()].tolist()
print("🔍 Colonnes avec valeurs manquantes :")
print(colonnes_nan)

# 3. Imputer les valeurs manquantes par la médiane pour les colonnes numériques
colonnes_numeriques = df.select_dtypes(include=['float64', 'int64']).columns

for col in colonnes_numeriques:
    mediane = df[col].median()
    df[col] = df[col].fillna(mediane)

# 4. Détection des valeurs aberrantes avec IQR
colonnes_aberrantes = []
bornes = {}

for col in colonnes_numeriques:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    borne_min = Q1 - 1.5 * IQR
    borne_max = Q3 + 1.5 * IQR
    bornes[col] = (borne_min, borne_max)
    
    outliers = df[(df[col] < borne_min) | (df[col] > borne_max)]
    
    if not outliers.empty:
        colonnes_aberrantes.append(col)
        print(f"⚠️ {col} contient {outliers.shape[0]} valeurs aberrantes.")

print("\n Colonnes contenant des valeurs aberrantes :")
print(colonnes_aberrantes)

# 5. Supprimer les lignes contenant des valeurs aberrantes
for col in colonnes_aberrantes:
    borne_min, borne_max = bornes[col]
    df = df[(df[col] >= borne_min) & (df[col] <= borne_max)]

print(f"\n Nombre de lignes restantes après suppression des valeurs aberrantes : {df.shape[0]}")

# 6. Normalisation Min-Max manuelle
for col in colonnes_numeriques:
    min_val = df[col].min()
    max_val = df[col].max()
    if max_val != min_val:  # éviter division par zéro
        df[col] = (df[col] - min_val) / (max_val - min_val)

print("\n Aperçu des données normalisées :")
print(df.head())

# 7. Exporter le dataset nettoyé et normalisé
df.to_csv('credit_card_dataset_cleaned.csv', index=False)
print("\n Fichier exporté : credit_card_dataset_cleaned.csv")
