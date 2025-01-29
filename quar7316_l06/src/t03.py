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
numbers.append(1)
numbers.append(4)
numbers.append(7)
numbers.append(4)
numbers.append(890)
value = 4
count = numbers.count(value)
print(f"{value} appears {count} in the list")

maxim = numbers.max()
print(f"The biggest value in 'numbers': {maxim}")

minim = numbers.min()
print(f"The smallest value in 'numbers': {minim}")
