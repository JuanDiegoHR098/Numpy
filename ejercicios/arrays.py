import numpy as np
import pandas as pd

arreglo= np.array([[[0,1,2],
                    [1,7,8]
                    ,[1,7,8]],

                [[0,3,5],
                [2,6,9],
                [1,7,8]],

                [[0,2,3],
                [5,7,9],
                [7,9,1]]])

#INDEXACION DE LISTA
#Primer es por si se trabaja una tercera dimension
#El segundo corresponde a las filas que se van a tomer de cada arreglo
#El tercero corresponde a las columnas que se van a tomar y hasta donde se van a tomar
f=arreglo[0:,0:,0:2]
print(f)
print(np.shape(arreglo)) #ME DA LA FORMA DE LA MATRIZ

n= arreglo.reshape(9,1,3)
print(np.ndim(n))


#CREAR MATRICES DESDE CERO

# MATRIZ DE CEROS
q= np.zeros((2,5),dtype=int)
print(q)
print("-"*30)
r=np.ones((2,5), dtype=float)
print(np.shape(r)) # NOS MUESTRA LA FORMA DE LA MATRIZ

print("-"*30)
t= np.identity(4) #CREA LA MATRIZ IDENTIDAD
print(t)
print("-"*30)

#CREAR MATRIZ DE NUMEROS ENTEROS ALEATORIOS ENTESOS 
#SI SE DESEA CON NUMEROS ALEATORIOS FLOTANTES SE HARIA ASI : np.ramdom.rand(10,size(3,3,3))
i= np.random.randint(10,size=(3,3,3))
print(i)
print("-"*30)


#TOMA LOS VALORES DESDE 0 HASTA 5  Y ME ARROJA UN VECTOR CON 11 NUMEROS ENTRE 0 Y 5 DE UNA FORMA ORDENADA
o= np.linspace(0,5,11,dtype=int)
print(o)
print("-"*30)

#CREA UN VECTOR CON DETERMINADO RANGO Y SI SE DESEA SE LE AGREGA UN SALTO
p= np.arange(0,20,2)
print(p)
print("-"*30)

#MATRIZ DE UNA DIMENCION QUE ARROJA VALORES ALEATORIOS ENTRE 0 Y 1
a=np.random.random(3)
print(a)
print("-"*30)
#ME CREA UNA MATRIZ ALEATORIOA ENTRE UN NUMERO Y OTRO SIN INCLUIR EL ULTIMO , SE PUEDE CREAR DEL TAMAÑO QUE SE QUIERA
s= np.random.random_integers(2,20,size=(3,2,4))
print(s)
print("-"*30)

#CREA UNA MATRIZ DE TAMAÑO 2X3 VACIA CON VALORES SIN INICIALIZAR
d=np.empty((2,3))
print(d)
print("-"*30)

n= np.random.randn(5)
print(n)