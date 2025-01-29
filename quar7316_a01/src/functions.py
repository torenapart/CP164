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

# Constants


def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    temp = []

    for value in values:
        if value not in temp:
            temp.append(value)

    values.clear()
    values.append(temp)

    return


def list_subtraction(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtraction(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    count = 0
    while count < len(minuend):
        if minuend[count] in subtrahend:
            minuend.pop(count)
        else:
            count += 1

    return


def dsmvwl(string):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvwl(string)
    -------------------------------------------------------
    Parameters:
       string - a string (str)
    Returns:
       out - string with the vowels removed (str)
    -------------------------------------------------------
    """
    v1 = "a"
    v2 = "e"
    v3 = "i"
    v4 = "o"
    v5 = "u"
    out = ""

    for char in string:
        if char.lower() not in [v1, v2, v3, v4, v5]:
            out += char

    return out


def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged:
    Do not strip() the lines.
    Use: upp, low, dig, whi, rem = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        upp - the number of uppercase letters in the file (int)
        low - the number of lowercase letters in the file (int)
        dig - the number of digits in the file (int)
        whi - the number of whitespace characters in the file (int)
        rem - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    upp = 0
    low = 0
    dig = 0
    whi = 0
    rem = 0
    line = fv.readline()
    for char in line:
        upper = char.isupper()
        lower = char.islower()
        digit = char.isdigit()
        space = char.isspace()
        if upper == True:
            upp += 1
        elif lower == True:
            low += 1
        elif digit == True:
            dig += 1
        elif space == True:
            whi += 1
        else:
            rem += 1
    return upp, low, dig, whi, rem


def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    leap_year = False
    remfour = year % 4
    remhundred = year % 100
    remfourhundred = year % 400
    if remfour == 0 and remhundred != 0 or remfourhundred == 0:
        leap_year = True
    return leap_year


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    tester = name[0]
    valid = False
    letter = name.isalpha()
    undy = "_"
    if tester == undy and letter == True:
        valid = True

    return valid


def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    a must be unchanged.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a list (int)
    -------------------------------------------------------
    """
    md = abs(a[1] - a[0])
    for i in range(1, len(a) - 1):
        diff = abs(a[i + 1] - a[i])
        if diff > md:
            md = diff

    return md


def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a. You may assume there is at
    least one value in a.
    a must be unchanged.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    small = large = a[0][0]
    total = 0
    count = 0

    for row in a:
        for j in row:
            small = min(small, j)
            large = max(large, j)
            total += j
            count += 1

    average = total / count
    return small, large, total, average


def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    c = []
    rows = len(a)
    cols = len(a[0])

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        c.append(row)

    return c
