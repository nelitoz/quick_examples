import xmltodict

with open("1user.xml", "r") as fhand:
    xml_example = fhand.read()
    xml_data = xmltodict.parse(xml_example)

for role in xml_data['root']['user']['roles']:
    print (role)

xml_data['root']['user']['location']['state']= 'QR'

print(xml_data)
with open ('1user.xml','w') as fhand:
    fhand.write(xmltodict.unparse(xml_data, pretty=True) )


