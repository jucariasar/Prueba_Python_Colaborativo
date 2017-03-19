from persona import Persona

class Empleado(Persona):
	def __init__(self, nombre, empresa):
		super().__init__(nombre)
		self._empresa = empresa

	def getEmpresa(self):
		return self._empresa

	def setEmpresa(self, empresa):
		self._empresa=empresa

	def __str__(self):
		return (super().__str__() + "\nEmpresa: " + self._empresa)