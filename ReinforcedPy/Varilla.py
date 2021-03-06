from .Material import *
class Varilla():

	def __init__(self,material: Material,designacion: float):
		self.material=material
		self.designacion = designacion
		varillas = [{'A':-1,'D':-1},{'A':-1,'D':-1},{'A':32*10**-6,'D':6.4*10**-3},
		{'A':71*10**-6,'D':9.5*10**-3},{'A':129*10**-6,'D':12.7*10**-3},{'A':199*10**-6,'D':15.9*10**-3},
		{'A':284*10**-6,'D':19.1*10**-3},{'A':387*10**-6,'D':22.2*10**-3},{'A':510*10**-6,'D':25.4*10**-3},
		{'A':645*10**-6,'D':28.7*10**-3},{'A':819*10**-6,'D':32.3*10**-3},{'A':1006*10**-6,'D':35.8*10**-3},
		{'A':-1,'D':-1},{'A':-1,'D':-1},{'A':1452*10**-6,'D':43.0*10**-3},{'A':-1,'D':-1},{'A':-1,'D':-1},
		{'A':-1,'D':-1},{'A':2581*10**-6,'D':57.3*10**-3}]
		self.area=varillas[designacion]['A']
		self.diametro=varillas[designacion]['D']