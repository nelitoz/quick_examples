from netmiko import ConnectHandler
from claro_devices import *
from vlantools import *


def get_command(device, command):
	net_connect = ConnectHandler(**device)
	output = ''
	output += net_connect.send_command(command, delay_factor=4)
	return output
	net_connect.disconnect()


def get_commands(device, command_list):
	net_connect = ConnectHandler(**device)
	for command in command_list:
		# print (command)
		fcommand = f"show interface status down |egrep -i command$"
		output = command + net_connect.send_command(fcommand, delay_factor=4)
		print (output)

	net_connect.disconnect()

def prechecks(device):
	hostname = get_command(device, "show hostname").split(".")[0].strip()
	print(hostname)
	with open("ints.txt", "r") as fhand:
		ints = fhand.readlines()
		get_commands(device, ints)

for device in devices:
	prechecks(device)

