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


lst = List()
for i in range(1, 7):
    lst.append(i)
print("List:")
current = lst._front
while current is not None:
    print(current._value)
    current = current._next
print()
evlst, odlst = lst.split_alt_r()

print("Even:")
current = evlst._front
while current is not None:
    print(current._value)
    current = current._next
print()

print("Odd:")
current = odlst._front
while current is not None:
    print(current._value)
    current = current._next
print()
