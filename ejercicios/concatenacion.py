import numpy as np 

x= np.array([[0,1,2],[1,7,8]])
y=np.array([[1,7,8],[2,4,5]])
z=np.array([[3,9,1],[1,7,8]])
w= np.array([[0,1,2,1,7,8]])

# concatenacion= np.concatenate((x,y), axis=1)
# print(concatenacion)
# print(np.ndim(concatenacion))
# print(("-")*30)

# m= np.array_split(w,2)
# print(m)

#OPERACIONES CON MATRICES (+,-,*,/) SE COMPORTAN IGUAL AL EJEMPLO   
c= x*y
print(c)

# PARA SACAR UNA MATRIZ BOOLEANA PARA FILTRAR LA INFORMACION
mascaras= y<4
print(mascaras)