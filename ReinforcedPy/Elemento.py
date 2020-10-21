class Elemento:								#TODO Clase viga

	def __init__ (self,base,altura,material,longitud): #TODO replantear parámetros (y la vida)
		self.base=base
		self.altura=altura
		self.material=material
		self.longitud=longitud
		self.area=base*altura
		self.inercia=base*altura**3/12
		self.rhoMin= 0.0033  				#TODO Cuantía mínima (revisión)
		self.rhoMax= 0.02833				#TODO Cuantía máxima
		self.recubrimiento=0.06				#TODO Debería importarse de geometria
		self.d=altura-self.recubrimiento	#Fibra a compresión (d)
	def generarDesdeCarga(self,w):
		self.M=lambda x:w*self.longitud/2*x-w*x**2/2
		self.V=lambda x:w*self.longitud/2-w*x

	def cuantiaRequerida(self,Mu,phi=0.9):
		