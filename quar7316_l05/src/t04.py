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
from functions import to_power
# Constants
base = 12
power = 3

output = to_power(base, power)
if power == 2:
    print(f"{base} squared is: {output}")
elif power == 3:
    print(f"{base} cubed is: {output}")
else:
    print(f"{base} to the power of {power} is: {output}")
