from .Material import *
import math
class Concreto(Material):

	def __init__(self, fc=28, ec=0.0031,gamma=23.54):
		E = 4700000*math.sqrt(fc)
		v=0.2
		super().__init__(E,v,gamma)
		if fc<=28:
			self.b1 = 0.85
		elif fc>56:
			self.b1 = 0.65
		else:
			self.b1 = 0.85-0.05*(fc-28)/7

		self.fc = fc
		self.ec = ec
