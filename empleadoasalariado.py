from empleado import Empleado

class EmpleadoAsalariado(Empleado):

	def __init__(self, nombre, empresa, salario):
		super().__init__(nombre, empresa)
		self._salario = salario
	

	def getSalario(self):
		return self._salario

	def setSalario(self, salario):
		self._salario = salario

	def __str__(self):
		return (super().__str__() + "\nSalario: " + str(self._salario))