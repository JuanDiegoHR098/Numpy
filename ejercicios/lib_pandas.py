import numpy as np
import pandas as pd

# w=[1,2,3,4,5,6,7]
# w1= pd.Series(w)
# x= {"a":0,"b":1,"c":2,"d":3}
# x1= pd.Series(x)     #UNA SERIE ES UN CONJUNTO DE ELEMENTOS DONDE SE ALMACENA CUALQUIER TIPO DE DATOS
# print(w1)

# #CREAR SERIES ALEATORIAS USANDO NUMPY
# print("-"*30)
# q= pd.Series(np.random.randn(5), index=["a","b","c","d","e"]) # randn  ME ARROJA NUMEROS ALEATORIOS INCLUYENDO NEGATIVOS # INDEX ME PERMITE CAMBIAR INDICE PREDETERMINADO POR EL INDICE QUE SE DESEA
# print(q)
# print("-"*30)
# #DATAFRAME
# #ES EL CONJUTNO DE TODOS LAS SERIES

# e= {"one":pd.Series(np.random.random_integers(0,6,5),index=["a","b","c","d","e"]),
#     "two":pd.Series(np.random.randn(3), index=["a","c","d"])}

# df= pd.DataFrame(e)
# print(df)
# print("-"*30)
# #INDEXACION
# v=df["a":"c"] # SE PUEDE HACER CON LOS NOMBRES DE LAS CLAVES O CON NUMEROS
# print(v)
# print("-"*30)

# #REASIGNACION DE VALORES
# a= pd.DataFrame(e,index=["m","ñ","o","p","q"]) #COMO EN ESTE CASO NO HAY NADA ASIGNADO A ESTOS VALOR RETORNA NaN
# print(a)
# m= pd.DataFrame(e,index=["a","b","c","l","ñ"])
# print(m)

# g= pd.DataFrame(e, index=["x","w","z"], columns=["three","four"]) # AQUI REDEFINIMOS TODOO NUEVOS INDICES Y NUEVAS COLUMNAS 
# print(g)

# print("-"*30)

#LLAMADO DE INDICES Y COLIMNAS 
# print(df.index)
# print(df.columns)
# print(df.shape) #FORMA
# print(df.size) #TAMAÑO
# print(df.ndim) #DIMENSION

print("-"*30)
#

dict_data= {"edad":[20,21,22,23,24],
            "cm":[110,112,113,114,115],
            "pais":["co","mx","ee.uu","co","arg"],
            "genero":["M","M","F","F","M"],
            "Q1":[5,10,12,np.nan,7 ],
            "Q2":[7,9,9,8,7]
            }

dt= pd.DataFrame(dict_data, index=["a","b","c","d","f"])



##################### COVERTIR A DIFERENTES FORMATOS #######################
df_excel= dt.to_excel("test.xlsx", index=True)
df_csv=dt.to_csv("test.csv",index=True)
df_json=dt.to_json("test.json")

######################### PARA LEERLOS ##################################
df_leer_excel= pd.read_excel("test.xlsx") # SI SE TIENE EN OTRA CARPETA COPIAR LA RUTA DEL ARCHIVO
df_leer_csv= pd.read_csv("test.csv")
df_leer_json= pd.read_json("test.json")



#################### PARA BORRAR ######################
#PARA BORRAR UNA COLUMNA  (NOTA: AXIS=0 FILAS , AXIS=1 COLUMNAS)
df_leer_excel.drop(["Unnamed: 0","Q1"],axis=1 ,inplace=True) #AXIS EL EJE DONDE SE ENCUENTRA Y INPLACE PARA QUE SE VISUALICE QUE SI SE BORRO

# print(df_leer_excel)
###################### PARA HACER PROMEDIOS #################
df_leer_csv["promedio"]= df_leer_csv[["Q1","Q2"]].mean(axis=1, skipna=True, numeric_only=False)

###############SINTAXIS PARA REMPLAZAR DATOS ##########################
#1) df_leer_csv["genero"]= df_leer_csv["genero"].replace({"M":0,"F":1})

#2 DE ESTA FORMA SE LOCALIZA DONDE SE ENCUENTRA LO QUE SE BUSCA Y EL SEGUNDO PARAMETRO ES PARA MODIFICAR SOLO ESA COLUMNA, SI NO SE PONE SEGUNDO PARAMETRO MODIFICA TODA LA FILA ¡¡OJOOO!!

# df_leer_csv.loc[df_leer_csv["genero"]=="M","genero"]=1

#3 POR INDEXACION
#SE LE DA DESDE DONDE HASTA DONDE ( FILAS) DESEA TRAER Y EN LA LISTA DESPUES DE LA COMA SE PONEN LOS NOMBRES DE LAS COLUMNAS
t=df_leer_csv.loc[:,["genero","pais"]]

#4 OTRAS COSAS QUE SE PUENDE HACER
#DE ESTA FORMA FILTRAMOS Y ASIGNAMOS UN VALOR A TODOS LOQ QUE CUMPLEN LA CONDICION( SE DEBE ESPECIFICAR LA COLUMNA DONDE SE DESEA HACER LOS CAMBIOS)
df_leer_csv.loc[df_leer_csv["promedio"]>8,"promedio"] = "Aprobo"

############ APLICAR MASCARAS ###################
#1-)ME SACA UNA LISTA DE BOOLEANOS SI SE ENCUENTRA O NO A LO QUE ESTA IGUALADO 

m=df_leer_csv["genero"]=="M"

#2-)TAMBIEN SE PUEDEN SUMAR LOS VALORES BOOLEANOS 
n= np.sum(m) # DE ESTA FORMA SABEMOS CUANTOS HOMBRES O MUJERES HAY 


print(m)

