import matplotlib.pyplot as mpt
import seaborn as sb

df= sb.load_dataset("penguins")
print(df.describe())
sb.pairplot(data=df, vars=["bill_length_mm", "bill_depth_mm", "flipper_length_mm"], hue="species")
mpt.title("courbes des caractéristiques")
mpt.show()

sb.boxplot(data=df, x='island', y='body_mass_g')
mpt.title('Masse corporelle par île')
mpt.xlabel('Île')
mpt.ylabel('Masse corporelle (g)')
mpt.show()

sb.scatterplot(
    data=df,
    x='flipper_length_mm',
    y='bill_length_mm',
    hue='species',
    style='sex'
)
mpt.title('Relation entre nageoires et bec selon le sexe')
mpt.xlabel('Longueur des nageoires (mm)')
mpt.ylabel('Longueur du bec (mm)')
mpt.show()