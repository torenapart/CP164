"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Toren Quarshie
ID:      169067316
Email:   quar7316@mylaurier.ca
__updated__ = "2024-03-16"
-------------------------------------------------------
"""
# Imports

# Constants


def hash_table(slots, values):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    695    2 Lasagna, 7
    1355    4 Butter Chicken, 2
    Do not create an actual Hash_Set.
    Use: hash_table(slots, values)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hash     Slot Key")
    print("-------- ---- --------------------")
    for v in values:
        hashed = hash(v)
        slt = hashed % 7
        k = v.key()
        print("{:8}{:5} {}".format(hashed, slt, k))

    return
