from vlantools import *

with open("dev1_po1_vlans.txt") as fhand:
    agg1_service_vlans =fhand.read()
    
with open("dev2_po1_vlans.txt") as fhand:
    agg2_service_vlans = fhand.read()
    
    
agg1 = clean_trunk_vlan_config(agg1_service_vlans)
agg2 = clean_trunk_vlan_config(agg2_service_vlans)
agg1 = from_string_to_int(agg1)
agg2 = from_string_to_int(agg2)

get_differentials(agg1,agg2)
