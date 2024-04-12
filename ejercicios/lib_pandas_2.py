import numpy as np
import pandas as pd

# a=[i for i in range(10)]

# # LA FUNCION MAP RECIBE UNA FUNCION Y UN ITERABLE. SE UTILIZA CUANDO QUEREMOS APLICAR UNA FUNCION A UN ITERABLE 
# b= list(map(lambda x: x*2,a))
# print(b)

# ### FUNCION FILTER
# # AL IGUAL QUE MAP RECIBE UNA FUNCION Y UN ITERABLE
# #NOS SIRVE PARA FILTRAR CON UNA FUNCION LOS VALORES DEL ITERABLE QUE CUMPLEN DICHA FUNCION

# c= [i for i in range(30)]
# d= list(filter(lambda x: x%2==0,c))
# print(d)


dict_data= {"edad":[20,21,22,23,24],
            "cm":[110,112,113,114,115],
            "pais":["co","mx","ee.uu","co","arg"],
            "genero":["M","M","F","F","M"],
            "Q1":[5,10,12,np.nan,7 ],
            "Q2":[7,9,9,8,7]
            }

df= pd.DataFrame(dict_data)

# USO DE APPLY Y MAPAPPLY ( NOTA: MAP APPLY SOLO TRABAJARIA CON LAS SERIES, A DIFERENCIA DEL APPLY QUE SE LE PUEDE ESPECIFICAR (FUNCIONAN IGUAL))
# y=df["cm"].apply(lambda x: x*2) # DE ESTA FORMA SE USA PARA APLICARLO A UNA SERIE( FUNCIONA MUY SIMILAR A MAP Y FILTER)
# z= df.apply(lambda x: x*2) # SE APLICARIA SOBRE TODOS EL DATAFRAME
# w= df.apply(lambda x:x**2, axis=0) #SE APLICA A LO LARGO DE UN EJE
# print(w)


# USO DE GROUPBY 
# SE UTILIZA PARA AGRUPAR POR CLAVE VALOR COMO SE DESEE MOSTRAR
# EN ESTE CASO ITERA SOBRE EL DATA FRAME UTILIZANDO LA CLAVE "GENERO" Y ME TRAE TODOS LOS VALORES DIFERENTES QUE SE ENCUENTRAN ESTA CLAVE
# EN ESTE CASO MASCULINO Y FEMENINO AGRUPADOS 
# for k,v in df.groupby(["genero"]):
#     print(f"la llave asociada a {k} y su valor asociado es: \n{v} ")

df.groupby(["genero"]).mean()
print(df)