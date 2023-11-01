# Let AST of a programming language be defined as follows:

# and exceptions:

# class UndeclaredIdentifier(Exception): #name:str

# class UndeclaredField(Exception): #name:str

# class UndeclaredClass(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above AST to detect undeclared declarations (throw the exception UndeclaredIdentifier). Note that the redeclared declarations exception also is thrown if a redeclared declaration is detected:

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
            if isinstance(x,VarDecl):
                o.append(self.visit(x,o))

        for x in ctx.mem:
            if isinstance(x,FuncDecl):
                o.append(self.visit(x,o))

    #$ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise UndeclaredField(ctx.name)
        return ctx.name

    #$ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredMethod(ctx.name)

        object = o
        for x in ctx.param:
            object.append(self.visit(x,object))
        for x in ctx.body[0]:
            object.append(self.visit(x,object))
        for x in ctx.body[1]:
            self.visit(x,object)
        return ctx.name

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    #$ class ClassType(Type):#$name:str
    def visitClassType(self,ctx:ClassType,o:object):
        if ctx.name not in o:
            raise UndeclaredClass(ctx.name)

    #$ class IntLit(Lit): #$val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    #$ class Id(Expr): #$name:str
    def visitId(self,ctx:Id,o:object):
        if ctx.name not in o:
            raise UndeclaredIdentifier(ctx.name)

    #$ class FieldAccess(Expr): #exp:Expr,field:str
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        if ctx.field not in o:
            raise UndeclaredField(ctx.field)
        o.append(ctx.field)