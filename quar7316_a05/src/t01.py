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
from Food import Food
from Food_utilities import read_food
from List_array import List
from copy import deepcopy

fh = open("foods.txt", "r", encoding="utf-8")
foods = read_food(fh)
food_list = List()
for food in foods:
    food_list.append(food)

# getitem
if len(food_list) > 0:
    print("Get item:", food_list[0])

# clean
food_list.clean()
print("cleaned:", [str(food) for food in food_list])

# combine
list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[1])
food_list.combine(list1, list2)
print("combine:", [str(food) for food in food_list])

# intersection
list1 = deepcopy(food_list)
list2 = deepcopy(food_list)
list1.intersection(list1, list2)
print("intersection:", [str(food) for food in food_list])

# prepend
food_list.prepend(Food("Spankopita", 0, True, 100))
print("prepend:", [str(food) for food in food_list])

# remove_front
if not food_list.is_empty():
    food_list.remove_front()
print("remove front:", [str(food) for food in food_list])

# remove_many
if len(food_list) > 0:
    food_list.remove_many(food_list[0])
print("remove many:", [str(food) for food in food_list])

# split
if len(food_list) > 0:
    list1, list2 = food_list.split()
    print("List 1 split:", [str(food) for food in list1])
    print("List 2 split:", [str(food) for food in list2])

# split_alt
if len(food_list) > 0:
    list1, list2 = food_list.split_alt()
    print("List 1 split:", [str(food) for food in list1])
    print("List 2 split:", [str(food) for food in list2])

# union
list1 = List()
list2 = List()
list1.append(foods[0])
list2.append(foods[1])
food_list.union(list1, list2)
print("union:", [str(food) for food in food_list])

# eq
list1 = List()
list1.append(foods[0])
list2 = List()
list2.append(foods[0])
print("Equal:", list1 == list2)

# iter
for food in food_list:
    print(food)
