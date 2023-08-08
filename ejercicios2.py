class Estudiante():
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando....")
    def trabajar(self):
        if self.edad >=18:
            print(f"El estudiante {self.nombre} esta trabajando....")
        else:
            print(f"El estudiante {self.nombre} no tiene edad para trabajar...")

nombre = input("Dame tu nombre: ")
edad = int(input("Dame tu edad: "))
grado = input("Dame tu grado: ")

estudiante1 = Estudiante(nombre,edad,grado)

while True:
    x = input("Que quieres que el estudiante haga?: ").lower()
    if x == "estudiar":
        estudiante1.estudiar()
    elif x == "trabajar":
        estudiante1.trabajar()
    elif x =="quit":
        break;
    else:
        print(f"El estudiante {estudiante1.nombre} no puede {x}")