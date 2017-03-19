from persona import Persona 
from empleado import Empleado 
from empleadoasalariado import EmpleadoAsalariado 

p1=Persona("Laura")
print(p1.getNombre())
s1= EmpleadoAsalariado("Carlos", "mcdoanls", 100)
print(s1.getNombre())
print(s1.getSalario())