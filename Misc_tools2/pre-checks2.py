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
		fcommand = "show run int "+command
		output = command + net_connect.send_command(fcommand, delay_factor=4)

		dev1 = clean_trunk_vlan_config(output)
		dev1 = from_string_to_int(dev1)
		get_differentials(dev1, command)

	net_connect.disconnect()


def prechecks(device):
	hostname = get_command(device, "show hostname").split(".")[0].strip()
	print(hostname)
	with open("pos.txt", 'r') as fhand:
		pos = fhand.readlines()
		get_commands(device,pos)


for device in devices:
	prechecks(device)