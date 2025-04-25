import matplotlib.pyplot as mpt
import seaborn as sb

df = sb.load_dataset("diamonds")

sb.boxplot(data=df, x="cut", y="price", hue="color")
mpt.title("Prix des diamants par coupe et couleur")
mpt.xlabel("Coupe")
mpt.ylabel("Prix")
mpt.show()