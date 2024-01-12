
#? Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# input : 13,2,4,5
# Expected: ['13', '2', '4', '5']
# ('13', '2', '4', '5')
num = input () 
print (num.split(","))
print(tuple(num.split(",")))