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

lisd = List()
lisd.append("eternal")
lisd.append("barracuda")
lisd.append("thyme")
lisd.append("china")

searchee = lisd.find("thyme")
print(f"Found word: {searchee}")

index = lisd.index("barracuda")
print(f"'barracuda' index: {index}")

contains = "eternal" in lisd
if contains:
    print(f"'eternal' IS in the list")
else:
    print(f"'eternal' is NOT in the list")
