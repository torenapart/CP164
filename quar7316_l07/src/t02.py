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

values = [1, 2, 3, 4, 5]
list1 = List()
list2 = List()
for v in values:
    list1.append(v)
    list2.append(v)

identical = list1.is_identical_r(list2)
print(f"It is {identical} that the lists are identical.")
