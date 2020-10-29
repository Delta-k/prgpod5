# %%
import pandas as pd
import numpy as np
#%%
import seaborn as sns

# %%
df = pd.read_csv("insurance.csv")
df.head()
df.describe() 

#%%
#sns.displot(x = "region", data = df)
#sns.displot(x="region",hue="sex",multiple="stack",data=df)
#sns.displot(x="age",data=df)
#g=sns.histplot(data=df,x="age",multiple="stack",hue="sex")
for q in df.age.quantile([.25,.5,.75]):
    g.axvline(q,linestyle=":") #línea para marcar el eje en la posición q
    g.text(q,5,q)

#%%
df.corr()
#sns.heatmap(df.corr(),annot=True)
#sns.scatterplot(data=df,x="age",y="charges")
sns.scatterplot(data=df,x="bmi",y="charges",hue="smoker")

#%%
fumadores = df[df.smoker == "yes"]
nofumadores = df[df.smoker == "no"]
#sns.scatterplot(data=fumadores,x="age",y="charges",hue="bmi")
#sns.heatmap(fumadores.corr(),annot=True)

pd.cut(fumadores.bmi ,[0,18.5,25,30,60], labels=['Underweight', 'Normal', 'Overweight','Obese'], right = True)
#cerrado por la izq


#%%

pd.cut(df.age,[17,20,35,50,64],labels=['Adolecente','Joven adulto','Adulto','Adulto mayor'])

# %%
print("Esta es la media de la edad:", df["age"].mean())


# %%
df.shape
