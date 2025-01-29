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

from functions import is_palindrome_stack

palindrome = str(input("Input here: "))
output = is_palindrome_stack(palindrome)
print()
print(f"It is {output} that {palindrome} is a palindrome")
