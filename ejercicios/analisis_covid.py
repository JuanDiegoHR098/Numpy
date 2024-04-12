import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_covid= pd.read_csv("covid_19.csv")

q= df_covid.head(10) # TRAE LOS PRIMEROS 10 DATOS DEL ARCHIVO
w= df_covid.tail(10) # TRAE LOS ULTOMOS 10 DAROS DEL ARCHIVO
e= df_covid.iloc[[1,30,200],[1,4,5]] # DE ESTA FORMA SE BUSCA POR FILAS [1,30,200] Y COLUMNAS [1,4,5] CON EL INDICE 
r= df_covid.loc[400:450,["Date","Confirmed"]]
t= df_covid.loc[0:,"Confirmed"]>0
y=np.sum(t)

print(q)

# u= list(map(lambda x: x+1,r))
# print(u)