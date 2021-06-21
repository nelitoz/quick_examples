print("""
# 
#  ----    1  ------
# Classes: Special methods
#
#""")
"""
La funcion de __str__ es se legible para el end-user
"""
print ("Ejemplo de __str__ ")
"""

"""
class Empleado():
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()
    def fullname(self):
        return (f"{self.first} {self.last}")
    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

emp1 = Empleado("Daniel", "Castillo", 100)
print(emp1)
#redefiniendo la clase para agregar el __str__
class Empleado():

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

    def __str__(self):
        #return str(self.__dict__)
        return self.fullname()
        #return f"Empleado('{self.first}', '{self.last}',{self.pay})"

emp1 = Empleado("Daniel", "Castillo", 100)
print(emp1)

print("""
# 
#  ----    2  ------
# Classes: Special methods
#
#""")
"""
La funcion de __repr__ es quitar ambiguedad al objeto
Usualmente representa un comando que pudieramos meter en el interprete
Es util principalmente como ayuda para el programador
Si tengo __repr__ y __str__, este ultimo tomara precedencia
"""
print ("Ejemplo de __repr__ ")
"""

"""
class Empleado():
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

emp1 = Empleado("Luis", "Martinez", 100)
print(emp1)
#redefiniendo la clase para agregar el __repr__
class Empleado():

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

    def __repr__(self):
        return f"Empleado('{self.first}', '{self.last}',{self.pay})"

emp1 = Empleado("Daniel", "Castillo", 100)
print(emp1)

print("""
# 
#  ----    3  ------
# Classes: Special methods
#
#""")
"""
La funcion de __add__ es se legible para el end-user
"""
print ("Ejemplo de __add__ ")
"""
"""
class Empleado():

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

    def __repr__(self):
        return f"Empleado('{self.first}', '{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.fullname()}, -- {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Empleado("Daniel", "Castillo", 100)
emp2 = Empleado("Leinad", "Castro", 120)

print (emp1+emp2)
print("""
# 
#  ----    3  ------
# Classes: Special methods
#
#""")
"""
La funcion de __add__ sirve para poder sumar valores del objeto con otro objeto
"""
print ("Ejemplo de __add__ ")
"""
"""
class Empleado():

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

    def __repr__(self):
        return f"Empleado('{self.first}', '{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.fullname()}, -- {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

emp1 = Empleado("Daniel", "Castillo", 100)
emp2 = Empleado("Leinad", "Castro", 120)

print (emp1+emp2)

print("""
# 
#  ----    3  ------
# Classes: Special methods
#
#""")
"""
La funcion de __len__ define la longuitud de algun elemento del objeto
"""
print ("Ejemplo de __len__ ")
"""
"""
class Empleado():

    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return (f"{self.first} {self.last}")

    def raise_salary(self):
        self.pay = self.pay*self.raise_amount
        print ("Salary increase")

    def __repr__(self):
        return f"Empleado('{self.first}', '{self.last}',{self.pay})"

    def __str__(self):
        return f"{self.fullname()}, -- {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp1 = Empleado("Daniel", "Castillo", 100)
emp2 = Empleado("Leinad", "Castro", 120)
print(len(emp1))
print(len(emp2))