## Aqui ya hay abstraccion, ya que el usuario final solo ve el metodo conducir, pero no le muestro internamente lo que contienen los demás metodos, como encender  el usuario no necesita preocuparse por cómo se implementa el encendido internamente, ya que eso está oculto detrás del método encender(). Esto cumple con el principio de abstracción, ya que se simplifica la interacción con la clase y se ocultan los detalles internos.

#abstraccion, ocultar la complejidad interna de un sistema.

class Auto():
    def __init__(self, marca,velocidad):
        self.estado = "apagado"
        self.marca = marca
        self.velocidad = velocidad
    def encender(self):
        self.estado = "encendido"
        print(f"El auto {self.marca} esta encendido")
    def conducir(self):
        if self.estado == "apagado":
            self.encender()
        print(f"Conduciendo un {self.marca} lo llevare de 0 a {self.velocidad} km/h")
        
mi_auto = Auto("Ferrari",1000)
mi_auto.conducir()
        
        
        