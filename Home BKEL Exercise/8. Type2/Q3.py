# Given the AST declarations as follows:

from abc import ABC
class Program: #decl:List[Decl],stmts:List[Stmt]
    def __init__(self,decl,stmts):
        self.decl = decl
        self.stmts = stmts

    pass

class Decl(ABC): #abstract class
    pass

class VarDecl(Decl): #name:str
    def __init__(self,name):
        self.name = name

class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]
    def __init__(self,name,param,local,stmts):
        self.name = name
        self.param = param
        self.local = local
        self.stmts = stmts
    pass

class Stmt(ABC): #abstract class
    pass

class Assign(Stmt): #lhs:Id,rhs:Exp
    def __init__(self,lhs,rhs):
        self.lhs = lhs
        self.rhs = rhs
    pass

class CallStmt(Stmt): #name:str,args:List[Exp]
    def __init__(self,name,args):
        self.name = name
        self.args = args
    pass

class Exp(ABC): #abstract class
    pass

class IntLit(Exp): #val:int
    def __init__(self,val):
        self.val = val
    pass

class FloatLit(Exp): #val:float
    def __init__(self,val):
        self.val = val
    pass

class BoolLit(Exp): #val:bool
    def __init__(self,val):
        self.val = val

    pass

class Id(Exp): #name:str
    def __init__(self,name):
        self.name = name
    pass

# reddeclare
class Redeclared(Exception):
    def __init__(self,decl):
        self.decl = decl

# TypeMismatchInStatement
class TypeMismatchInStatement(Exception):
    def __init__(self,stmt):
        self.stmt = stmt

# UndeclaredIdentifier
class UndeclaredIdentifier(Exception):
    def __init__(self,ident):
        self.ident = ident

# TypeCannotBeInferred
class TypeCannotBeInferred(Exception):
    def __init__(self,stmt):
        self.stmt = stmt



# Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:
#
# In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
# the type of an Id is inferred from the above constraints in the first usage, 
# if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the statement
# For static referencing environment, this language applies the scope rules of block-structured programming language where a function is a block. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# In a call statement, the argument type must be the same as the parameter type. If there is no function declaration in the static referencing environment, exception UndeclaredIdentifier should be raised together with the function call name. If the numbers of parameters and arguments are not the same or at least one argument type is not the same as the type of the corresponding parameter, exception TypeMismatchInStatement should be raise with the call statement. If there is at least one parameter type cannot be resolved, exception TypeCannotBeInferred should be raised together with the call statement.
class BKEL(ABC):
    pass

class BKFunc(BKEL):
    def __init__(self, name, param, local, typ):
        self.name = name
        self.param = param  # list of types
        self.local = local
        self.typ = typ

    def __str__(self):
        return f"Function: {self.name}, Params: {self.param}, Locals: {self.local}, Type: {self.typ}"

class BKVar(BKEL):
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ

    def __str__(self):
        return f"Variable: {self.name}, Type: {self.typ}"
        
class IntType: pass
class FloatType: pass
class BoolType: pass

class Visitor(ABC): 
    def visit(self,ctx,o):
        return ctx.accept(self,o)
    pass
class StaticCheck(Visitor):

    def checkType(self, left, right):   
        if type(left) == type(right): 
            return True
        return False

    def visitProgram(self,ctx:Program,o):
        o = []
        for decl in ctx.decl:
            self.visit(decl,o)
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    def visitVarDecl(self,ctx:VarDecl,o): 
        for var in o:
            if ctx.name == var.name:
                raise Redeclared(ctx)

        o.append(BKVar(ctx.name,None))
        return 

    def visitFuncDecl(self,ctx:FuncDecl,o):
        for func in o:
            if ctx.name == func.name:
                raise Redeclared(ctx)

        op = [] 

        for param in ctx.param:
            self.visit(param,op)
        ol = op
        
        # print(op)
        for local in ctx.local:
            self.visit(local,ol)
        for stmt in ctx.stmts:
            self.visit(stmt,ol)
            
        a = o.append(BKFunc(ctx.name,op,None,None))

    def visitCallStmt(self,ctx:CallStmt,o):
        func = None

        for decl in o:
            if isinstance(decl,BKFunc) and decl.name == ctx.name:
                func = decl
                break
        # there is no function declaration in the static referencing environment
        if func == None:
            raise UndeclaredIdentifier(ctx.name)

        # the numbers of parameters and arguments are not the same 
        if len(func.param) != len(ctx.args):
            raise TypeMismatchInStatement(ctx)
        
        # print(func)
        for i in range(len(func.param)):
            if not self.checkType(func.param[i].typ,ctx.args[i]):
                arg = self.visit(ctx.args[i], o)
                typ_arg = arg.typ if isinstance(arg, BKVar) else arg
                # print("Call")
                # print(arg)
                # print(func.param[i].typ)
                
                if typ_arg == None and func.param[i].typ == None:
                    raise TypeCannotBeInferred(ctx)
                    
                # print(arg.typ)
                #if they not the same type, reassign to the missing type
                if func.param[i].typ == None and typ_arg != None:
                    func.param[i].typ = typ_arg
                    continue
                
                if (typ_arg == None) and (func.param[i].typ != None):
                    arg.typ = func.param[i].typ
                    continue
                
                raise TypeMismatchInStatement(ctx)

    def visitAssign(self,ctx:Assign,o):
        left = self.visit(ctx.lhs,o)  
        right = self.visit(ctx.rhs,o)
        
        typ_left = left.typ if isinstance(left, BKVar) else left
        typ_right = right.typ if isinstance(right, BKVar) else right
        
        # print("Assign")
        # print(typ_left)
        # print(typ_right)
        
        if typ_left == None and typ_right != None:
            left.typ = typ_right
            return

        if typ_right == None and typ_left != None:
            if isinstance(right, BKVar):
                right.typ = typ_left
            else:
                right = typ_left
            return
        
        if typ_left == None and typ_right == None:
            raise TypeCannotBeInferred(ctx)
            
        if typ_left != typ_right:
            raise TypeMismatchInStatement(ctx)
        return

    def visitIntLit(self, ctx:IntLit, o): 
        return IntType() 

    def visitFloatLit(self, ctx, o): 
        return FloatType()

    def visitBoolLit(self, ctx, o): 
        return BoolType()

    def visitId(self,ctx,o): 
        # print("--- Variables and Functions ---")
        # for item in o:
        #     print(item)
        # print("---")
    
        for id in o:
            if id.name == ctx.name:
                return id
                

