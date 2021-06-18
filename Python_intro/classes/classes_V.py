print("""
# 
#  ----    1  ------
# Classes: Herencia
#
#""")
"""
"""
print ("Ejemplo de herencia ")

"""
Tenemos 2 clases  hijas (Dev, Rh)
Tendremos una clase padre (Empleado)
Las clases hijas heredan la estructura de la clase padre
"""

class Empleado():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{self.first}.{self.last}@nelitoz.com"

    def fullnaname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

class Dev(Empleado):
    pass

class RH(Empleado):
    pass

emp1 = Dev("Daniel", "Castillo", 100)
emp2 = RH("Pedro","Paramo",100)

print(emp1.fullnaname())
print(emp1.pay)
print(emp2.fullnaname())
print(emp2.pay)

print("subiendo cuota de aumento")
Dev.raise_amount=1.10
emp1.apply_raise()
emp2.apply_raise()

print(emp1.fullnaname())
print(emp1.pay)
print(emp2.fullnaname())
print(emp2.pay)

print(f"monto aumento empleado: {Empleado.raise_amount}")
print(f"monto aumento Dev: {Dev.raise_amount}")
print(f"monto aumento RH: {RH.raise_amount}")


print("""
# 
#  ----    2  ------
# Classes: Herencia, 
#
#""")
"""
"""
print ("Ejemplo de herencia sobre-escribiendo variable en hijo ")

"""
Dev class tiene una neceisdad particual que no tiene RH
de este modo, modificaremos a Dev, de tal forma que el cambio solo aplique para las instancias 
de esta clase
"""

class Empleado():

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{self.first}.{self.last}@nelitoz.com"

    def fullnaname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

class Dev(Empleado):
    raise_amount = 1.10

class RH(Empleado):
    pass


emp1 = Dev("Daniel", "Castillo", 100)
emp2 = RH("Pedro","Paramo",100)

print(emp1.fullnaname())
print(emp1.pay)
print(emp2.fullnaname())
print(emp2.pay)
print("Subiendo el sueldo a cada empleado")
emp1.apply_raise()
emp2.apply_raise()

print(emp1.fullnaname())
print(emp1.pay)
print(emp2.fullnaname())
print(emp2.pay)

print(f"monto aumento empleado: {Empleado.raise_amount}")
print(f"monto aumento Dev: {Dev.raise_amount}")
print(f"monto aumento RH: {RH.raise_amount}")


print("""
# 
#  ----    3  ------
# Classes: Aumentar datos de inicializacion de una clase hija, 
#
#""")
print ("Ejemplo de herencia cuando el hijo agrega mas variables de inicializacion")

"""
Algunas veces vamos a querer inicializar nuestras clases especificas con 
mas informacion que la clase padre.
"""

class Empleado():
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{self.first}.{self.last}@nelitoz.com"

    def fullnaname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

#ahora definira el lenguaje de programacion que maneja
class Dev(Empleado):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lag):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lag

    def __repr__(self):
        return str(self.__dict__)

class RH(Empleado):
    pass


emp1 = Dev("Daniel", "Castillo", 100, "PY")
emp2 = Dev("Leinad","Ragnarok",100, "JS")

print (emp1)
print (emp2)


print("""
# 
#  ----    4  ------
# Classes: Ejemplo mas avanzado, 
#
#""")
print ("Ejemplo mas avanzado")

"""
Creamos una nueva clase
Aumentamos sus parametros iniciales default
Aumentamos las funciones iniciales default
"""
class Empleado():
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.mail = f"{self.first}.{self.last}@nelitoz.com"

    def fullnaname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount


class Dev(Empleado):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lag):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lag

    def __repr__(self):
        return str(self.__dict__)


class Manager(Empleado):
    raise_amout = 1.15

    def __init__(self, first, last, pay, managed_people=None):
        super().__init__(first, last, pay)
        if managed_people == None:
            self.managed_people = []
        else:
            self.managed_people = managed_people

    def remove_people(self, dude):
        self.managed_people.remove(dude)
        print(f"{dude}, was removed")

    def append_people(self, dude):
        self.managed_people.append(dude)
        print(f"{dude}, was added")

    def show_people(self):
        return (self.managed_people)

    def __repr__(self):
        return str(self.__dict__)

deve1 = Dev("Daniel", "Castillo", 10, "PY")
deve2= Dev("Leinad", "Rag", 10, "JS")
manager_team1 = Manager("Otoniel","Melgarejo",110)

print(deve1)
print(deve2)
print(manager_team1)
manager_team1.append_people(deve1)
manager_team1.append_people(deve2)
manager_team1.remove_people(deve1)

print("="*10)
print("second team")
print("="*10)
deve3 = Dev("Lucas", "Kruger", 10, "PY")
deve4= Dev("Jason", "Fox", 10, "JS")
manager_team2 = Manager("Larry","Smith",110,[deve3,deve4])
print(manager_team2)