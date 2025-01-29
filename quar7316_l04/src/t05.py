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
target = []
lst = List()
count = 10
while count < 51:
    lst.append(count)
    count += 10

frst = lst[2]
print(f"Current first value is: {frst}")
print(f"Set first value to: 5")
lst[2] = 5
list_to_array(lst, target)
print(target)
