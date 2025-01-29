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
from functions import file_analyze
# Constants
fv = open("foods.txt", "r")
upp, low, dig, whi, rem = file_analyze(fv)
fv.close()

print(f"""Uppercase: {upp} Lower: {low}, Digits: {
      dig}, Spaces{whi}, Remaining letters: {rem}""")
