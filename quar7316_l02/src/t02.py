"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
# Imports
from utilities import array_to_stack, Stack
# Constants
s = Stack()
i = 0
source = []
number = int(input("Number of values to append: "))
while i < number:
    val = int(input("Input a value: "))
    if val != "":
        num = int(val)
        source.append(num)
        i += 1

array_to_stack(s, source)
