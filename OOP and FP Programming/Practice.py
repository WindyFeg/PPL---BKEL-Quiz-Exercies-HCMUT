# #  *Create Expression, Binary, Unary, Intlit and Floatlit

# class Exp:
#     def eval():
#         pass

# class Binary(Exp):
#     def __init__(self, operator, left, right):
#         self.operator = operator
#         self.left = left
#         self.right = right

#     def eval(self):
#         if(self.operator == '+'):
#             return self.left.eval() + self.right.eval()
#         elif(self.operator == '-'):
#             return self.left.eval() - self.right.eval()
#         elif(self.operator == '*'):
#             return self.left.eval() * self.right.eval()
#         elif(self.operator == '/'):
#             return self.left.eval() / self.right.eval()
#         else:
#             return self.left.eval()
        
# class Unary(Exp):
#     def __init__(self, operator, num):
#         self.num = num
#         self.operator = operator

#     def eval(self):
#         if(self.operator == '-'):
#             return - self.num.eval()
#         return + self.num.eval()

# class Intlit(Exp):
#     def __init__(self, num):
#         self.num = num

#     def eval(self):
#         return self.num
    

# class Floatlit(Exp):
#     def __init__(self, num):
#         self.num = num

#     def eval(self):
#         return self.num
    
# a = Intlit(3)
# print(a.eval())



# *QUESTION DIST
# ?dist([1,2,3],4) -> [(1,4),(2,5),(3,4)]

# list comprehension
# def dist_comprehension(lst, num):
#     return [(i,num) for i in lst]

# def dist_highOF(lst, num):
#     return list(map(
#         lambda x: (x,num),
#         lst
#     ))


# print(dist_highOF([1,2,3],4))

# *QUESTION 2
# ?LessThan([1,2,3,4,5], 3) -> [1,2]

# list comprehension
from functools import reduce


# def lessThan_listComprehension(lst, num):
#     return list(filter(
#         lambda x : x <num,
#         lst
#     ))

# def lessthan_highOF(lst, num):
#     return list(reduce(
#         lambda prev, curr: prev + [curr] if curr < num else prev,
#         lst,
#         []
#     ))

# print(lessthan_highOF([1,2,3,4,5], 3))

# *QUESTION 3
# ?Flatten([[1,2,3],[4,5,6]]) -> [1,2,3,4,5,6]

def flattern_recursive(lst):
    return lst[0] + flattern_recursive(lst[1:]) if len(lst) > 0 else []

print(flattern_recursive([[1,2,3],[4,5,6]]))


def flattern_listComprehension(lst):
    return [x for i in lst for x in i]

print(flattern_listComprehension([[1,2,3],[4,5,6]]))

def flattern_highOF(lst):
    return reduce(
        lambda prev, curr: prev + curr,
        lst,
        []
    )

print(flattern_highOF([[1,2,3],[4,5,6]]))