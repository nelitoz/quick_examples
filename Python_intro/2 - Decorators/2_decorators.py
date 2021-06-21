print("""
# 
#  ----    1  ------
# Clase como decorador
#
#""")
class ClaseDecoradoraPadre(object):
    def __init__(self, funcion_hija):
        self.funcion_hija = funcion_hija
    def __call__(self, *args, **kwargs):
        print (f"buenas tardes")
        return self.funcion_hija(*args, **kwargs)

@ClaseDecoradoraPadre
def saludo1():
    print ("daniel")

@ClaseDecoradoraPadre
def saludo2(edad):
    print(f"soy Daniel y tengo {edad} ")

saludo1()
print("\n")
saludo2(40)

"""
Un decorador es una funcion padre, que toma a una funcion hijo como argumento.
el padre agrega una funcionalidad al hijo y retorna al hijo con dicha funcionalidad.
"""
#
# ----    2   ------
# Agregemos alguna funcionalidad para la funcion display
#
#""")
