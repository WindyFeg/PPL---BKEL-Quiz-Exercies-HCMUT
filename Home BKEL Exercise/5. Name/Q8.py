# Let AST of a programming language be defined as follows:

# class Program: #decl:List[Decl]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str,typ:Type

# class ConstDecl(Decl): #name:str,val:Lit

# class FuncDecl(Decl): #name:str,param:List[VarDecl],body:Tuple(List[Decl],List[Expr])

# class Type(ABC): #abstract class

# class IntType(Type)

# class FloatType(Type)

# class Expr(ABC): #abstract class

# class Lit(Expr): #abstract class

# class IntLit(Lit): #val:int

# class Id(Expr): #name:str

# and exceptions:

# class RedeclaredVariable(Exception): #name:str

# class RedeclaredConstant(Exception): #name:str

# class RedeclaredFunction(Exception): #name:str

# class UndeclaredIdentifier(Exception): #name:str

# Implement the methods of the following class Visitor to travel on the above AST to detect undeclared declarations (throw the exception UndeclaredIdentifier). Note that the redeclared declarations exception also is thrown if a redeclared declaration is detected:

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o:object):
        o = []
        for x in ctx.decl:
            o.append(self.visit(x,o))

    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredVariable(ctx.name)
        return ctx.name

    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredConstant(ctx.name)
        return ctx.name
    
    def visitFuncDecl(self,ctx:FuncDecl,o:object):
        if ctx.name in o:
            raise RedeclaredFunction(ctx.name)

        o1 = [o]
        for x in ctx.param:
            o1.append(self.visit(x, o1))
        
        for x in ctx.body[0]:
            o1.append(self.visit(x, o1 + [ctx.name] ))

        for x in ctx.body[1]:
            o1.append(self.visit(x, o1 + [ctx.name]))
        
        return ctx.name

    def visitIntType(self,ctx:IntType,o:object):pass

    def visitFloatType(self,ctx:FloatType,o:object):pass

    def visitIntLit(self,ctx:IntLit,o:object):pass

    def visitId(self,ctx:Id,o:object):
        def check_nested(obj):
            if ctx.name in obj:
                return True
            for name in obj:
                if isinstance(name, list):
                    return check_nested(name)
            return False
        
        if check_nested(o) is True:
            return
        raise UndeclaredIdentifier(ctx.name)
        