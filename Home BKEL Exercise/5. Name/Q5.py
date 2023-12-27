# Let AST of a programming language be defined as follows:

# class RedeclaredField(Exception): #name:str

# class RedeclaredMethod(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above AST to detect redeclared declarations (throw the exception RedeclaredMethod or RedeclaredField). 

class StaticCheck(Visitor):

    #$ class Program: #decl:List[ClassDecl]
    def visitProgram(self,ctx:Program,o:object):
        for x in ctx.decl:
            self.visit(x,o)

    # class Decl(ABC): #abstract class
    #$ class ClassDecl:#name:str,parent:str,mem:List[Decl]
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        o = []
        for x in ctx.mem:
            o.append(self.visit(x,o))

    #$ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        return ctx.name

    #$ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredMethod(ctx.name)

        object = []
        for x in ctx.param:
            self.visit(x,object)
        for x in ctx.body[0]:
            self.visit(x,object)
        for x in ctx.body[1]:
            self.visit(x,object)
        return ctx.name

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitClassType(self,ctx:ClassType,o:object):pass

    #$ class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    #$ class Id(Expr): #name:str
    def visitId(self,ctx:Id,o:object):pass

    #$ class FieldAccess(Expr): #exp:Expr,field:str
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        if ctx.field == o:
            raise RedeclaredField(ctx.field)
        o.append(ctx.field)
