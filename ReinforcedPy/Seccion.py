import math
class Seccion():
	def __init__(self,b,h,varillas,concreto):
		self.varillas = varillas
		self.b = b
		self.h = h
		self.concreto = concreto

	def cargaAxial(self, c, compresion=False):
		self.deformaciones(c)
		pc = -0.85*(self.concreto.fc)*self.b*self.concreto.b1*c
		ps = 0
		for varilla in self.varillas:
			var = varilla['varilla']
			if compresion:
				ps += var.area*var.material.E*varilla['e']
			else:
				ps += (varilla['e']>0)*var.area*varilla['f']
		return ps+pc

	def deformaciones(self,c):
		for varilla in self.varillas:
			#varila = {'X':x,'Y':y,'varilla':Varilla}
			coordX = varilla['X']
			coordY = varilla['Y']
			ecu = self.concreto.ec
			ey = varilla['varilla'].material.ey
			dv = self.h-c-coordY
			varilla['e'] = ecu/c*dv
			if math.abs(varilla['e']) >= ey:
				varilla['f'] = 420*varilla['e']/math.abs(varilla['e'])
			else:
				varilla['f'] = varilla['varilla'].material.E*varilla['e']

	def encontrarC(self):
		x0 = 0.000001
		xf = self.h
		xr = (xf +x0)/2
		for i in range(100):
			fx0 = cargaAxial(x0)
			fxf = cargaAxial(xf)
			fxr = cargaAxial(xr)
			if fx0*fxr > 0:
				x0 = xr
				xf = xf
			else:
				x0 = x0
				xf = xr

	def momentoNominal(self):
		#EncontrarC
		pass



		