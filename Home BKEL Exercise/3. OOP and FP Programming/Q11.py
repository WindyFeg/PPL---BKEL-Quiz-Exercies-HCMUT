# Scala has function compose to compose two functions but Python does not have this function. Write function compose that can takes at least two functions  as its parameters and returns the composition of these parameter functions. For example compose(f,g,h)(x) is defined as f(g(h(x))).

def compose(f, g, *functions):
    def composed(x):
        res = x
        for function in reversed(functions):
            res = function(res)
        return f(g(res))
    return composed
