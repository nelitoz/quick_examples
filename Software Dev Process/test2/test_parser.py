import unittest
from parser import ConfigurationParser


class TestParse(unittest.TestCase):
    def test_parse_customer_name(self):
        cp = ConfigurationParser()
        expected_names = ["CUSTOMER_A", "CUSTOMER_B"]
        parsed_names = cp.parseCustomerNames()
        self.assertEqual(parsed_names, expected_names)
        self.assertEqual(list, type(parsed_names))

    def test_parse_customer_vlan(self):
        cp = ConfigurationParser()
        customer_name = "CUSTOMER_A"
        expected_vlan = ['100', '102']
        parsed_vlan = cp.parseCustomerVlan(customer_name)
        self.assertEqual(expected_vlan, parsed_vlan)

    def test_parse_customer_ip(self):
        cp = ConfigurationParser()
        vlan = "100"
        expected_ip = "10.10.100.1"
        parsed_ip = cp.parseCustomerIP(vlan)
        self.assertEqual(parsed_ip, expected_ip)


if __name__ == "__main__":
    unittest.main()
