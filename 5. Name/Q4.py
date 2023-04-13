# Let AST of a programming language be defined as follows:

# ?and exceptions:

#$ class RedeclaredVariable(Exception): #name:str

#$ class RedeclaredConstant(Exception): #name:str

#$ class RedeclaredFunction(Exception): #name:str

#$ class UndeclaredIdentifier(Exception): #name:str

# ?Implement the methods of the following class Visitor to travel on the above AST to detect undeclared declarations (throw the exception UndeclaredIdentifier). Note that the redeclared declarations exception also is thrown if a redeclared declaration is detected:

class StaticCheck(Visitor):

    #@ class Decl(ABC): #abstract class
    #@ class Expr(ABC): #abstract class
    #@      class Lit(Expr): #abstract class
    #@ class Type(ABC): #abstract class

    #@ class Program: #decl:List[Decl]
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o.append(decl.accept(self,o))

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

    #@ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)
        o_func = []
        #* Check for redeclared variable in param
        for vardecl in ctx.param:
            o_func.append(self.visit(vardecl,o_func))
        #* Check for redeclared variable in body
        for decl in ctx.body[0]:
            if isinstance(decl,FuncDecl):
                o_func.append(self.visit(decl,o+o_func+[ctx.name]))
            else:
                o_func.append(self.visit(decl,o+ o_func))
        o_func = o + o_func+[ctx.name]
        for expr in ctx.body[1]:
            self.visit(expr,o_func)
        return ctx.name

    #@ class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):pass

    #@ class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):pass

    
    #@ class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    #@ class Id(Expr): #name:str
    def visitId(self,ctx:Id,o:object):
     if not ctx.name in o:
        raise UndeclaredIdentifier(ctx.name)