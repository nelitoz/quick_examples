import re

def clean_trunk_vlan_config(allowed_vlans):
    # This function will take commands directly from int po sh running
    # <== switchport trunk allowed vlan 2,5,9,79,92-93,100,119,146,201,242
    # <== switchport trunk allowed vlan add 250,273,302,315,395,400,420-421
    # and will return a list of string vlans
    # ==> ['2', '5', '9', '79', '92-93', '100', '119', '146', '201', '242', ' 250', '273', '302', '315', '395', '400', '420-421'
    allowed_vlans = allowed_vlans.strip()
    vlans = str(re.findall("switchport trunk allowed .* (\d.*)",allowed_vlans, re.M))
    string_vlan_list = re.sub("[\[\]']","",vlans)
    string_vlan_list = string_vlan_list.split(",")
    return string_vlan_list

def unrange(r):
    # This function expects a vlan range string
    # and returns a list of unraged vlans
    number = r.split("-")
    return(list(range(int(number[0]),int(number[1])+1)))

def from_string_to_int(string_vlan_list):
    # This function expect a LIST of STRINGS with single and vlan ranges
    # <== ['1-3', '5', '9-10',] list of strings
    # and will return a list of integer vlans without ranges
    # ==> [1, 2, 3, 5, 9, 10,] list of integers
    
    unrange_vlan_list=[]
    for vlan in string_vlan_list:
        if "-" in vlan:
            for i in unrange(vlan):
                unrange_vlan_list.append(i)
        else:
            unrange_vlan_list.append(int(vlan))
    return unrange_vlan_list


def get_missing_vlans_list(show_commands):
    # This function expects a list of vlans strings
    # and return a list of individual vlans missing

    list_vlans_string = clean_trunk_vlan_config(show_commands)
    list_vlans_int = from_string_to_int(list_vlans_string)
    return [x for x in range(list_vlans_int[0], list_vlans_int[-1] + 1) if x not in list_vlans_int]


def get_consecutive_integer_series(integer_list):
    # from https://stackoverflow.com/questions/2361945/detecting-consecutive-integers-in-a-list
    integer_list = sorted(integer_list)
    start_item = integer_list[0]
    end_item = integer_list[-1]

    a = set(integer_list)  # Set a
    b = range(start_item, end_item+1)

    # Pick items that are not in range.
    c = set(b) - a  # Set operation b-a

    li = []
    start = 0
    for i in sorted(c):
        end = b.index(i)  # Get end point of the list slicing
        li.append(b[start:end])  # Slice list using values
        start = end + 1  # Increment the start point for next slicing
    li.append(b[start:])  # Add the last series

    for sliced_list in li:
        if not sliced_list:
            # list is empty
            continue
        if len(sliced_list) == 1:
            # If only one item found in list
            yield str(sliced_list[0])
        else:
            yield "{0}-{1}".format(sliced_list[0], sliced_list[-1])


def get_differentials(set1,set2):
    set1 = set(set1)
    set2 = set(set2)
    #print(f"Diferencia Simetricas{sorted(set1.symmetric_difference(set2))}\n\n")

    print(f"dev1 tiene:{len(set1)} vlans")
    #print(f"Falta en dev1:{sorted(set2.difference(set1))}\n\n")

    print(f"dev2 tiene:{len(set2)} vlans")
    #print(f"Falta en dev2:{sorted(set1.difference(set2))}\n\n")

