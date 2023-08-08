
class Persona():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def imprimir(self):
        print(f"El nombre de la persona es {self.nombre} y la edad es {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def imprime_grado(self):
        print(f"El grado del estudiante es {self.grado}")
        
estudiante = Estudiante("Jaime",24,"Tercero")
estudiante.imprime_grado()
estudiante.imprimir()