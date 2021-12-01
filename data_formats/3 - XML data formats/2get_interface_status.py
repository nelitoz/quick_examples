import re
import xmltodict

def open_xml(file):
    with open(file,"r") as fhand:
        xml_example = fhand.read()
        xml_data = xmltodict.parse(xml_example)
    return xml_data

xml_data = open_xml("2dc2_int_down.xml")

#in case the Row interface is equal to a list, meaning there are more than 1 interface
if type(xml_data["nf:rpc-reply"]["nf:data"]["show"]["interface"]["status"]["up"]["__readonly__"]["TABLE_interface"]["ROW_interface"])==list:
    for i in xml_data["nf:rpc-reply"]["nf:data"]["show"]["interface"]["status"]["up"]["__readonly__"]["TABLE_interface"][
        "ROW_interface"]:
        if re.match(r"Ethernet", i["interface"]):
            if "name" in i:
                print (i["interface"]+","+ i["state"]+","+i["name"])
            else:
                print (i["interface"]+","+ i["state"]+","+"NONE")

#in case the Row interface is equal to dict, meaning there is just 1 interface
else:
    interface = xml_data["nf:rpc-reply"]["nf:data"]["show"]["interface"]["status"]["up"]["__readonly__"]["TABLE_interface"]["ROW_interface"]
    table_interface = xml_data["nf:rpc-reply"]["nf:data"]["show"]["interface"]["status"]["up"]["__readonly__"]["TABLE_interface"]
    if "Ethernet" in interface["interface"]:
        if "name" in interface["name"]:
            print (interface["interface"], interface["state"], interface["name"])
        else: 
            print (interface["interface"], interface["state"])
