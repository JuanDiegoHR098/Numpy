import numpy as np

#CREAR MATRIZ DE CEROS TIPO 3X4
# a= np.zeros((3,4))
# print(a)

#crea una matriz de ceros tipo 3x4 excepto la primera fila que sera 1
# a[0,:]=1
# print(a)

# crea una matriz de ceros tipo 3x4 excepto la ultima fila que sera el rango entre 5 y 8
# a[2:3,:]=np.linspace(5,8,4)
# print(a)
# print("-"*30)

# #Crea una matriz de unos y se cambian los indices impares por un 2 
# b= np.ones(10)
# print(b)

# b[::2]=2
# print(b)

#Crean un tablero de ajederez con unos en las casilla negras y ceros en las casillas blancas

# c= np.zeros([8,8])

# for i in range(8):
#     for e in range(8):
#         if (i+e) % 2 != 0:
#             c[i,e]=1

# print(c)

#Crear una matriz aleatorio 5x5 hallaron los valores minimos y maximos 

d= np.random.random((5,5))
print(d.max(),d.min())