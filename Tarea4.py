# %%

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

#%%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[["hour", "weekday"]]

#%%

ssd=[]
ks = range(1,11)
for k in range(1,11):
    km = KMeans(n_clusters=k)
    km = km.fit(dfp)
    ssd.append(km.inertia_)

kneedle = KneeLocator(ks, ssd, S=1.0, curve="convex", direction="decreasing")
kneedle.plot_knee()
plt.show()

k = round(kneedle.knee)

print(f"Numbre of clusters: {k}")

# %%
kmeans = KMeans(n_clusters=k).fit(df[["total_items", "weekday"]])
sns.scatterplot(data=df, x="weekday", y="total_items", hue="")
plt.show()

# %%
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()

#%%
"""
== distancia euclidiana ==
Entrada:
    obj1, obj2: Objetos a regrupar (diccionarios)
    attributes: Lista de attributos (strings) a considerar para el cálculo de la distancia  
"""
def distance(obj1, obj2, attributes):
    return 0

"""
== K-Means ==
Entrada:
    k: Número de clústeres,
	D: Dataset compuesto de n objetos
"""
def kmeans(k, D, attributes):

    return []

if __name__ == "__main__":
    file = open("Mall_Customers.csv", newline='')
    dataset = []
    for row in csv.DictReader(file):
        nrow = {}
        for key, value in row.items():
            if key == "Genre":
                nrow[key] = value
            else:
                nrow[key] = float(value)
        dataset.append(nrow)
    kmeans(3, dataset, ["Annual_Income_(k$)", "Spending_Score"])




# %%

