import numpy as np
import matplotlib.pyplot as plt 
import ReinforcedPy as rp 
import matplotlib.patches as mpatches

coordenadasY=0.54
concreto28 = rp.Concreto()
acero420 = rp.AceroRefuerzo()
varillas = [{'X': 0.06,'Y':0.54,'varilla': rp.Varilla(acero420,6)}]*9+[{'X': 0.06,'Y':0.54,'varilla': rp.Varilla(acero420,6)}]


viga=rp.Elemento(0.3,0.6,[concreto28,acero420],6)
viga.generarDesdeCarga(50)
# x=np.linspace(0,viga.longitud)
# plt.plot(x,viga.rhoReq(x),label='Cuantía Requerida')
# plt.plot([0,viga.longitud],[viga.rhoMin,viga.rhoMin],label='Cuantía Mínima')
# plt.plot([0,viga.longitud],[viga.rhoMax,viga.rhoMax],label='Cuantía Máxima')
# plt.legend()
# plt.grid()
# plt.xlabel('Distancia [m]')
# plt.ylabel(r'$\rho$')
# plt.title('Gráfica de Cuantías')

seccion = rp.Seccion(0.3,0.6,varillas,concreto28,orientacion=-1)
# print(seccion.encontrarC())
#print(seccion.momentoNominal())
seccion.dibujar()
