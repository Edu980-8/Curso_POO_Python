# Herencia simple

class Persona:
    def  __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print(f"Hola soy {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.nacionalidad}")

class Empleado(Persona):
    def __init__(self, nombre,apellido, edad, nacionalidad, trabajo, salario):
        super().__init__(nombre, apellido, edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
class Estudiante(Persona):
    def __init__(self, nombre,apellido, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, apellido, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
    
        
camilo = Empleado("Camilo","Perez", 24, "Colombiano", "Programador", 3500000)
julian = Estudiante("Julian", "Alvarez",13,"Argentino", 2.8, "Harvard University")
camilo.hablar()
julian.hablar()
print(julian.universidad)