import numpy as np
import matplotlib.pyplot as plt 
import ReinforcedPy as rp 
import matplotlib.patches as mpatches

concreto28 = rp.Concreto()
acero420 = rp.AceroRefuerzo()

viga=rp.Elemento(0.3,0.6,[concreto28,acero420],6)
viga.generarDesdeCarga(50)
viga._test_secciones()
viga.diagramaMomentoNominal()
viga.secciones[0].dibujar()
