# Given the AST declarations as follows:

#? and the Visitor class is declared as follows:

#@ class Program: #decl:List[VarDecl],exp:Exp

#@ class VarDecl: #name:str,typ:Type

#@ class Type(ABC): #abstract class

#@ class IntType(Type)

#@ class FloatType(Type)

#@ class BoolType(Type)

#@ class Exp(ABC): #abstract class

#@ class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,&&,||, >, <, ==, or  !=

#@ class UnOp(Exp): #op:str,e:Exp #op is -, !

#@ class IntLit(Exp): #val:int

#@ class FloatLit(Exp): #val:float

#@ class BoolLit(Exp): #val:bool

#@ class Id(Exp): #name:str

#? Rewrite the body of the methods in class StaticCheck to check the following type constraints:

#? + , - and * accept their operands in int or float type and return float type if at least one of their operands is in float type, otherwise, return int type

#? / accepts their operands in int or float type and returns float type

#? !, && and || accept their operands in bool type and return bool type

#? >, <, == and != accept their operands in any type but must in the same type and return bool type

#? the type of an Id is from the declarations, if the Id is not in the declarations, exception UndeclaredIdentifier should be raised with the name of the Id. 

#? If the expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the innermost sub-expression that contains type mismatch.


class StaticCheck(Visitor):

    def visitProgram(self, ctx: Program, o):
        o=[]
        for decl in ctx.decl:
            o.append(self.visit(decl, o))
        return self.visit(ctx.exp, o)

    def visitVarDecl(self, ctx: VarDecl, o):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return ctx

    def visitIntType(self, ctx: IntType, o):
        return None

    def visitFloatType(self, ctx: FloatType, o):
        return None

    def visitBoolType(self, ctx: BoolType, o):
        return None

    def visitBinOp(self, ctx: BinOp, o):
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        op = ctx.op

        if op in ['+', '-', '*']:
            if isinstance(left, BoolType) or isinstance(right, BoolType):
                raise TypeMismatchInExpression(ctx)
            if isinstance(left, FloatType) or isinstance(right, FloatType):
                return FloatType()
            else:
                return IntType()

        elif op == '/':
            if isinstance(left, BoolType) or isinstance(right, BoolType):
                raise TypeMismatchInExpression(ctx)
            return FloatType()

        elif op in ['&&', '||', '!']:
            if not isinstance(left, BoolType) or not isinstance(right, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

        elif op in ['>', '<', '==', '!=']:
            if not type(left) == type(right):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitUnOp(self, ctx: UnOp, o):
        e = self.visit(ctx.e, o)
        op = ctx.op

        if op == '-':
            if isinstance(e, BoolType):
                raise TypeMismatchInExpression(ctx)
            if isinstance(e, FloatType):
                return FloatType()
            else:
                return IntType()

        elif op == '!':
            if not isinstance(e, BoolType):
                raise TypeMismatchInExpression(ctx)
            return BoolType()

    def visitIntLit(self, ctx: IntLit, o):
        return IntType()

    def visitFloatLit(self, ctx: FloatLit, o):
        return FloatType()

    def visitBoolLit(self, ctx: BoolLit, o):
        return BoolType()

    def visitId(self, ctx: Id, o):
        name = ctx.name
        for decl in o:
            if decl.name == name:
                return decl.typ
        raise UndeclaredIdentifier(ctx.name)
