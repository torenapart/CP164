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

list1 = List()
list2 = List()


for value in [1, 3, 5, 7]:
    list1.append(value)
for value in [2, 4, 5, 6, 7]:
    list2.append(value)

union_list = List()

union_list.union_r(list1, list2)

print("Union:")
current = union_list._front
while current is not None:
    print(current._value)
    current = current._next
print()
