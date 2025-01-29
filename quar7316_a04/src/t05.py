"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-04"
-------------------------------------------------------
"""
# Imports
from functions import pq_split_key
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
pq.insert(1)
pq.insert(2)
pq.insert(6)
pq.insert(8)
split = 3

higher, lower = pq_split_key(pq, split)

print("Target 1 Queue:")
for value in higher:
    print(value)
print()

print("Target 2 Queue:")
for value in lower:
    print(value)
print()
