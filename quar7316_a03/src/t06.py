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
from functions import postfix

expression = input("Input your expression here:")
print()
output = postfix(expression)
print(f"{output}")
