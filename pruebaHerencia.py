from persona import Persona 
from empleado import Empleado 
from empleadoasalariado import EmpleadoAsalariado 

p1=Persona("Laura")
print(p1.getNombre())
s1= EmpleadoAsalariado("Carlos", "mcdoanls", 100)
print(s1.getNombre())
print(s1.getSalario())

nombres2 = input("Ingrese el nombre del nuevo empleado:")
empresas2 = input("Ingrese la empresa del nuevo empleado: ")
salarios2 = int(input("Ingrese el salario del nuevo empleado: "))
s2 = EmpleadoAsalariado(nombres2, empresas2, salarios2)

print(s2)
print(s1)
print(p1)

personas = [p1, s1, s2]

for i in personas:
	print(i.getNombre())