"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-03"
-------------------------------------------------------
"""
# Imports
from List_array import List
from utilities import list_to_array
from utilities import array_to_list
# Constants

lst = List()
target = []
source = [10, 20, 30, 40, 50]
array_to_list(lst, source)

list_to_array(lst, target)
print(target)
