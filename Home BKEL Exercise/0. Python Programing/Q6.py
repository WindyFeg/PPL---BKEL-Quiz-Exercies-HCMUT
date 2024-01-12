
#? Write a Python function sum_of_cubeNo that takes a positive integer n and returns the sum of the cube of all the positive integers smaller than n.

# print(sum_of_cube(8))

def sum_of_cube(n):
    return sum([i ** 3 for i in range(1,n)])
