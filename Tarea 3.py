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

df_nuevo = df.drop(columns = ["customer","order"] )
sns.boxplot(data = df_nuevo, orient = "h",palette="Set2")

# %%
sns.catplot(x = "weekday", y =  "hour", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "discount%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "total_items", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "customer", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Food%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Fresh%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Baby%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Drinks%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Home%", data = df, kind = "box");
sns.catplot(x = "weekday", y =  "Beauty%", data = df, kind = "box");

# %%
