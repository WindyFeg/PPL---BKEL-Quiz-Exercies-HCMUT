class Exp:
    def accept(self, visitor):
        pass

class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right

    def accept(self, visitor):
        return visitor.visit_binexp(self)

class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand

    def accept(self, visitor):
        return visitor.visit_unexp(self)

class IntLit(Exp):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_intlit(self)

class FloatLit(Exp):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_floatlit(self)


class Eval:
    def visit_binexp(self, exp):
        if exp.operator == '+':
            return exp.left.accept(self) + exp.right.accept(self)
        elif exp.operator == '-':
            return exp.left.accept(self) - exp.right.accept(self)
        elif exp.operator == '*':
            return exp.left.accept(self) * exp.right.accept(self)
        elif exp.operator == '/':
            return exp.left.accept(self) / exp.right.accept(self)

    def visit_unexp(self, exp):
        if exp.operator == '+':
            return exp.operand.accept(self)
        elif exp.operator == '-':
            return -exp.operand.accept(self)

    def visit_intlit(self, exp):
        return exp.value

    def visit_floatlit(self, exp):
        return exp.value


class PrintPrefix:
    def visit_binexp(self, exp):
        return f"{exp.operator} {exp.left.accept(self)} {exp.right.accept(self)}"

    def visit_unexp(self, exp):
        return f"{exp.operator}. {exp.operand.accept(self)}"

    def visit_intlit(self, exp):
        return str(exp.value)

    def visit_floatlit(self, exp):
        return str(exp.value)


class PrintPostfix:
    def visit_binexp(self, exp):
        return f"{exp.left.accept(self)} {exp.right.accept(self)} {exp.operator}"

    def visit_unexp(self, exp):
        return f"{exp.operand.accept(self)} {exp.operator}."

    def visit_intlit(self, exp):
        return str(exp.value)

    def visit_floatlit(self, exp):
        return str(exp.value)
