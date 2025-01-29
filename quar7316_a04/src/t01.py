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

queue = Queue()

for i in range(5):
    queue.insert(i)
    print(f"Inserted {i} into the queue.")


frst = queue.peek()
print(f"first: {frst}")

remove = queue.remove()
print(f"removed: {remove}")

print(f"The queue is {len(queue)} values long")
