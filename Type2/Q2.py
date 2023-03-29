# Given the AST declarations as follows:

# class Program: #decl:List[Decl],stmts:List[Stmt]

# class Decl(ABC): #abstract class

# class VarDecl(Decl): #name:str

# class FuncDecl(Decl): #name:str,param:List[VarDecl],local:List[Decl],stmts:List[Stmt]

# class Stmt(ABC): #abstract class

# class Assign(Stmt): #lhs:Id,rhs:Exp

# class CallStmt(Stmt): #name:str,args:List[Exp]

# class Exp(ABC): #abstract class

# class IntLit(Exp): #val:int

# class FloatLit(Exp): #val:float

# class BoolLit(Exp): #val:bool

# class Id(Exp): #name:str

# and the Visitor class is declared as follows:

# Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

#? In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign
#? the type of an Id is inferred from the above constraints in the first usage, 
#? if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or
# If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the statement
# For static referencing environment, this language applies the scope rules of block-structured programming language where a function is a block. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.
# In a call statement, the argument type must be the same as the parameter type. If there is no function declaration in the static referencing environment, exception UndeclaredIdentifier should be raised together with the function call name. If the numbers of parameters and arguments are not the same or at least one argument type is not the same as the type of the corresponding parameter, exception TypeMismatchInStatement should be raise with the call statement. If there is at least one parameter type cannot be resolved, exception TypeCannotBeInferred should be raised together with the call statement.

class StaticCheck(Visitor):

    def visitProgram(self,ctx:Program,o):pass

    def visitVarDecl(self,ctx:VarDecl,o): pass

    def visitFuncDecl(self,ctx:FuncDecl,o): pass

    def visitCallStmt(self,ctx:CallStmt,o):pass

    def visitAssign(self,ctx:Assign,o): pass

    def visitIntLit(self,ctx:IntLit,o): pass 

    def visitFloatLit(self,ctx,o): pass

    def visitBoolLit(self,ctx,o): pass

    def visitId(self,ctx,o): pass