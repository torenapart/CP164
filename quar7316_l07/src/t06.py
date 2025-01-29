"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-03-02"
-------------------------------------------------------
"""
# Imports
from List_linked import List
oglist = List()
for value in range(1, 6):  # This will create a list with values 1 to 5
    oglist.append(value)


print("List:")
current = oglist._front
while current is not None:
    print(current._value)
    current = current._next
print()

oglist.reverse_r()

print("Reversed:")
current = oglist._front
while current is not None:
    print(current._value)
    current = current._next
print()
