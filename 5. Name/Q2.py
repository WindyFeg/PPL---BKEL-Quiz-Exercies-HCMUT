# Let AST of a programming language be defined as follows:

# and exceptions:

#$ class RedeclaredVariable(Exception): #name:str

#$ class RedeclaredConstant(Exception): #name:str

#$ class RedeclaredFunction(Exception): #name:str

# ?Implement the methods of the following class Visitor to travel on the above AST to detect redeclared declarations (throw the exception corresponding to the second declaration with the same name) in the same scope:

class StaticCheck(Visitor):
    # x = Program([VarDecl("b",IntType()),
    # FuncDecl("a",
    #   [VarDecl("a",FloatType())],
    #   [ConstDecl("c",IntLit(3)),VarDecl("b",IntType()),VarDecl("c",IntType())])
    # ])


    #@ class Program: #decl:List[Decl]
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o.append(decl.accept(self,o))
    #@ class Decl(ABC): #abstract class
    #@ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name
    #@ class ConstDecl(Decl): #name:str,val:Lit
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name

    #@ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:List[Decl]
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name) 
        o_func = []
        for decl in (ctx.param + ctx.body):
            o_func.append(decl.accept(self,o_func))
        return ctx.name
    
    #@ class Type(ABC): #abstract class
    #@ class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):pass

    #@ class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):pass

    #@ class Lit(ABC): #abstract class
    #@ class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass