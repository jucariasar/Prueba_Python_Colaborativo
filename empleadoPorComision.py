from empleado import Empleado

class EmpleadoPorComision(Empleado):
	def __init__(self, nombre, empresa, totalVentas, comision):
		super().__init__(nombre, empresa)
		self._totalVentas = totalVentas
		self._comision = comision

	def getTotalVentas(self):
		return self._totalVentas

	def setTotalVentas(self, ventas):
		self._totalVentas = ventas

	def getComision(self):
		return self._comision

	def setComision(self, comision):
		self._comision = comision

	def salarioTotal(self):
		return (self.getTotalVentas() + float(self.getTotalVentas() * self.getComision()))

	def __str__(self):
		return (super().__str__() + "\nTotal Ventas: " + str(self._totalVentas) + 
			"Comision: " + str(self._comision) + "Salario Total: " + self.salarioTotal())