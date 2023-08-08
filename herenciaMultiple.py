class Persona:
    def  __init__(self, nombre,edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("Hola estoy hablando un poco")

class Artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def  mostrar_habilidad(self):
        print(f"Mi habilidad es: {self.habilidad}")
        
#Herencia Multiple, Empleado artista hereda nombre, edad y nacionalidad de Persona y Habilidad de la clase artista, ademas define sus propios Atributos.        

class EmpleadoArtista(Persona,Artista):## Se tiene prioridad de herencia en persona, es decir, si existiesen dos metodos llamados igual, tomaria la definicion de la clase persona y luego la de artista. MRO(Method Resolution order)
    def __init__(self,nombre,edad,nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre,edad,nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario = salario
        self.empresa = empresa
    def presentarse(self):
        return f"{super().mostrar_habilidad()}" # Estoy llamando al mostrar habilidad del metodo padre, en este caso de Artista
        
andres = EmpleadoArtista('Andres',69,'Colombiano','Programar','Programador',3000)
andres.presentarse()

#Me entrega true, porque Empleado artista es una subclase de persona
herencia = issubclass(EmpleadoArtista,Persona)
print(herencia)

#Me entrega false, porque persona no  es  una subclase de Empleado artista (Porque es el padre) 
herencia = issubclass(Persona,EmpleadoArtista)
print(herencia)