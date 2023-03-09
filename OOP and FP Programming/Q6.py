# List comprehension approach

def dist(lst, n):
    return [(x,n) for x in lst]

print(dist([1,2,3],4))