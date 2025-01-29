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
from Queue_array import Queue
from utilities import queue_to_array
queue = Queue()
list = [1, 2, 3, 4, 5, 6]
target = []
queue.insert(list)
print(queue)
queue_to_array(queue, target)
print(target)
