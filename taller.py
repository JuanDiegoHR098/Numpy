import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io as sio


#1-)Crear una matriz de Numpy aleatoria de 4 dimensiones y un size de 1200000 

y= np.random.random((30,40,10,100))


# i= np.random.randint(1200000,size=(30,40,10,100))
# print(i)

#2-) Crea una copia de la matriz creada en el ítem anterior (usar método copy) de solo 3 
# dimensiones (“Cortando una de las dimensiones”) 

q= y.copy().reshape((30,40,1000))


# r= np.random.randint(72,size=(2,3,6))
# print(r)

# De la matriz 3D, muestra todos los atributos propios de dicha matriz , dimensión, tamaño, 
# etc..

w=q.shape
e=q.size
r= q.dtype
t= q.ndim


#3.) Modificar su forma y pasarla a 2D 

u= q.copy().reshape(1200,1000)

#4.)Crea una función que reciba la matriz anterior y la pase a un objeto tipo dataframe de Pandas

def dataframe(x):
    return pd.DataFrame(x)



#5.)Crear una función que permita cargar un archivo .mat y .csv  
dict_data= {"edad":[20,21,22,23,24],
            "cm":[110,112,113,114,115],
            "pais":["co","mx","ee.uu","co","arg"],
            "genero":["M","M","F","F","M"],
            "Q1":[5,10,12,np.nan,7 ],
            "Q2":[7,9,9,8,7]
            }
a= sio.savemat("python1.mat",dict_data)

def cargar_archivo():
    print("1.Cargar archivo .mat\n2.Cargar archivo.csv")
    entrada=int(input("Ingrese una opcion:"))
    if entrada == 1:
        
        return sio.loadmat("archivos\senales_potencial.mat")
    elif entrada ==2:
        intro= input("Ingrese la direccion con el nombre del archivo")
        return pd.read_csv(intro)
    
#6.) Crear funciones de suma, resta, multiplicación, división, logaritmo ,promedio, desviación estándar NOTA: Estas funciones deben permitir hacer estos procesos a lo largo de un eje (usando Numpy)

c= np.random.randint(100,size=(2,3))
v= np.arange(6).reshape(2,3)

def suma(x,y):
    while True:
        try:
            return np.add(x,y)
        except ValueError:
            print("Solo se permiten sumas con matrices de igual dimension")

def resta(x,y):
    while True:
        try:
            return np.subtract(x,y)
        except ValueError:
            print("Solo se permiten sumas con matrices de igual dimension")

def division():
    while True:
        try:
            return np.divide(v,c)
        except ValueError:
            print("Solo se permiten sumas con matrices de igual dimension")

# print(f"Matriz A= \n\n{c}\n\nMatriz B:\n{v}\n\nMatriz suma:\n\n{suma(c,v)}")

#7.) Buscar en Kaggle un archivo .csv relacionadas con alguna patología, descargar y hacer 
# funciones como las propuestas en el ítem anterior, pero implementándolas usando Pandas 
# y que permitan tambien elegir columnas.

def cargar(ruta):
    data= pd.read_csv(ruta)
    return data

def calcular_promedio(data, columna):
    promedio= data[columna].mean()
    return promedio

def filtrar_datos(data, columna, valor):
    datos_filtrados = data[data[columna] > valor]
    return datos_filtrados

def estadisticas_por_grupo(data, columna_grupo, columna_estadistica):
    grupo = data.groupby(columna_grupo)
    estadisticas_grupo = grupo[columna_estadistica].agg(['mean', 'sum', 'count'])
    return estadisticas_grupo

def visualizar_grafico(datos, columna_x, columna_y):
    plt.scatter(datos[columna_x], datos[columna_y])
    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.title("Gráfico de dispersión")
    plt.show()

#8.) Usar matplotlib para graficar la señal del archivo mat del punto 6 y crear funciones para 
# graficar histogramas, stems, barras, pies 


def graficar_señal_desde_mat(archivo_mat, nombre_variable):
    datos = sio.io.loadmat(archivo_mat)
    señal = datos[nombre_variable]
    plt.plot(señal)
    plt.xlabel('Tiempo')
    plt.ylabel('Amplitud')
    plt.title('Gráfico de la señal')
    plt.show()


def graficar_histograma(datos, bins=10):
    plt.hist(datos, bins=bins)
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    plt.show()

def graficar_stems(datos):
    plt.stem(datos)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfico de stems')
    plt.show()

def graficar_barras(categorias, valores):
    plt.bar(categorias, valores)
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de barras')
    plt.show()

def graficar_pastel(etiquetas, tamaños):
    plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%')
    plt.title('Gráfico de pastel')
    plt.show()
