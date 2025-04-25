import matplotlib.pyplot as mpt
import seaborn as sb

df=sb.load_dataset("titanic")
print(df.describe())
sb.countplot(data=df, x="class", hue="sex")
mpt.title("graphe des survivants")
mpt.xlabel("class")
mpt.ylabel("Nombre de passagers")
mpt.show()

sb.violinplot(data=df, x="class", y="fare")
mpt.title("Prix du ticket par classe")
mpt.xlabel("class")
mpt.ylabel("fare")
mpt.show()

correlation_matrix = df.corr(numeric_only=True)

sb.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
mpt.title("Matrice de corrélation")
mpt.show()