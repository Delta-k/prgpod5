# %%

import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from kneed import KneeLocator

#%%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")

dfp = df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]]

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
kmeans = KMeans(n_clusters=k).fit(df[["total_items","discount%","weekday","hour","Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]])
#sns.scatterplot(data=df, x="weekday", y="total_items", hue="hour")
print(kmeans.cluster_centers_)

# %%
kmeans.cluster_centers_

# %%
import numpy as np
np.linalg.norm(kmeans.cluster_centers_[0] - kmeans.cluster_centers_[1] )

# %%
cluster0 = df[kmeans.labels_ == 0]
cluster0.describe()
cluster0[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
cluster1 = df[kmeans.labels_ == 1]
cluster1.describe()
cluster1[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
cluster2 = df[kmeans.labels_ == 2]
cluster2.describe()
cluster2[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%
cluster3 = df[kmeans.labels_ == 3]
cluster3.describe()
cluster3[["Food%","Fresh%","Drinks%","Home%","Beauty%","Health%","Baby%","Pets%"]].sum().plot.bar()
plt.show()

# %%



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

