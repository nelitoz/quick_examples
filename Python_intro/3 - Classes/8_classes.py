print("""
# 
#  ----    1  ------
# Classes: Clases abstractas 
#
#""")
"""
Una clase abstracta es una clase que contiene funciones sin cuerpo. 
La razon de estas clases abstractas es definir un perfil para otras sub-classe, 
dicho perfil tendra definidos los metodos que las subclases deberan usar. 
Por otro lado, la clase abstracta no debe ser instanciada individualmente. 
"""
print ("Ejemplo de Abstraccion ")
"""

"""
class Shape():
    def area(self):pass
    def perimeter(self):pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4

    def __repr__(self):
        return f"Square({self.side})"

cuerpo = Shape()
cuadrado = Square(5)
print (cuadrado.area())
print (cuadrado.perimeter())

print("""
# 
#  ----    2  ------
# Classes: Clases abstractas 
#
#""")
"""

En realidad Python no soporta por default el concepto de abstract 3 - Classes.
regla de abstracciones: La clase abstracta no se puede instanciar 
Esta se rompe porque el objeto cuerpo es una instancia de la clase Shape 
Para convertir una clase normal, a una clase abstracta, usamos al modulo abc

"""
print ("Ejemplo de Abstraccion con el modulo ABC ")
"""
"""
from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):pass

    @abstractmethod
    def perimeter(self):pass

class Square(Shape):
    def __init__(self,side):
        self.side = side

    def area(self):
        return self.side**2

    def perimeter(self):
        return self.side*4

    def __repr__(self):
        return f"Square({self.side})"

# nos daria un type error si ejecutamos la line ade abajo
#cuerpo = Shape()

cuadrado = Square(6)
print (cuadrado.area())
print (cuadrado.perimeter())

# Si quiciera instanciar una clase hija que no tenga definidos los metodos
# de la clase padre, tendriamos un error