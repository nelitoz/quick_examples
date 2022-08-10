import os
from netmiko import ConnectHandler
from claro_devices import *

def precheck_ortezal1():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "ortezal1-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    net_connect = ConnectHandler(**cisco_ortezal1)
    
    with open("pre-checks_ortezal1.txt") as fhand:
        cisco_ortezal1_show_commands = fhand.readlines()
    
    with open(output_file, "w+") as fhand:        
        for line in cisco_ortezal1_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)
    net_connect.disconnect()


def precheck_ortezal2():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "ortezal2-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    net_connect = ConnectHandler(**cisco_ortezal2)
    
    with open("pre-checks_ortezal2.txt") as fhand:
        cisco_ortezal2_show_commands = fhand.readlines()
    
    with open(output_file, "w+") as fhand:        
        for line in cisco_ortezal2_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)
    net_connect.disconnect()
    
def precheck_agg1():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "agg1-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    net_connect = ConnectHandler(**cisco_AGG1)
    
    with open("pre-checks_agg1.txt") as fhand:
        cisco_AGG1_show_commands = fhand.readlines()
    
    with open(output_file, "w+") as fhand:        
        for line in cisco_AGG1_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)
    net_connect.disconnect()
    

def precheck_agg2():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "agg2-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    net_connect = ConnectHandler(**cisco_AGG2)
    
    with open("pre-checks_agg2.txt") as fhand:
        cisco_AGG2_show_commands = fhand.readlines()

    with open(output_file, "w+") as fhand:        
        for line in cisco_AGG2_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)
    net_connect.disconnect()
    
def precheck_aggr1():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "aggr1-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    net_connect = ConnectHandler(**cisco_AGGR1)
    
    with open("pre-checks_aggr1.txt") as fhand:
        cisco_AGGR1_show_commands = fhand.readlines()

    with open(output_file, "w+") as fhand:        
        for line in cisco_AGGR1_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)
            
    net_connect.disconnect()

def precheck_aggr2():
    save_path = "/Users/dacasti2/claro_MW2_prechecks"
    save_file = "aggr2-prechecks.txt"
    output_file = os.path.join(save_path, save_file)
    
    net_connect = ConnectHandler(**cisco_AGGR2)
    with open("pre-checks_aggr2.txt") as fhand:
        cisco_AGGR2_show_commands = fhand.readlines()

    with open(output_file, "w+") as fhand:
        for line in cisco_AGGR2_show_commands:
            print(line)
            output = net_connect.send_command(line)
            print(output)
            fhand.write(line)            
            fhand.write(output)

    net_connect.disconnect()
    
precheck_ortezal1()
precheck_ortezal2()
precheck_agg1()
precheck_agg2()
precheck_aggr1()
precheck_aggr2()