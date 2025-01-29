"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-21"
-------------------------------------------------------
"""
# Imports
from Food_utiliites import food_search
from Food_utilities import read_food
# Constants
list = ["BBQ Pork|1|False|920", "Orange Chicken|1|False|800", "Vegetables with Cashew Nuts|1|True|143",
        "Lemon Chicken|1|False|226", "Beef with Green Pepper|1|False|251"]
obj = read_food(list)
origin = 7
max_cals = 500
is_veg = False

result = food_search(list, origin, max_cals, is_veg)
print(result)
