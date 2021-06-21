print("""
# 
#  ----    1  ------
# Classes: decorador @property 
#
#""")
"""
Para usar un metodo como si fuera una variable usarmos el decorador @property.

Problema: la clase empleado, tiene una variable llamada: email
email, se crea con datos de inicializacion del objeto.
Si cambiamos una de las variables de inicializacion, el mail se mantendra igual
Para resolver el problema tendriamos que crear una funcion email(parecia a la func fullname)
El problema es que ahora la gente tendria que modificar su codigo para llamar a una funcion
"""
print ("Ejemplo de @property ")
"""

"""
class Empleado():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{self.first}.{self.last}@nelitoz.com".lower()

    def fullname(self):
        return f"{self.first} {self.last}"

    def __str__(self):
        return f"{self.fullname()} -- {self.mail}"

emp1 = Empleado("Daniel","Castillo",100)
print(emp1)
emp1.first = "Danielo"
print(emp1)

print ("-"*15)
print ("Con el uso de @property")
print ("-"*15)

class Empleado():
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def mail(self):
        return f"{self.first}.{self.last}@nelitoz.com".lower()

    def __str__(self):
        return f"{self.fullname()} -- {self.mail}"

emp1 = Empleado("Daniel","Castillo",100)
print(emp1)
emp1.first="Danilo"
print(emp1)


print("""
# 
#  ----    2  ------
# Classes: decorador @property con setter
#
#""")
"""
Se crea un decorador setter para cambiar variables.
El cliente setea el valor mediante la variable que exponse el decorador @property
"""
print ("Ejemplo de @property y setter")
"""

"""
class Empleado():
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @property
    def mail(self):
        return f"{self.first}.{self.last}@nelitoz.com".lower()

    def __str__(self):
        return f"{self.fullname} -- {self.mail}"


emp1 = Empleado("Daniel","Castillo",100)
print(emp1)
emp1.first="Danilo"
print(emp1)
print("Cambiando first y last desde fullname")
print(emp1.fullname)
emp1.fullname ="Waldo Williams"
print(emp1.fullname)
print(emp1)

print("""
# 
#  ----    3  ------
# Classes: decorador @property con deleter
#
#""")
"""
Implementaremos un deleter para el objeto
"""
print ("Ejemplo de @property y setter")
"""

"""
class Empleado():
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(" ")

    @fullname.deleter
    def fullname(self):
        self.first=None
        self.last=None
        print ("employee deleted")

    @property
    def mail(self):
        return f"{self.first}.{self.last}@nelitoz.com".lower()

    def __str__(self):
        return f"{self.fullname} -- {self.mail}"


emp1 = Empleado("Daniel","Castillo",100)
print(emp1)
emp1.first="Danilo"
print(emp1)
print("Cambiando first y last desde fullname")
print(emp1.fullname)
emp1.fullname ="Waldo Williams"
print(emp1.fullname)
print(emp1)
print("Usando el deleter")
del emp1.fullname
print(emp1)
