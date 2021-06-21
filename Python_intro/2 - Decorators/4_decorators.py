print("""
# 
#  ----    1  ------
# Stacking decoradores
#
#""")
import time
import logging
from functools import wraps


def my_timer(original_func):
    @wraps(original_func)
    def wrapper_time(*args, **kwargs):
        t1 = time.time()
        result = original_func(*args, **kwargs)
        print (f"execution time for: {original_func.__name__}, function was:{time.time()- t1}")
        return result
    return wrapper_time

def my_log(original_func):
    logging.basicConfig(filename=f"{original_func.__name__}_IV.log", level=logging.INFO)

    @wraps(original_func)
    def wrapper_log(*args, **kwargs):
        logging.info(f"{original_func.__name__}, ran with args {args} and kwargs{kwargs}")
        return original_func(*args, **kwargs)
    return wrapper_log

@my_log
@my_timer
def display_info(name, age):
    time.sleep(2)
    print(f"soy {name} y tengo {age}")

display_info("Daniel", 40)
