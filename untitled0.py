
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#x= np.arange(0,51)
#y=np.radians(x)

#plt.plot(x,np.random.randn(51))



#a= np.arange(0,59 )
#print(a)


dict_data= {"edad":[20,21,22,23,24],
            "cm":[110,112,113,114,115],
            "pais":["co","mx","ee.uu","co","arg"],
            "genero":["M","M","F","F","M"],
            "Q1":[5,10,12,14,7 ],
            "Q2":[7,9,9,8,7]
            }

df= pd.DataFrame(dict_data)

v=df.groupby(["genero"]).mean()
print(v)

