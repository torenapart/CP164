"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

s = Stack()
s._values.extend([1, 2, 3])
print(f"Pre: {s._values}")
s.reverse()
print(f"After: {s._values}")
