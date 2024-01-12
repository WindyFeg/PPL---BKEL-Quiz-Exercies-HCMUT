
#? Write a Python function check(lst,n) to test whether all numbers of the list lst is greater than the number n.
# print(check([21,12,5,8],3))

def check(lst,n):
    for i in lst:
        if i <= n:
            return False
    return True