# Given the AST declarations as follows:

#? and the Visitor class is declared as follows:


#? Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

#? + , - , *, / accept their operands in int type and return int type

#? +., -., *., /. accept their operands in float type and return float type

#? > and = accept their operands in int type and return bool type

#? >. and =. accept their operands in float type and return bool type

#? !, &&, ||, >b and =b accept their operands in bool type and return bool type

#? i2f accepts its operand in int type and return float type

#? floor accept its operand in float type and return int type

#? In an assignment statement, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the assignment statement.

#? the type of an Id is inferred from the above constraints in the first usage, 

#? if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or

#* If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the name of the assignment statement.

#? If an expression does not conform the type constraints, the StaticCheck will raise exception TypeMismatchInExpression with the expression.

class StaticCheck(Visitor):
    #@ class Exp(ABC): #abstract class

    #@ class Program: #decl:List[VarDecl],stmts:List[Assign]
    def visitProgram(self,ctx:Program,o):
        o=[]
        for decl in ctx.decl:
            o.append(self.visit(decl,o))
        for stmt in ctx.stmts:
            self.visit(stmt,o)
        
    #@ class VarDecl: #name:str
    def visitVarDecl(self,ctx:VarDecl,o): 
        if ctx.name in o:
            raise TypeRedeclaration(ctx.name)
        return [ctx.name, None]

    #@ class Assign: #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o): 
        lhs = self.visit(ctx.lhs,o)
        rhs_type = self.visit(ctx.rhs,o)

        if lhs[1] == None:
            for id in o:
                if id[0] == lhs[0]:
                    id[1] = rhs_type
            lhs[1] = rhs_type

        a = 'int' if isinstance(rhs_type, int) else 'float' if isinstance(rhs_type, float) else 'bool'
        b = 'int' if isinstance(lhs, int) else 'float' if isinstance(lhs, float) else 'bool'

        if lhs != rhs_type:
            raise TypeMismatchInStatement(a + b)
        return None

    #@ class BinOp(Exp): #op:str,e1:Exp,e2:Exp #op is +,-,*,/,+.,-.,*.,/., &&,||, >, >., >b, =, =., =b
    def visitBinOp(self,ctx:BinOp,o): 
        left = self.visit(ctx.e1, o)
        right = self.visit(ctx.e2, o)
        op = ctx.op
        if op in ['+', '-', '*', '/']:
            if isinstance(left, int) and isinstance(right, int):
                return int() 
            else:
                raise TypeMismatchInExpression(ctx)
        elif op in ['+.','-.','*.','/.']:
            if isinstance(left, float) and isinstance(right, float):
                return float()
            raise TypeMismatchInExpression(ctx)
        elif op in ['>','=']:
            if isinstance(left, int) and isinstance(right, int):
                return bool() 
            raise TypeMismatchInExpression(ctx)
        elif op in ['>.','=.']:
            if isinstance(left, float) and isinstance(right, float):
                return bool() 
            raise TypeMismatchInExpression(ctx)
        elif op in ['!', '&&', '||', '>b','=b']:
            if isinstance(left, bool) and isinstance(right, bool):
                return bool()
            raise TypeMismatchInExpression(ctx)
        else:
            raise TypeMismatchInExpression(ctx)
        

    #@ class UnOp(Exp): #op:str,e:Exp #op is -,-., !,i2f, floor
    def visitUnOp(self,ctx:UnOp,o): 
        op = ctx.op
        value = ctx.e
        if op == 'i2f':
            if isinstance(value, int):
                return float()
            raise TypeMismatchInExpression(ctx)
        elif op == 'floor':
            if isinstance(value, float):
                return int()
            raise TypeMismatchInExpression(ctx)
        elif op == '-':
            if isinstance(value, int):
                return int()
            raise TypeMismatchInExpression(ctx)
        elif op == '-.':
            if isinstance(value,float):
                return float()
            raise TypeMismatchInExpression(ctx)
        elif op == '!':
            if isinstance(value, bool):
                return bool()
            raise TypeMismatchInExpression(ctx)
        else:
            raise TypeMismatchInExpression(ctx)

    #@ class IntLit(Exp): #val:int
    def visitIntLit(self,ctx:IntLit,o): 
        return int() 

    #@ class FloatLit(Exp): #val:float
    def visitFloatLit(self,ctx,o): 
        return float()

    #@ class BoolLit(Exp): #val:bool
    def visitBoolLit(self,ctx,o): 
        return bool()
    
    #@ class Id(Exp): #name:str
    def visitId(self,ctx,o): 
        for id in o:
            if id[0] == ctx.name:
                return id
        raise UndeclaredIdentifier(ctx.name)
