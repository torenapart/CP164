"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List


numbers = List()
numbers.append(4)
numbers.append(6)
numbers.append(8)
numbers.append(9)
b4, current, index = numbers._linear_search(6)
print(f"Before: {b4._value if b4 else None}")
print(f"Current: {current._value if current else None}")
print(f"Index: {index}")
