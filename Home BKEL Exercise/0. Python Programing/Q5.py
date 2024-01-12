
# ?Write a Python function product(lst) to return the product of the list lst of integers 

def product(lst):
    res = 1
    for i in lst:
        res *= i
    return res