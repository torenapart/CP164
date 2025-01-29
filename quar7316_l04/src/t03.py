"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import list_to_array

lst = List()
target = []
count = 10
while count < 51:
    lst.append(count)
    count += 10
list_to_array(lst, target)
print(f"lst after appending numbers: {target}")
lst.insert(1, 60)
list_to_array(lst, target)
print(f"lst after inserting 60: {target}")
preremoved = 20
removed = lst.remove(20)
list_to_array(lst, target)
print(f"lst after removing {preremoved}: {target}")
