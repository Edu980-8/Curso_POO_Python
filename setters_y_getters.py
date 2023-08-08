## Los setters y getters son la manera de acceder y modificar a atributos privados de una clase.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre 
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre

eduard = Persona('Felipe')
print(eduard.get_nombre())

eduard.set_nombre("Julian")
print(eduard.get_nombre())

## Para evitar toda esta mano de codigo, Python creo algo hermoso, que se llama los decoradores.
