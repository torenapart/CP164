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

lst = List()
count = 10
while count < 51:
    lst.append(count)
    count += 10
looking = 20
index = lst.index(looking)
print(f"the index of the found number 20 is in: {index}")
found = lst.find(40)
print(f"the value 40 was found in: {found}")
count = lst.count(10)
print(f"count: {count}")
maxim = lst.max()
print(f"The maximum value in the list is: {maxim}")
minim = lst.min()
print(f"The minimum value in the list is: {minim}")
