print("""
# 
#  ----    1  ------
# Functions parameters
#
#""")

print("con parametros sin valor default")
def calc(x,y):
    print (x+y)

calc(1,2)

print("con parametros sin valor default")
def calc (a, b=0):
    print (a+b)

calc(2)
calc(2,1)

print("con cantidad de parametros variables")
#*args positional arguments

def router_info(*args):
    print (args)

router_info("netconf","yang")

#*kwargs positional arguments
def router_info(**kwargs):
    print(kwargs)

router_info(name ="N9k1", version ="9.3(5)", HW ="C9396FX-2")

print ("\n")
#*args and *kwargsarg
print ("*args and **kwargs")
def router_info(*args, **kwargs):
    print (args)
    print(kwargs)

router_info('Netconf','SNMP', version="9.3(5", HW="C9336FX-2")
