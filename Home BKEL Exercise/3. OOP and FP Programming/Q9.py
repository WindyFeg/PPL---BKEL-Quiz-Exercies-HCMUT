# Let lst be a list of integer and n be an integer, use high-order function approach to write function lessThan(lst,n) that returns the list of all numbers in lst less than n.

from functools import reduce

def lessThan(lst, n):
    def concat(pre, cur):
        if cur < n:
            return pre + [cur]
        else:
            return pre

    return reduce(concat, lst, [])


from functools import reduce

def lessThan(lst, n):
    res = []
    if len(lst) == 0:
        return []
    
    if lst[0] < n:
        res.append(lst[0])
    return res + lessThan(lst[1:], n)