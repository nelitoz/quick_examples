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
        vlanid = re.search(vlanPattern, self.config)
        return  int(vlanid.group(1))

# cp = ConfigurationParser()
# print(cp.parseCustomerVlan("CUSTOMER_A"))
