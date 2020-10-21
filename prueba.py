import numpy as np
import matplotlib.pyplot as plt 
import ReinforcedPy as rp 

viga=rp.Elemento(1,2,3,4)
x=np.linspace(0,viga.longitud)
viga.generarDesdeCarga(5)
plt.plot(x,viga.M(x))
plt.plot(x,viga.V(x))
plt.show()
