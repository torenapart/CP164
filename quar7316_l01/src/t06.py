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
from Food_utilities import write_foods
# Constants
fv = open("new_foods.txt", "w+")
foods = []
newfoods = input("Input a food object here:")
while newfoods != "":
    foods.append(newfoods)
    newfoods = input("Input another food object here:")
write_foods(fv, foods)
fv.close()
