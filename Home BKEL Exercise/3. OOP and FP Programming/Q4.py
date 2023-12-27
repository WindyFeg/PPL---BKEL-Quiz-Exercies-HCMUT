def compose(*funcs):
    if len(funcs) < 2:
        print("compose() missing 1 required positional argument")
    def inner(x):
        res = x
        for f in reversed(funcs):
            res = f(res)
        return res
    return inner
