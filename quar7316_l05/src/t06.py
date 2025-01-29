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
from functions import bag_to_set
# Constants


bag = [8, 9, 0, 0, 6, 3, 6, 3, 0, 4, 1]

output = bag_to_set(bag)

print(f"Old bag: {bag}, New bag with one of each: {output} ")
