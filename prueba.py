import numpy as np
import matplotlib.pyplot as plt 
import ReinforcedPy as rp 

concreto28 = rp.Concreto()
acero420 = rp.AceroRefuerzo()

viga=rp.Elemento(0.3,0.6,[concreto28,acero420],6)
viga.generarDesdeCarga(50)
x=np.linspace(0,viga.longitud)
plt.plot(x,viga.rhoReq(x),label='Cuantía Requerida')
plt.plot([0,viga.longitud],[viga.rhoMin,viga.rhoMin],label='Cuantía Mínima')
plt.plot([0,viga.longitud],[viga.rhoMax,viga.rhoMax],label='Cuantía Máxima')
plt.legend()
plt.grid()
plt.xlabel('Distancia [m]')
plt.ylabel(r'$\rho$')
plt.title('Gráfica de Cuantías')
plt.show()
print(acero420.varillas[0]['A'])


