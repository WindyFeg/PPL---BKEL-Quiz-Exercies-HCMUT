class Exp:
    def eval(self):
        pass
    
    def printPrefix(self):
        pass
    
class BinExp(Exp):
    def __init__(self, left, operator, right):
        self.operator = operator
        self.left = left
        self.right = right
        
    def eval(self):
        if self.operator == '+':
            return self.left.eval() + self.right.eval()
        elif self.operator == '-':
            return self.left.eval() - self.right.eval()
        elif self.operator == '*':
            return self.left.eval() * self.right.eval()
        elif self.operator == '/':
            return self.left.eval() / self.right.eval()
        else:
            return self.left.eval()
        
    def printPrefix(self):
        return f"{self.operator} {self.left.printPrefix()} {self.right.printPrefix()}"
    
class UnExp(Exp):
    def __init__(self, operator, operand):
        self.operator = operator
        self.operand = operand
        
    def eval(self):
        if self.operator == '+':
            return self.operand.eval()
        elif self.operator == '-':
            return -self.operand.eval()
            
    def printPrefix(self):
        return f"{self.operator}. {self.operand.printPrefix()}"
            
class IntLit(Exp):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)
    
class FloatLit(Exp):
    def __init__(self, value):
        self.value = value
        
    def eval(self):
        return self.value
    
    def printPrefix(self):
        return str(self.value)
