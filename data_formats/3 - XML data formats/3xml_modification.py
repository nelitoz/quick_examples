#!/usr/bin/env python

# Modules
import xml.etree.ElementTree as ET
# Variables

site_data = {
    "3": {
        "provider_side":{
            "router": "r5",
            "port": "g0/2",
            "ipv4": "1.1.1.1/30",
            "ipv6": "fe80::1/64"
             },
        "customer_side": {
            "router": "r6",
            "port": "g0/2",
            "ipv4": "1.1.1.2/30",
            "ipv6": "fe80::2/64"
             }
        }
    }

# .Element ==> crea el elemento root del XML
# .SubElement ==> agrega un elemento hijo al elemento padre
# .get ==> modifica el atributo de un elemento
# .append ==> agrega un sub-elemento al final del documento XML

# Body
for l1k,l1v in site_data.items():
    # Creo el elemento padre site con un ID = 3
    XML_element_L1 = ET.Element("site")
    XML_element_L1.set("id",l1k)

    for l2k, l2v in l1v.items():
        XML_element_L2 = ET.SubElement(XML_element_L1, l2k)

        for l3k, l3v in l2v.items():
            XML_element_L3 = ET.SubElement(XML_element_L2, l3k)
            XML_element_L3.text = l3v

# ET.dump(XML_element_L1)
# adding XML_ELEMENT_L1 to the XML file

tree = ET.parse("3input.xml")
root = tree.getroot()

root.find(".//sites").append(XML_element_L1)
tree.write("3output.xml")
