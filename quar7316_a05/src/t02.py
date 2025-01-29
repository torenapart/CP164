"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-02-11"
-------------------------------------------------------
"""
# Imports
from Sorted_List_array import Sorted_List
from Food_utilities import read_food
from copy import deepcopy
from Food import Food

fh = open("foods.txt", "r", encoding="utf-8")
foods = read_food(fh)
food_list = Sorted_List()
for food in foods:
    food_list.insert(food)

# getitem
if len(food_list) > 0:
    print("Get item:", food_list[0])

# clean
food_list.clean()
print("cleaned:", [str(food) for food in food_list])

# combine
list1 = Sorted_List()
list1.insert(foods[0])
list2 = Sorted_List()
list2.insert(foods[1])
food_list.combine(list1, list2)
print("combined:", [str(food) for food in food_list])

# intersection
list1 = deepcopy(food_list)
list2 = deepcopy(food_list)
list1.intersection(list1, list2)
print("intersected:", [str(food) for food in food_list])

# remove front
if not food_list.is_empty():
    food_list.remove_front()
print("removeed front", [str(food) for food in food_list])

# remove many
if len(food_list) > 0:
    food_list.remove_many(food_list[0])
print("removed many:", [str(food) for food in food_list])

# split
if len(food_list) > 0:
    list1, list2 = food_list.split()
    print("List 1 split:", [str(food) for food in list1])
    print("List 2  split:", [str(food) for food in list2])

# split alt
if len(food_list) > 0:
    list1, list2 = food_list.split_alt()
    print("List 1 split_alt:", [str(food) for food in list1])
    print("List 2  split_alt:", [str(food) for food in list2])

# union
list1 = Sorted_List()
list2 = Sorted_List()
list1.insert(foods[0])
list2.insert(foods[1])
food_list.union(list1, list2)
print("List union:", [str(food) for food in food_list])

# eq
list1 = Sorted_List()
list1.insert(foods[0])
list2 = Sorted_List()
list2.insert(foods[0])
print("List1 List2:", list1 == list2)

# iter
for food in food_list:
    print(food)
