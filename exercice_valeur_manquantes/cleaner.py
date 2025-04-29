import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 2. Charger le dataset Titanic
df = sns.load_dataset('titanic')

# 3. Observer rapidement
print(df.head())
print(df.info())
print(df.describe())

# 4. Simuler des données MAR
np.random.seed(42)  # pour reproductibilité
mask = (df['sex'] == 'female') & (np.random.rand(len(df)) < 0.5)
df.loc[mask, 'age'] = np.nan

# 5. Vérifier l'effet
print("\nProportion de valeurs manquantes par sexe :")
print(pd.crosstab(df['sex'], df['age'].isnull(), normalize='index'))

# 6. Visualiser les données manquantes
plt.figure(figsize=(6,4))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Visualisation des valeurs manquantes (Après simulation)')
plt.show()

# 7. Détection que les données sont MAR
df['age_missing'] = df['age'].isnull()

# On analyse par rapport au sexe
missing_by_sex = pd.crosstab(df['age_missing'], df['sex'], normalize='columns')
print("\nTaux de valeurs manquantes en fonction du sexe :")
print(missing_by_sex)

median_ages = df.groupby('sex')['age'].median()
print("\nMédianes d'âge par sexe :")
print(median_ages)

def impute_age(row):
    if pd.isnull(row['age']):
        return median_ages[row['sex']]
    else:
        return row['age']

df['age_imputed'] = df.apply(impute_age, axis=1)

print("\nDonnées après imputation :")
print(df[['sex', 'age', 'age_imputed']].head(10))

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.histplot(df['age'], bins=30, ax=axes[0], kde=True)
axes[0].set_title('Distribution des âges avant imputation')

sns.histplot(df['age_imputed'], bins=30, ax=axes[1], kde=True)
axes[1].set_title('Distribution des âges après imputation')

plt.tight_layout()
plt.show()
