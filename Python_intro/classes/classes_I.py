print("""
# 
#  ----    1  ------
# Classes
#
#""")
"""
Un decorador es una funcion padre, que toma a una funcion hijo como argumento.
el padre agrega una funcionalidad al hijo y retorna al hijo con dicha funcionalidad.
"""
print ("Ejemplo de clase vacia")
class Empleado():
    pass
emp1 = Empleado()
emp2 = Empleado()

emp1.first = "Daniel"
emp1.last = "Castillo"
emp1.email = "dacasti2@nelitoz.com"
emp1.pay = "800000"

emp2.first = "l0k1"
emp2.last = "Ragnarok"
emp2.email = "l0k1@nelitoz.com"
emp2.pay = "900000"

print (emp1.first)
print (emp2.first)

"""
La desventaja con lo de arriba es que se genera mucho codigo.
"""

print("""
# 
#  ----    2 ------
# Classes
# Ejemplo de clase con inicializacion
#""")
"""
"""

class Empleado():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

emp1 = Empleado("Daniel","Castillo",200000)
emp2 = Empleado("Jacobo","Martinez",150000)

print (emp1.pay)
print (emp2.pay)

print("""
# 
#  ----    3 ------
# Classes
# Ejemplo de clase con una funcionalidad
#""")
"""
"""
class Empleado():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

emp1 = Empleado("l0k","rag",10)
print (emp1.pay)
print(emp1.fullname())
