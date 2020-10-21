from .Material import *
class AceroRefuerzo(Material):

	def __init__(self, fy = 420,ey=0.0021):
		E = 200000000
		v = 0.23 #TODO Corregir
		super().__init__(E,v,gamma=0)
		self.ey = ey
		self.fy = fy
		
