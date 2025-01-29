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
from Food_utilities import read_food
# Constants
preoutput = str(input("Input a line of  food data here: "))
output = read_food(preoutput)
print()
print(output)
