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
from functions import recurse
import random

# Constants
x = random.randint(1, 5)

y = random.randint(1, 5)
print(f"x: {x}, y: {y}")
output = recurse(x, y)
print(f"After the recurse function this is the output: {output}")
