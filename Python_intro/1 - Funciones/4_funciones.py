print("""
# 
# Closures 
#  
#  ----    1  ------
#  es una funcion "interna"  que recuerda y tiene acceso a variables en el scope donde fue creada
#  aun cuando la funcion "externa" ha terminado de ser ejecutada
#""")

def outer_func():
    message = "Mensaje definido en outter func"

    def inner_func():
        print (message)
    
    return inner_func

a = outer_func()
a()


print ("\n")
print ("#ahora con parametro definido en la outter func")

def outer(msg):
    message = msg

    def inner():
        print (message)
        print (msg)
    
    return inner

bye = outer("bye")
bye()

hi = outer("hi")
hi()


print ("\n")
print ("#ahora un ejemplo mas practico")

import logging
logging.basicConfig(filename='Python_intro/1 - Funciones/funciones_IV.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info(f"Running {func.__name__} with arguments {args}")
        print (func(*args))
    return log_func

def add(x,y):
    return x+y

def subs(x,y):
    return x-y

print ("suma")
logger_add = logger(add)
logger_add(1,2)

print ("resta")
logger_sub = logger(subs)
logger_sub(2,1)