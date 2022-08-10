print("""
# 
#  ----    1  ------
# Decoradores
#
#""")
"""
Un decorador es una funcion padre, que toma a una funcion hijo como argumento.
el padre agrega una funcionalidad al hijo y retorna al hijo con dicha funcionalidad.
"""

def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function

def display():
    print ("display function ran")

decoreated_display = decorator_function(display)
decoreated_display()

print("""
# 
# ----    2   ------
# Agregemos alguna funcionalidad para la funcion display
#
#""")


def decorator_function(original_function):
    def wrapper_function():
        print("agregando funcionalidad")
        return original_function()
    return wrapper_function

def display():
    print("This is display function")

decoreated_display = decorator_function(display)
decoreated_display()


print("""
# 
# ----    3   ------
# Evaluando sintaxis mas comun para decoradores
#
#""")

def funcion_padre(funcion_hija):
    def wrapper():
        print ("buenas tardes")
        return funcion_hija()
    return wrapper

@funcion_padre
def func_x():
    print ("Soy daniel")

#decodara = funcion_padre(func_x)
#decodara()
func_x()

print("""
# 
# ----    4   ------
# la funcion hija pasando parametros
# cuidado porque el wrapper no tiene nada que pasarle a la funcion hija
#""")


def funcion_padre(funcion_hija):
    def wrapper(*args, **kwargs):
        print ("Buenas tardes")
        return funcion_hija(*args, **kwargs)
    return wrapper

@funcion_padre
def saludo1():
    print ("soy Daniel")

@funcion_padre
def saludo2(edad):
    print (f"soy Daniel, mi edad es {edad}")

saludo1()
print ("\n")
saludo2(40)