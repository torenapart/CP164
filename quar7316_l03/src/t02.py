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
from utilities import array_to_queue
queue = Queue()
source = [1, 2, 3, 45, 5, 6]
array_to_queue(queue, source)
peek = queue.peek()
target = queue.remove()

print(f"Removed {target}, Peek value {peek}")
