"""Collection of some useful functions"""
from functools import reduce

def collapse(data):
    """Given a list, returns the items of that list concatenated together"""

    return reduce(lambda x, y: x + y, data)

def slice(string, n):
    """Splits the string into some pieces of all size n00"""

    temp = []
    i = n
    while i <= len(string):
        temp.append(string[(i-n):i])
        i += n

    try:
        if string[(i-n)] != "":
            temp.append(string[(i-n):])
    except IndexError:
        pass

    return temp
