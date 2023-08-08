class Gato():
    def  sonido(self):
        return "Miau"
class Perro():
    def  sonido(self):
        return "Guau"
def hacer_sonido(animal):
    print(animal.sonido())

gato = Gato()
perro = Perro()

print(gato.sonido()) #Estoy utilizando el mismo metodo .sonido, pero pasandole objetos diferentes bien sea gato o perro.
print(perro.sonido())

hacer_sonido(perro) # Polimorfismo de función: Le estoy pasando diferentes objetos a la funcion, pero esta respondiendo diferente
hacer_sonido(gato)


#Polimorfismo de sobrecarga, la funcion que se define actua dependiendo de la cantidad de parametros con los que cuente, en python no se utiliza eso, se utiliza mas en java.

#Polimorfismo de cohersion: Por ejemplo al sumar 2 + 3.5, python convierte ese 2 automaticamente en un 2.0 para poder sumarlo con el 3.5  y entregar un resultado flotante.

a=2
b=3.5
c= b+a
print(type(a))
print(type(b))
print(type(c)) 

##Estudiar Duck Typing, Enlaces dinamicos y estaticos, y tipo real y declarado.

## El duck typing se basa en lo que puede hacer el objeto y no en el tipo especifico la idea detrás del duck typing es que si un objeto camina como un pato, nada como un pato y grazna como un pato, entonces podemos considerarlo como un pato, sin importar su tipo real. Esto significa que no importa qué clase o tipo de objeto sea, siempre que pueda realizar las acciones que necesitamos, podemos trabajar con él como si fuera el tipo adecuado.

## En Python se puede utilizar el duck typing debido a que es un lenguaje de programación de tipado dinámico, no es necesario declarar explícitamente el tipo de una variable o un objeto. En su lugar, el tipo se determina en tiempo de ejecución según cómo se utilizan las operaciones y los métodos en ese objeto. 


# ENLACE ESTATICO ocurre en tiempo de compilación En lenguajes de programación estáticamente tipados como C++ o Java, se determina qué método se debe invocar en tiempo de compilación en función del tipo declarado de la variable o del objeto. La vinculación se resuelve basándose en la firma del método en la clase en la que se declara, y no se tiene en cuenta el tipo real del objeto en tiempo de ejecución. Esto significa que, una vez que el compilador ha decidido qué método debe invocarse, no cambiará durante la ejecución del programa.


##El enlace dinámico, también conocido como enlace tardío o enlace dinámico tardío, ocurre en tiempo de ejecución. En lenguajes de programación con enlace dinámico como C#, Python o Java (en algunos casos), la resolución del método se realiza teniendo en cuenta el tipo real del objeto al que se refiere la variable en tiempo de ejecución. Esto permite que las llamadas a métodos se resuelvan en función de la implementación de la clase específica a la que pertenece el objeto, y no solo en función del tipo declarado de la variable.