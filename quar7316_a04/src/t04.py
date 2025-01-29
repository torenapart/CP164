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
from Queue_array import Queue

source_queue = Queue()

for i in range(10):
    source_queue.insert(i)

target1, target2 = source_queue.split_alt()


print("Target 1 Queue:")
for value in target1:
    print(value)
print()

print("Target 2 Queue:")
for value in target2:
    print(value)
print()
