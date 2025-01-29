"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from Deque_linked import Deque

deque = Deque()
for value in [1, 2, 3, 4, 5]:
    deque.insert_rear(value)
for value in [0, -1, -2, -3, -4]:
    deque.insert_front(value)
print("Deque after inserting values at rear and front:", list(deque))
print()
front_value = deque.remove_front()
rear_value = deque.remove_rear()
print(f"Removed from front: {front_value}, Removed from rear: {rear_value}")
print()
print(f"Peek front: {deque.peek_front()}, Peek rear: {deque.peek_rear()}")
print()
print("Is the deque empty?", deque.is_empty())
print()
print("Length of the deque:", len(deque))
print()
deque2 = Deque()
for value in [-2, -1, 0, 1, 2, 3, 4]:
    deque2.insert_rear(value)
print("Are deques equal?", deque == deque2)
print()

print("Iterating through the deque:", list(deque))
