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
words.append("carp")
words.append("come")
words.append("venus")

onedex = words[1]
print(f"word @ index 1: {onedex}")

words[1] = "planetary"
print(f"New word @ index 1: {words[1]}")
