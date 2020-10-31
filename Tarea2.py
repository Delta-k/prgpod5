# %%
#Se cargaron los datos usando la librería estándar de Python y Pandas.
import pandas as pd
import numpy as np

# %%
#Dataset 
df = pd.read_csv("ulabox_orders_with_categories_partials_2017.csv")
df.head()

#%%
#Verificación del tamaño del dataset
df.shape

#%%
#Analizis de variables y su rangos (Se muestra el máximo y mínimo)
df.describe()

# %%
#Medidas de tendencia central (media, mediana y moda) 

df.mean()
df.median()
df.mode()

# %%
#Medidas de dispersión (desviación estándar) de cada variable
df.std()

# %%
#Medidas de posición (cuartiles) de cada variable.
df.quantile()