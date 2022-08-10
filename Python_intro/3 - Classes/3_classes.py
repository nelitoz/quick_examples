print("""
# 
#  ----    1  ------
# Classes: class methods
#
#""")
"""
"""
print ("Ejemplo de class method ")

"""
los metodos dentro de una clase, toman el nombre de la instancia como primer argumento. 
En este caso, nos gustaria que el metodo set_raise_amount tomen el nombre de la clase como primer argumento. 
Para esta tarea usamos al decorador @classmethod
"""


class Empleado():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{first}.{last}@nelitoz.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay* self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


emp1 = Empleado("daniel","castillo",100)
print (emp1.mail)
print (emp1.fullname())
print (emp1.pay)
emp1.apply_raise()
print (emp1.pay)

print("subiendo el aumento salarial mediante la clase")
Empleado.set_raise_amount(1.50)
emp1.apply_raise()
print (emp1.pay)

print("subiendo el aumento salarial mediante la instancia de la clase")
emp1.set_raise_amount(1.55)
emp1.apply_raise()
print (emp1.pay)

print("Comprobamos que el valor cambio para toda la clase y para objetos asociados")

emp2 = Empleado("david","bowie",100)
print(emp2.first)
print (emp2.pay)
print (emp2.raise_amount)
emp2.apply_raise()
print (emp2.pay)

print("""
# 
#  ----    2  ------
# Classes: class methods
#
#""")
"""
"""
print ("Ejemplo de class method como un constructor")

"""
problem: es probable que la data para inicializar un empleado, venga en otro formato.
Solucion: usaremos un class method para leer la data, parsear la data y retornar una instancia de la clase
"""

class Empleado():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{first}.{last}@nelitoz.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay* self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, string_data):
        first, last, pay=string_data.split("-")
        return cls(first,last,int(pay))

emp1_data_string = "daniel-castillo-100"
emp2_data_string = "david-bowie-200"

emp1=Empleado.from_string(emp1_data_string)
emp2=Empleado.from_string(emp2_data_string)

print(emp1.first)
print (emp1.pay)
print (emp1.raise_amount)
emp2.apply_raise()
print (emp1.pay)


print(emp2.first)
print (emp2.pay)
print (emp2.raise_amount)
emp2.apply_raise()
print (emp2.pay)