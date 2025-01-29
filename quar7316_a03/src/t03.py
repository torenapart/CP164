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
from functions import stack_reverse
from Stack_array import Stack

s = Stack()
s.push(1)
s.push(3)
s.push(5)
print(f"Pre: {s._values}")
stack_reverse(s)
print(f"After: ")
while not s.is_empty():
    print(s.pop())
