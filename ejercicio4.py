class Animal:
    def comer(self):
        return f"El animal esta comiendo"
class Mamifero(Animal):
    def amamantar(self):
        return f"El mamifero esta amamantando"
class Ave(Animal):
    def volar(self):
        return f"El ave esta volando"
class Murcielago(Ave,Mamifero):
    pass


murcielago = Murcielago()
print(murcielago.volar())
print(murcielago.amamantar()) 
print(murcielago.comer())

print(Murcielago.mro())