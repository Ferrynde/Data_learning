import pandas as pd

df = pd.read_csv("../datasets/marketing_campaign.csv")

print(df.info())
print(df.describe())

doublons = df.duplicated()  # retourne un booléen pour les doublons
print(f"\n Nombre total de doublons : {doublons.sum()}")

#sup les doublons sans en gardant la première occurence
df_sans_doublons = df.drop_duplicates()

