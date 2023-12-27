# Let AST of a programming language be defined as follows:

# and exceptions:

#% class UndeclaredIdentifier(Exception): #name:str

#% class UndeclaredField(Exception): #name:str

#% class UndeclaredClass(Exception): #name:str

#* Implement the methods of the following class Visitor to travel on the above AST to detect undeclared declarations (throw the exception UndeclaredIdentifier). Note that the redeclared declarations exception also is thrown if a redeclared declaration is detected:

# !NOT FINISHED
import functools 
class BKClass:
    def __init__(self, n, mem):
        self.name = n
        self.mem = mem

    def __str__(self):
        return self.name + ':' + str(self.mem)

class Member:
    def __init__(self, n, t):
        self.name = n
        self.typ = t

    def __str__(self):
        return self.name + ':' + str(self.typ)
    

class Environment(Visitor):
    def visitProgram(self,ctx:Program,o:object): 
        return functools.reduce(lambda x,y: x + self.visit(y, x), ctx.decl, [])
    
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        for x in o:
            if x.name == ctx.name:
                raise RedeclaredClass(ctx.name)
        return [BKClass(ctx.name, functools.reduce(lambda x,y: x + self.visit(y, x), ctx.mem, []))] + o

    def visitVarDecl(self,ctx:VarDecl,o:object):
        return [Member(ctx.name, self.visit(ctx.typ, o))] + o
    
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        return [Member(ctx.name, None)] + o

    # $class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):
        return 'int'

    # $class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):
        return 'float'
    
    # $class ClassType(Type):#name:str
    def visitClassType(self,ctx:ClassType,o:object):
        for x in o:
            if x.name == ctx.name:
                return ctx.name
        raise UndeclaredClass(ctx.name)

class StaticCheck(Visitor):

    #$ class Program: #decl:List[ClassDecl]
    def visitProgram(self,ctx:Program,o:object): 
        env = Environment().visit(ctx, [])
        for x in ctx.decl:
            self.visit(x, env)

    #$ class ClassDecl:#name:str,parent:str,mem:List[Decl]
    def visitClassDecl(self,ctx:ClassDecl,o:object):
        for x in ctx.mem:
            self.visit(x, o)

    #$ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        return [Member(ctx.name, self.visit(ctx.typ, o))] + o

    #$ class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        param = []
        for x in ctx.param:
            param.append(self.visit(x, o))

        for x in ctx.body[0]:
            param.append(self.visit(x, param + o))
        for x in ctx.body[1]:
            param.visit(x, param + o)
 

    # $class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):
        return 'int'

    # $class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):
        return 'float'

    # $class ClassType(Type):#name:str
    def visitClassType(self,ctx:ClassType,o:object):
        return ctx.name

    # $class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass

    #$ class Id(Expr): #name:str
    def visitId(self,ctx:Id,o:object):
        for cl in o:
            for mem in cl.mem:
                if mem.name == ctx.name:
                    return mem.typ
                
        raise UndeclaredIdentifier(ctx.name)

    #$ class FieldAccess(Expr): #exp:Expr,field:str
    def visitFieldAccess(self,ctx:FieldAccess,o:object):
        typ = None
        for e in ctx.exp:
            typ = self.visit(e, o)
            
        for cl in o:
            if cl.name == typ:
                for mem in cl.mem:
                    if mem.name == ctx.field:
                        return mem.typ
                raise UndeclaredField(ctx.field)