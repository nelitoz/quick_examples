import time

print("""
# 
#  ----    1  ------
# ejemplo 1 de caso de uso para decorator
#
#""")

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)
    def wrapper(*args, **kwargs):
        logging.info(f"{orig_func.__name__}, ran with args {args} and kwargs{kwargs}")
        return orig_func(*args, **kwargs)
    return wrapper

def display():
    print ("soy Daniel")

def display_info(name, age):
    print (f"hola, soy {name} y tengo {age}")

print ("funciones hijas sin ser decoradas")
display()
display_info("Daniel", 40)
print("\n")

print ("funciones hijas decoradas")

@my_logger
def display():
    print ("soy Daniel")
@my_logger
def display_info(name, age):
    print (f"hola, soy {name} y tengo {age}")


display()
display_info("Daniel", 40)

print("""
# 
#  ----    2  ------
# ejemplo 2 de caso de uso para decorator
#
#""")

def my_timer(original_func):
    import time
    def wrapper(*args, **kwargs):
        initial_time = time.time()
        result = original_func(*args, **kwargs)
        total_time = time.time()-initial_time
        print(f"{original_func.__name__}, ran in {total_time}")
        return result
    return wrapper

@my_timer
def display():
    time.sleep(1)
    print ("Daniel")

@my_timer
def display_info(name, edad):
    time.sleep(3)
    print(f"mi nombre es {name} y tengo {edad}")


display()
display_info("Daniel",40)

