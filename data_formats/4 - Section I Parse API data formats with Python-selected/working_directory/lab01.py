# Import modules
import sys
from helper import *

import xml.etree.ElementTree as ET
import yaml
import json
import xml.dom.minidom as MD

# Main function
if __name__ == "__main__":
    #########################################
    #              Procedure 1              #
    #########################################
    print ("DEVNET")


    #########################################
    #              Procedure 2              #
    #########################################
    print('##################')
    print('###### YAML ######')
    print('##################')

    # Open the user.yaml file as read only
    with open("user.yaml","r") as fhand:
        # Load the stream using safe_load
        yaml_data = yaml.safe_load(fhand)

    # Print the object type
    print("Type of user_yaml variable:",type(yaml_data))

    print('----------------------')

    # Iterate over the keys of the user_yaml and print them
    print('Keys in user_yaml:')
    for k in yaml_data:
        print (k)

    print('----------------------')

    # Create a new instance of class User
    user1 = User()

    # Assign values from the user_yaml to the object user
    user1.id = yaml_data['id']
    user1.first_name = yaml_data['first_name']
    user1.last_name = yaml_data['last_name']
    user1.birth_date = yaml_data['birth_date']
    user1.address = yaml_data['address']
    user1.score = yaml_data['score']



    # Print the user object
    print('User object:')
    print (user1)


    #########################################
    #              Procedure 3              #
    #########################################
    print('##################')
    print('###### JSON ######')
    print('##################')

    # Create JSON structure from the user object

    json_data = json.dumps(user1, default=serializeUser)
    
    # Print the created JSON structure
    print('Print user_json:')
    print (json_data)

    print('----------------------')

    # Create JSON structure with indents and sorted keys
    print('JSON with indents and sorted keys')
    json_data = json.dumps(user1, default=serializeUser, indent=4)
    print (json_data)


    #########################################
    #              Procedure 4              #
    #########################################
    print('######################')
    print('# XML - Element Tree #')
    print('######################')

    # Parse the user.xml file
    mytree = ET.parse("user.xml")        
    # Get the root element
    myroot = mytree.getroot()

    # Print the tags
    print('Tags in the XML:')
    for element in myroot:
        print (element.tag)

    print('----------------------')

    # Print the value of id tag
    print('id tag value:')
    print (myroot.find("id").text)

    print('----------------------')

    # Find all elements with the tag address in root
    addresses = myroot.findall("address")

    # Print the adresses in the xml
    print('Addresses:')
    for address in addresses:
        for a in address:
            print (f"{a.tag}:{a.text}")
        print ("\n")

    print('----------------------')
    
    # Print the elements in root with their tags and values
    print('Print the structure')
    for k in myroot.iter():
        print (f"{k.tag}:{k.text}")

    # Parsing XML files with MiniDOM 
    print('######################')
    print('### XML - MiniDOM ####')
    print('######################')

    # Parse the user.xml file
    dom = MD.parse("user.xml")


    # Print the tags
    for node in dom.childNodes:
        printTags(node.childNodes)

    print('----------------------')

    # Accessing element value
    print('Accessing element value')
    idElements = dom.getElementsByTagName('id')
    print (idElements)
    elementId = idElements.item(0)
    print (elementId.childNodes)

    idValue = elementId.firstChild.data
    print(idValue)

    print('----------------------')
    

    # Print elements from the DOM with tag name 'address'
    print('Addresses:')
    for node in dom.getElementsByTagName('address'):
        printNodes(node.childNodes)

    print('----------------------')

    # Print the entire structure with printNodes
    print('The structure:')
    for node in dom.childNodes:
        printNodes(node.childNodes)


    #########################################
    #              Procedure 5              #
    #########################################
    print('######################')
    print('#   Use Namespaces   #')
    print('######################')

# Parse the user.xml file
    itemTree = ET.parse('item.xml')

    # Get the root element
    root = itemTree.getroot()

    # Define namespaces 
    namespaces = {'a':'https://www.example.com/network', 'b':'https://www.example.com/furniture'}

    # Set table as the root element 
    elementsInNSa = root.findall('a:table', namespaces)
    elementsInNSb = root.findall('b:table', namespaces)

    # Elements in NS a
    print('Elements in NS a:')   
    for e in elementsInNSa:
        for i in e.iter():
            print (f"{i.tag}:{i.text}")

    print('----------------------')

    # Elements in NS b
    print('Elements in NS b:')
    for i in list(elementsInNSb[0]):
        print (i.tag + ":" + i.text)

