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
from functions import queue_split_alt

source = Queue()
temp = Queue()

for i in range(10):
    source.insert(i)
    temp.insert(i)

target1, target2 = queue_split_alt(source)
print("target1 contains:")
while not target1.is_empty():
    print(target1.remove(), end=' ')
print("target2 contains:")
while not target2.is_empty():
    print(target2.remove(), end=' ')
