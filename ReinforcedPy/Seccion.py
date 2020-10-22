import numpy as np
class Seccion():
	def __init__(self,b,h,varillas,concreto,orientacion=1):
		self.varillas = varillas
		self.b = b
		self.h = h
		self.concreto = concreto
		self.orientacion = orientacion
		if self.orientacion == -1:
			for barra in self.varillas:
				barra['Y']=self.h-barra['Y']

	def cargaAxial(self, c, compresion=False):
		self.deformaciones(c)
		pc = -0.85*(self.concreto.fc*1000)*self.b*self.concreto.b1*c
		ps = 0
		for varilla in self.varillas:
			var = varilla['varilla']
			if compresion:
				ps += var.area*var.material.E*varilla['e']
			else:
				ps += (varilla['e']>0)*var.area*varilla['f']
		return ps+pc

	def momento(self, c, compresion=False):
		self.deformaciones(c)
		a = self.concreto.b1*c
		mc = 0.85*(self.concreto.fc*1000)*self.b*a*(self.h/2-a/2)
		ms = 0
		for varilla in self.varillas:
			var = varilla['varilla']
			if compresion:
				ms += var.area*var.material.E*varilla['e']*(self.h/2-varilla['Y'])
			else:
				ms += (varilla['e']>0)*var.area*varilla['f']*(self.h/2-varilla['Y'])
		return ms+mc

	def calcularPhi(self):
		deformaciones = []
		for varilla in self.varillas:
			deformaciones.append(varilla['e'])
		et = np.max(deformaciones)
		if et>0:
			if et<=0.002:
				return 0.65
			elif et<0.005:
				return 0.65 + (et-0.002)*250/3
			else:
				return 0.9
		else:
			return -1
	def deformaciones(self,c):
		for varilla in self.varillas:
			#varila = {'X':x,'Y':y,'varilla':Varilla}
			coordX = varilla['X']
			coordY = varilla['Y']
			ecu = self.concreto.ec
			ey = varilla['varilla'].material.ey
			dv = self.h-c-coordY
			varilla['e'] = ecu/c*dv
			if np.abs(varilla['e']) >= ey:
				varilla['f'] = varilla['varilla'].material.fy*1000*varilla['e']/np.abs(varilla['e'])
			else:
				varilla['f'] = varilla['varilla'].material.E*varilla['e']
		self.phi = self.calcularPhi()

	def encontrarC(self):
		x0 = 0.000001
		xf = self.h
		xr = (xf +x0)/2
		for i in range(100):
			fx0 = self.cargaAxial(x0)
			fxf = self.cargaAxial(xf)
			fxr = self.cargaAxial(xr)
			if fx0*fxr < 0:
				xf = xr
			else:
				x0 = xr
			xr = (xf +x0)/2
		return xr

	def momentoNominal(self):
		c = self.encontrarC()
		Mn = self.momento(c)
		return Mn,Mn*self.phi




		