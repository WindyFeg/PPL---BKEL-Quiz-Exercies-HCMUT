# Let AST of a programming language be defined as follows:

# and exceptions:

# class UndeclaredIdentifier(Exception): #name:str

# class UndeclaredField(Exception): #name:str

# class UndeclaredClass(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above AST to detect undeclared declarations (throw the exception UndeclaredIdentifier). Note that the redeclared declarations exception also is thrown if a redeclared declaration is detected:
class Environment(Visitor):
    def visitProgram(self,ctx:Program,o:object):
        o = []
        for x in ctx.decl:
            self.visit(x,o)
    
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        if ctx.name in o:
            raise RedeclaredClass(ctx.name)
        return ctx.name

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        return ctx.name

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredField(ctx.name)
        return ctx.name

    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredMethod(ctx.name)
        return ctx.name

    def visitIntType(self,ctx:IntType,o:object):
        pass

    def visitFloatType(self,ctx:FloatType,o:object):
        pass

    def visitClassType(self,ctx:ClassType,o:object):
        pass

    def visitIntLit(self,ctx:IntLit,o:object):
        pass

    def visitId(self,ctx:Id,o:object):
        pass

    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        pass


class StaticCheck(Visitor):

    #$ class Program: #decl:List[ClassDecl]
    def visitProgram(self,ctx:Program,o:object):
        pass

    # class Decl(ABC): #abstract class
    #$ class ClassDecl:#name:str,parent:str,mem:List[Decl]
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        pass


    #$ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        pass

    #$ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        pass

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    #$ class ClassType(Type):#$name:str
    def visitClassType(self,ctx:ClassType,o:object):
        pass

    #$ class IntLit(Lit): #$val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    #$ class Id(Expr): #$name:str
    def visitId(self,ctx:Id,o:object):
        pass
    #$ class FieldAccess(Expr): #exp:Expr,field:str
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        pass