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
from Food_utilities import get_vegetarian, read_foods
# Constants

fv = open("foods.txt", "r")
foods = read_foods(fv)
output = get_vegetarian(foods)

for out in output:
    print()
    print(output)

fv.close()
