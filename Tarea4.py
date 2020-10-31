# %%
#Importar librerías
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

#%%
#Carga Dataset reto Ulabox
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

#Dataset que discrimina variables "customer" y "order"
dfp = df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]]

#%%
#Generar k (número óptimo de clusters)
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
#Centro de cada cluster por variable
kmeans = KMeans(n_clusters=k).fit(df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]])
#sns.scatterplot(data=df, x="weekday", y="total_items", hue="hour")
print(kmeans.cluster_centers_)

# %%
#Centro de cada cluster por variable (arreglo)
kmeans.cluster_centers_

# %%
#Distancia euclidiana / Generación de heatmap a partir de matriz de distancias
import numpy as np
matriz_distancias = []
for i in range(4):
    vector=[]
    for j in range(4):
        newDistancia =np.linalg.norm(kmeans.cluster_centers_[i]-kmeans.cluster_centers_[j])
        vector.append(newDistancia)
    matriz_distancias.append(vector)
print(matriz_distancias)
sns.heatmap(matriz_distancias, cmap="coolwarm", annot = True)

# %%
#Visualización porcentaje para cada variable (departamento) Cluster 0
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()
cluster0[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
#Visualización porcentaje para cada variable (departamento) Cluster 1
cluster1 = df[kmeans.labels_ == 1]
cluster1.describe()
cluster1[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
#Visualización porcentaje para cada variable (departamento) Cluster 2
cluster2 = df[kmeans.labels_ == 2]
cluster2.describe()
cluster2[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
#Visualización porcentaje para cada variable (departamento) Cluster 4
cluster3 = df[kmeans.labels_ == 3]
cluster3.describe()
cluster3[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()


# %%

