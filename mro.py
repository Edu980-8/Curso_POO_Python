
class C:
    pass
       
class E(C):
      def hablar(self):
        print("Hola desde E")
        
class B(E):
    pass
        
class D(E):
   pass

class F(E):
  pass

class A(B,D,F):
    pass
   
a = A()
print(A.mro())