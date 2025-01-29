"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
# Imports
from List_linked import List

words = List()
words.append("mathematics")
words.append("creation")
words.append("makeshift")
words.append("manifestation")
first = words.peek()
print(f"Peek: {first}")
removed = words.remove("creation")
print(f"Removed item: {removed}")
