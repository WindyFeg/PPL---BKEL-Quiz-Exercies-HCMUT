# Given the AST declarations as follows:

#@ class Exp(ABC): #abstract class

#@ class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

#@ class UnOp(Exp): #op:str,e:Exp #op is -, !

#@ class IntLit(Exp): #val:int

#@ class FloatLit(Exp): #val:float

#@ class BoolLit(Exp): #val:bool

#? and the Visitor class is declared as follows:


#? Rewrite the body of the methods in class StaticCheck to check the following type constraints:

#? + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type

#? / accepts their operands in int or float type and returns float type

#? !, && and || accept their operands in bool type and return bool type

#? >, <, == and != accept their operands in any type but must in the same type and return bool type 

#? If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.

class StaticCheck(Visitor):

    def visitBinOp(self,ctx:BinOp,o): 
        left = self.visit(ctx.e1,o)
        right = self.visit(ctx.e2,o)
        if ctx.op in ['+','-','*']:
            if isinstance(left, bool) or isinstance(right, bool):
                raise TypeMismatchInExpression(ctx)
            elif isinstance(left, int) and isinstance(right, int):
                return int()
            return float()

        elif ctx.op in ['/']:
            if isinstance(left, bool) or isinstance(right, bool):
                raise TypeMismatchInExpression(ctx)
            return float()
        
        elif ctx.op in ['&&','||', '!']:
            if isinstance(left, bool) and isinstance(right, bool):
                return bool()
            raise TypeMismatchInExpression(ctx)
        
        elif ctx.op in ['>','<','==','!=']:
            if type(left) == type(right):
                return bool()
            raise TypeMismatchInExpression(ctx)



    def visitUnOp(self,ctx:UnOp,o):
        value = self.visit(ctx.e,o)
        op = ctx.op

        if op in ['!']:
            if isinstance(value, bool):
                return bool()
            raise  TypeMismatchInExpression(ctx)
        elif op in ['-']:
            if isinstance(value, bool):
                raise TypeMismatchInExpression(ctx)
            return int() if isinstance(value, int) else float()

    def visitIntLit(self,ctx:IntLit,o): 
        return int()

    def visitFloatLit(self,ctx,o): 
        return float()

    def visitBoolLit(self,ctx,o): 
        return bool()
