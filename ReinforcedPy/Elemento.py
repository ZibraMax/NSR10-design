import numpy as np

class Elemento:								#TODO Clase viga

	def __init__ (self,base,altura,materiales,longitud): #TODO replantear parámetros (y la vida)
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
		self.recubrimiento=0.06				#TODO Debería importarse de geometria
		self.d=altura-self.recubrimiento	#Fibra a compresión (d)

	def generarDesdeCarga(self,w):
		self.M=lambda x:w*self.longitud/2*x-w*x**2/2
		self.V=lambda x:w*self.longitud/2-w*x

	def rhoReq(self,x,phi=0.9):
		fc = self.materiales[0].fc
		fy = self.materiales[1].fy
		pcuad = ((fc)/(1.18*fy))**2
		return (fc)/(1.18*fy)-np.sqrt(pcuad-(self.M(x)*fc*1000)/(0.59*phi*self.base*self.d**2*(fy*1000)**2))
		