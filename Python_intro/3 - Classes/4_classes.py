print("""
# 
#  ----    1  ------
# Classes: static methods
#
#""")
"""
"""
print ("Ejemplo de static methods ")

"""
Ahora veremos el concepto de staticmethods.
Los instance methods, (los cuales son los metodos regulares) toman como primer argumento la instancia (self) 
Los class methods, toman como primer argumento a la clase(cls) 
Los static methods, no toman ni la instancia ni la clase como primer argumento 
Los static methods se usan cuando queremos darle una funcionalidad al objeto sin que necesariamente tengamos que modificar o usar variables del objeto
"""
import time
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

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True

import datetime
emp1 = Empleado("daniel","castillo", 100)
print(emp1.fullname())
my_day = datetime.date(2021, 6, 19)

print(emp1.is_workday(my_day))