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

name = List()
name.append("Marcus")
name.prepend("Requis")
name.insert(1, "Monkey D. Luffy")
for v in name:
    print(v)
