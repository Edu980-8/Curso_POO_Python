class Celular_Fijo():
    marca = "Samsung"
    modelo = "s23"
    camara = "48mp"

class Celular:
    def __init__(self, marca, modelo, camara): #Esto es el constructor
        self.marca=marca
        self.camara=camara
        self.modelo=modelo
    
    def llamar(self): #Es necesario usar el parametro self en la clase, porque asi se auto referencia el objeto
        print(f"Estas llamando desde un {self.modelo}") 
    
    def colgar(self):
        print(f"Estas colgando desde un {self.modelo}") 
    

celular1 = Celular_Fijo()
print(celular1.camara)

celular2 = Celular("Motorola","g23","12mp")
print(celular2.modelo)
celular2.llamar()
celular2.colgar()


