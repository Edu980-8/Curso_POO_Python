## Creo una plantilla que no se puede instanciar, pero a partir de alli heredo todas las subclases. Ventajas: Seguridad y fomento del polimorfismo.

from abc import ABC,abstractclassmethod

# Esta es la clase abstracta, ya que no la puedo instanciar, solo la puedo usar como padre
class  Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
    @abstractclassmethod 
    def hacer_actividad(self):
        pass
    def  presentarse(self):
        print(f"Hola me llamo {self.nombre} y tengo {self.edad} años.")

## Esta es la clase que hereda la clase abstracta

class Estudiante(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}")
        
class Trabajador(Persona):
    def __init__(self,nombre,edad,sexo,actividad):
        super().__init__(nombre,edad, sexo, actividad)
    def hacer_actividad(self):
        print(f"Estoy trabajando en: {self.actividad}")

eduard = Trabajador("Eduard",24,"Masculino","Desarrollador de Software")
eduard.presentarse()
eduard.hacer_actividad()
diego = Estudiante("Diego",18,"Masculino","Ingenieria Industrial")
diego.presentarse()
diego.hacer_actividad()

## Al hacer una clase abstracta estoy obligando a los demas programadores a usar todos los metodos de esa clase, estoy estableciendo una especie de contrato o interfaz que las subclases concretas deben cumplir. Esto significa que estoy definiendo una estructura que obliga a los demás programadores a implementar todos los métodos abstractos en las subclases para que puedan ser instanciadas correctamente.

## Evita errores y FOMENTA EL POLIMORFISMO.