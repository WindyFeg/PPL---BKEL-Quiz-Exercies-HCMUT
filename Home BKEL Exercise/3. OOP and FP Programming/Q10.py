# Use recursive approach to write a function lstSquare(n:Int) that returns a list of the squares of the numbers from 1 to n?

def lstSquare(n):
    res = []
    if n == 0:
        return []
    else:
        res.append(n*n)
    return lstSquare(n-1) + res

def lstSquare(n):
    return [x*x for x in range(1,n+1)]

def lstSquare(n):
    return map(
        lambda x: x*x,
        range(1,n+1)
        )