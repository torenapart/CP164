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
from Priority_Queue_array import Priority_Queue

pq = Priority_Queue()
source = [2, 4, 18, 6, 2]
for value in source:
    pq.insert(value)
key = 15

higher, lower = pq.split_key(key)

print("PQ with values higher than key:")
for value in higher:
    print(value)
print()

print("PQ with values lower or equal to key:")
for value in lower:
    print(value)
print()
