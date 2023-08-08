class MiClase:
    def  __init__(self):
        self._atributo_privado = "Valor"
        self.__atributo_muy_privado = "Valor 2"
objeto = MiClase()
print(objeto._atributo_privado) # El simbolo "_" define un atributo privado, es decir, puede accederse desde la clase pero tiene un cierto nivel de privacidad.
print(objeto.__atributo_muy_privado) # El simbolo "__" define un atributo muy privado, es decir, no se puede acceder con el objeto.atributo, sino que se debe accesar mediante el uso de setters y getters.