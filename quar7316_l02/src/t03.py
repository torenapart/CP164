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
from utilities import stack_to_array, Stack
# Constants


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
target = []
stack_to_array(stack, target)
print(target)
