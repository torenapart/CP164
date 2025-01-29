"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-27"
-------------------------------------------------------
"""
# Imports
from functions import stack_combine
from utilities import array_to_stack
from utilities import stack_to_array
from Stack_array import Stack
# Constants
target = []
source1 = Stack()
source2 = Stack()
list1 = [5, 8, 12, 8]
array_to_stack(source1, list1)
list2 = [3, 6, 1, 7, 9, 14]
array_to_stack(source2, list2)
outputstack = stack_combine(source1, source2)
stack_to_array(outputstack, target)
print(target)
