class Material():
	def __init__(self, E, v, gamma):
		self.E = E
		self.v = v
		self.gamma = gamma
		self.G = self.E/2/(1+self.v)
