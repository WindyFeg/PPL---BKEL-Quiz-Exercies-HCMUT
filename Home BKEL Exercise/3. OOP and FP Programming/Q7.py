# Use recursive approach to write a function lstSquare(n:Int) that returns a list of the squares of the numbers from 1 to n?

# test: lstSquare(3)
# result: [1,4,9]

def lstSquare(n):
    if n == 1:
        return [1]
    else:
        return lstSquare(n-1) + [n*n]
    
print(lstSquare(3))