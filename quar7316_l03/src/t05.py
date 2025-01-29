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
from Priority_Queue_array import Priority_Queue
from utilities import pq_to_array
# Constants

pq = Priority_Queue()
list = [1, 2, 3, 44, 5, 6]
pq.insert(list)
print(pq)
output = pq.remove()
print(output)
