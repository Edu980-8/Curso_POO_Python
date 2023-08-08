def decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcion_modificada


@decorador
def saludo():
    print("Hola eduard")
    
saludo()

## Un decorador es una funcion que le agrega funcionalidad a otra funcion (antes y/o despues de ejecutarla) sin modificar la funcion inicial:) Sirve para hacer validaciones por ejemplo.

## Decoradores de clases, decoradores multiples 