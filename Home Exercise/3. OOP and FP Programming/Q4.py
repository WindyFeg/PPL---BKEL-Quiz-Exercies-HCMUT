
def increase(x):
    return x + 1

def square(x):
    return x * x

def compose(*funcs):
    if len(funcs) >2:
        print("compose() missing 1 required positional argument")
    else:
        def fun(x):
            res = x
            for f in reversed(funcs):
                res = f(res)
            return res
        return fun;

f = compose(increase,square)
print(f(3)) #increase(square(3)) = 10

