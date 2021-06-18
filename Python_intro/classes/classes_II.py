print("""
# 
#  ----    1  ------
# Classes variables  de clase y variables de instancia
#
#""")
"""
"""
print ("Ejemplo de clase ")

class Empleado():
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.mail = f"{self.name}.{self.last}@nelitoz.com"

    def fullname(self):
        return f"{self.name} {self.last}"

    def set_raise(self):
        self.pay = self.pay*1.04


emp1 = Empleado("dan","cast", 100)
print (emp1.mail)
print (emp1.fullname())
print (emp1.pay)
emp1.set_raise()
print (emp1.pay)

"""
El problema con el codigo de arriba es que todos los empleados
recibiran el mismo salario.
Sacamos una variable de la clase que la puede consumir la funcion.
dicha variable tiene que ser consultada ya sea desde la instaci o de la clase
"""

print("""
# 
#  ----    2  ------
# Classes variables consultada desde la instancia
#
#""")
"""
"""
print ("Ejemplo de clase ")

class Empleado():

    raise_amount = 1.10
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.mail = f"{self.name}.{self.last}@nelitoz.com"

    def fullname(self):
        return (f"{self.name} {self.last}".lower())

    def set_raise(self):
        self.pay = self.pay * self.raise_amount

emp1 = Empleado("Daniel", "Castillo", 1000)
print(emp1.fullname())
print (emp1.pay)
emp1.set_raise()
print (emp1.pay)
print("""
# 
#  ----    2  ------
# Classes variables consultada desde la instancia
#
#""")
"""
"""
print ("Ejemplo de clase ")

class Empleado():

    raise_amount = 1.10
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.mail = f"{self.name}.{self.last}@nelitoz.com"

    def fullname(self):
        return (f"{self.name} {self.last}".lower())

    def set_raise(self):
        self.pay = self.pay * self.raise_amount

emp1 = Empleado("Daniel", "Castillo", 1000)
print(emp1.fullname())
print (emp1.pay)
emp1.set_raise()
print (emp1.pay)


print("""
# 
#  ----    3  ------
# Classes variables consultada desde la clase
#
#""")
"""
"""
print ("Ejemplo de clase ")

class Empleado():

    raise_amount = 1.10
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.pay = pay
        self.mail = f"{self.name}.{self.last}@nelitoz.com"

    def fullname(self):
        return (f"{self.name} {self.last}".lower())

    def set_raise(self):
        self.pay = self.pay * Empleado.raise_amount

emp1 = Empleado("Daniel", "Castillo", 1000)
print(emp1.fullname())
print (emp1.pay)
emp1.set_raise()
print (emp1.pay)