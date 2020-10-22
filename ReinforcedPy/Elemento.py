import numpy as np
from .Seccion import *
from .Varilla import *

import matplotlib.pyplot as plt

class Elemento:								#TODO Clase viga
	def __init__ (self, base: float, altura: float, materiales: list, longitud: float,recubrimiento: float=0.06) -> object: #TODO replantear parámetros (y la vida)
		self.base=base
		self.altura=altura
		self.materiales=materiales
		self.longitud=longitud
		self.area=base*altura
		self.inercia=base*altura**3/12
		fc = self.materiales[0].fc
		fy = self.materiales[1].fy
		ec = self.materiales[0].ec
		ey = self.materiales[1].ey
		self.rhoMin = np.max([1.4/fy,0.25*np.sqrt(fc)/fy])
		self.rhoMax = 0.85*fc/fy*self.materiales[0].b1*ec/(ec+ey)
		self.recubrimiento=recubrimiento
		self.d=altura-self.recubrimiento	#Fibra a compresión (d)
		self.secciones = []

	def generarDesdeCarga(self, w: float):
		self.M=lambda x:w*self.longitud/2*x-w*x**2/2
		self.V=lambda x:w*self.longitud/2-w*x

	def _test_secciones(self):
		varillas = [{'X': 0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionApoyo = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=0,orientacion=-1)
		varillas = [{'X': 0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionTerciorsIzq = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=1/3,orientacion=-1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionTerciorsDer = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=1/3,orientacion=1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionLuzMediosIzq = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=0.5,orientacion=1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionLuzMediosDer = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=0.5,orientacion=1)

		self.secciones = [seccionApoyo,seccionTerciorsIzq,seccionTerciorsDer,seccionLuzMediosIzq]

		varillas = [{'X': 0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionApoyo = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=1,orientacion=-1)
		varillas = [{'X': 0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.54,'varilla': Varilla(self.materiales[1],8)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionTerciorsIzq = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=1-1/3,orientacion=-1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionTerciorsDer = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=1-1/3,orientacion=1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionLuzMediosIzq = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=0.5,orientacion=1)
		varillas = [{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base/2,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': (self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 2*(self.base+0.06)/3,'Y':0.06,'varilla': Varilla(self.materiales[1],4)},
		{'X': 0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)},
		{'X': self.base-0.06,'Y':0.06,'varilla': Varilla(self.materiales[1],8)}]
		seccionLuzMediosDer = Seccion(self.base,self.altura,varillas,self.materiales[0],posicion=0.5,orientacion=1)

		self.secciones+=[seccionLuzMediosDer,seccionTerciorsDer,seccionTerciorsIzq,seccionApoyo]
	
	def diagramaMomentoNominal(self):
		x = []
		y = []
		for seccion in self.secciones:
			x.append(self.longitud*seccion.posicion)
			y.append(seccion.momentoNominal())
		y = np.array(y)
		plt.plot(x,y[:,0])
		plt.plot(x,y[:,1])
		plt.legend([r'$Mn$',r'$\phi Mn$'])
		plt.grid()
		plt.title('Diagrama de resistencia a flexion')
		plt.show()

	def rhoReq(self,x: float, phi: float = 0.9) -> float:
		fc = self.materiales[0].fc
		fy = self.materiales[1].fy
		pcuad = ((fc)/(1.18*fy))**2
		return (fc)/(1.18*fy)-np.sqrt(pcuad-(self.M(x)*fc*1000)/(0.59*phi*self.base*self.d**2*(fy*1000)**2))
		