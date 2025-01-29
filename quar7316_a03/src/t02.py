"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack

s1 = Stack()
s2 = Stack()
target_stack = Stack()
count = 1
count2 = 3
while count != 5:
    s1.push(count)
    count += 1

while count2 != 7:
    s2.push(count2)
    count2 += 1

target_stack.push(10)
target_stack.push(20)
target_stack.push(30)
target_stack.combine(s1, s2)
print(target_stack._values)
