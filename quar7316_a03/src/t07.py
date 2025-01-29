"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
# Imports

from functions import stack_maze

maze = {
    'Start': ['A'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': [],
    'E': ['F', 'X'],
    'F': ['G'],
    'G': ['C']
}
print(maze)
print(stack_maze(maze))
