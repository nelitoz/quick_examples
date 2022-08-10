
print("""
# 
#  ----    1  ------
# Void 1 - Funciones
#
#""")
def calc():
    print (2+2)

def saludo():
    print("Hola")

calc()
saludo()

print("""
# 
# ----    2   ------
# Functions return value
#
#""")

def calc():
    return 2+2

def saludo():
    return "hola"

resultado = calc()
sal = saludo()
print (resultado)
print(sal)

print("""
# 
# ----    3   ------
# funciones pre-build
#
#""")
print ("hola, estoy usando la funcion pre-build llamada 'print' ")

l = len('Daniel')
print (f"Cantidad de letras en el string 'daniel:'{l}",)

print("""
# 
# ----    4   ------
# funciones importadas
#
#""")
from pprint import pprint
pprint("hola, funcion pprint")

import math
sen_10 = math.sin(10)
print(sen_10)

import random
random_numer = random.randint(0,100)
print (random_numer)

from datetime import datetime
time_now = datetime.now()
print(time_now)
