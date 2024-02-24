# Let lst be a list of a list of element, 
# use high-order function approach to write function flatten(lst) that returns the list of all elements


from functools import reduce
def flatten(lst):
    return reduce(lambda x, y: x + y, lst, [])

def flatten(lst):
    return [item for sublst in lst for item in sublst]

def flatten(lst):
    res = []
    for item in lst:
        if isinstance(item, list):
            res.extend(flatten(item))
        else:
            res.append(item)
    return res