#!/usr/bin/env python

# Modules
import xml.etree.ElementTree as ET

# Body
tree = ET.parse("3output.xml")
root = tree.getroot()

print(f"Building Catalogs for {root.tag}")

sites_xpath = ".//sites/"

# .findall ==> retorna una lista de sub-elementos con base en un xpath
# .get ==> retorna el valor del atributo consultado.
# .tag ==> retorna el tag del elemento que consulta
# .find ==> retorna el primer objeto elemento que encuentra con base al xpath proporcionado
# .text ==> retorna el valor del elemento
for site in root.findall(sites_xpath):
    site_id = site.get("id")
    print("\n")
    print(f"{site.tag} {site_id}")
    provider_router = site.find("./provider_side/router").text
    provider_port = site.find("./provider_side/port").text
    consumer_router = site.find("./customer_side/router").text
    consumer_port = site.find("./customer_side/port").text

    print(f"{provider_router} {provider_port} <==>{consumer_port} {consumer_router}")

