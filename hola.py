# %%
import pandas as pd
import numpy as np
import seaborn as sns
# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()

#%%

sns.displot(x="weekday",hue="hour",multiple="stack",data=df)

#%%
g = sns.histplot(data=df, x="hour", multiple="stack", hue = "weekday")
for q in df.hour.quantile([.25, .5, .75]):
    g.axvline(q, linestyle=":")
    g.text(q, 5, q)


# %%
sns.heatmap(df.corr())

# %%
df.plot.scatter(x="weekday",y="discount%")

# %%
df.plot.scatter(x="weekday",y="hour")

# %%
df.plot.scatter(x="weekday",y="Food%")


# %%
df.plot.scatter(x="weekday",y="Fresh%")

# %%
sns.catplot(x = "weekday", y =  "discount%", data = df, kind = "box");

# %%
sns.catplot(x = "weekday", y =  "discount%", data = df, kind = "box");