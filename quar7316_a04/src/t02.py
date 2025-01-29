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
from Queue_circular import Queue

queue1 = Queue()
queue2 = Queue()
source = [1, 2, 3, 4, 5]
for v in source:
    queue1.insert(v)
    queue2.insert(v)

if queue1.__eq__(queue2):
    print("they are equal.")
else:
    print("they are not equal.")
