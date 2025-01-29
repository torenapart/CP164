"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-14"
-------------------------------------------------------
"""
# Imports
from functions import matrix_stats
# Constants


small, large, total, average = matrix_stats([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(f"Small: {small} Large: {large} Total: {total} Average: {average}")
