# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()

#%%
df.shape

#%%
df.describe()

# %%
df.mean()
df.median()
df.mode()

# %%
