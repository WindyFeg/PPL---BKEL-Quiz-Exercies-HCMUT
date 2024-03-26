# Let lst be a list of integer and n be any value, use high-order function approach to write function dist(lst,n) that returns the list of pairs of an element of lst and n.
# test:  dist([1,2,3],4)
# expected: [(1, 4),(2, 4),(3, 4)]


def dist(lst, n):
    return list(map(lambda x: (x,n), lst))

# print(dist([1,2,3],4))

def dist(lst, n):
    if len(lst) == 0: return []
    if len(lst) == 1:
        return [(lst[0], n)]
    return [(lst[0], n)] + dist(lst[1:], n)

def dist(lst,n):
    return [(x,n) for x in lst]
