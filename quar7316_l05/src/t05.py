"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-10"
-------------------------------------------------------
"""
# Imports
from functions import is_palindrome
# Constants

worrr = "racecar"
output = is_palindrome(worrr)
if output:
    print(f"The word '{worrr}', IS a palindroome")
else:
    print(f"The word '{worrr}' is NOT a palindrome")
