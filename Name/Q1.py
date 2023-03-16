# Let AST of a programming language be defined as follows:

#? and exception RedeclaredDeclaration:

#@class RedeclaredDeclaration(Exception): #name:str

#? Implement the methods of the following class Visitor to travel on the above ASST to detect re-declared declarations (throw exception RedeclaredDeclaration):

class StaticCheck(Visitor):

    #@ class Program: #decl:List[Decl]
    #* decl.accept(self, o) --\  THE
    #* self.visit(decl,o)   --/  SAME
    def visitProgram(self,ctx:Program,o:object): 
        o = []
        for decl in ctx.decl:
            o.append(decl.accept(self,o))

    #$ class Decl(ABC): #abstract class
    #@ class VarDecl(Decl): #name:str,typ:Type
    def visitVarDecl(self,ctx:VarDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return ctx.name

    #@ class ConstDecl(Decl): #name:str,val:Lit
    def visitConstDecl(self,ctx:ConstDecl,o:object):
        if ctx.name in o:
            raise RedeclaredDeclaration(ctx.name)
        return ctx.name

    #$ class Type(ABC): #abstract class
    #@ class IntType(Type)
    def visitIntType(self,ctx:IntType,o:object):pass

    #@ class FloatType(Type)
    def visitFloatType(self,ctx:FloatType,o:object):pass

    #$ class Lit(ABC): #abstract class
    #@ class IntLit(Lit): #val:int
    def visitIntLit(self,ctx:IntLit,o:object):pass