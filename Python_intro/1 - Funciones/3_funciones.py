print("""
# 
# First-Class 1 - Funciones 
#  
#  ----    1  ------
#  Las funciones pueden ser asignadas a una variable.
#  ahora, esa variable podra ejecutarse como la funcion
#""")


def add(x,y):
    return x+y

addition = add
print (addition(1,1))

print("""
# 
# First-Class 1 - Funciones 
#  
#  ----    2  ------
#  Pasar una funcion como argumento a otra funcion
#  
#""")

def square(x):
    return x**2

def my_calc(func, arg_list):
    result = []
    for number in arg_list:
        result.append(func(number))
    return result

square = my_calc(square,[1,2,3,4,5])
print (square)

print("""\n\n
# 
# First-Class 1 - Funciones 
#  
#  ----    3  ------
#  una funcion que retorna a otra funcion
#  
#""")

def logger(msg):
    def wrap_text():
        print (f"loggin message: {msg}")
    return wrap_text

log_x=logger("hello")
log_x()

def html(tag):

    def wrapper(msg):
        print (f"<{tag}>{msg}<\{tag}>")
    
    return wrapper

h1 = html("h1")
h1("Hola")

p = html("p")
p("esto es un paragraph")