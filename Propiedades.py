## Los setters y getters son la manera de acceder y modificar a atributos privados de una clase.

class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre 
        
    @property # Corresponde al getter.    
    def nombre(self):
        return self.__nombre
    
    @nombre.setter  ##Nombre corresponde al nombre de la funcion decorada definida en el @property
    def nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre
    
    @nombre.deleter  ##Nombre corresponde al nombre de la funcion decorada definida en el @property
    def nombre(self):
        del self.__nombre 
        
        
## Acceder a un metodo de una clase, es muy estresante cuando toca llamarlo con parentesis, porque hacerlo con parentesis, si podemos hacerlo como atributo de la clase agregandole simplemente el @property al metodo en cuestion.

## Para no tener acceso directo a la propiedad y generar un tipo de encapsulamiento, podemos usar los decoradores, asi el usuario nunca sabra que variable realmente esta usando  

eduard = Persona('Felipe')
print(eduard.nombre)

eduard.nombre = "Otro nombre"

print(eduard.nombre)

del eduard.nombre

print("holis")

## Ventajas de sintaxis, la sintaxis es mas limpia, permite encapsular logica adicional, logica es mas manejable, mayor flexibilidad en la evolucion del codigo, vuelven el codigo mas escalable.