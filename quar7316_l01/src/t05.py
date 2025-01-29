"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-12"
-------------------------------------------------------
"""
# Imports
from Food_utilities import read_foods
# Constants
fv = open("foods.txt", "r")
output = read_foods(fv)
fv.close()

for out in output:
    print()
    print(out)
