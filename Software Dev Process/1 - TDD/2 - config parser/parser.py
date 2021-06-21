import re

class ConfigurationParser:
    """
    Class to parse router configuration
    """
    with open("config.txt", "r") as fhand:
        config = fhand.read()

    def parseCustomerNames(self):

        customers = re.findall(r"^ip vrf (.+?)\n", self.config, re.MULTILINE)
        return customers

    def parseCustomerVlan(self, customer):
        vlanPattern = (
                r"interface GigabitEthernet.+?\n  encapsulation "
                r"dot1Q ([0-9]+)\n  ip vrf forwarding {}".format(customer)
        )
        return re.findall(vlanPattern, self.config)

    def parseCustomerIP(self, vlan):
        ip_pattern = (r"GigabitEthernet.+?\.{} +(.*)\n".format(vlan))
        return re.findall(ip_pattern, self.config)[0]

    def parseCustomerData(self):
        diccionario = {}
        # customers is a list of VRFs
        customers = self.parseCustomerNames()
        for customer in customers:
            vlans = self.parseCustomerVlan(customer)
            for vlan in vlans:
                ip = self.parseCustomerIP(vlan)
                if customer in diccionario:
                    diccionario[customer].append({vlan, ip})
                else:
                    diccionario[customer] = [{vlan, ip}]
                #print (diccionario)
        return diccionario



"""
cp = ConfigurationParser()
print(cp.parseCustomerNames())
print(cp.parseCustomerVlan("CUSTOMER_A"))
print(cp.parseCustomerIP(100))
print(cp.parseCustomerIP(102))
"""
cp = ConfigurationParser()
print (cp.parseCustomerData())
