# Given the AST declarations as follows:

#? and the Visitor class is declared as follows:

#? Rewrite the body of the methods in class StaticCheck to infer the type of identifiers and check the following type constraints:

#? In an Assign, the type of lhs must be the same as that of rhs, otherwise, the exception TypeMismatchInStatement should be raised together with the Assign

#? the type of an Id is inferred from the above constraints in the first usage, 

#? if the Id is not in the declarations, exception UndeclaredIdentifier should be raised together with the name of the Id, or

#? If the Id cannot be inferred in the first usage, exception TypeCannotBeInferred should be raised together with the statement

#? For static referencing environment, this language applies the scope rules of block-structured programming language where a function is a block. When there is a declaration duplication of a name in a scope, exception Redeclared should be raised together with the second declaration.

#? In a call statement, the argument type must be the same as the parameter type. If there is no function declaration in the static referencing environment, exception UndeclaredIdentifier should be raised together with the function call name. If the numbers of parameters and arguments are not the same or at least one argument type is not the same as the type of the corresponding parameter, exception TypeMismatchInStatement should be raise with the call statement. If there is at least one parameter type cannot be resolved, exception TypeCannotBeInferred should be raised together with the call statement.

class IntType: pass
class FloatType: pass
class BoolType: pass
class StaticCheck(Visitor):
    # class Program: #decl:List[Decl],stmts:List[Stmt]
    def visitProgram(self,ctx:Program,o):
        o=[]
        for decl in ctx.decl:
            o.append(self.visit(decl,o))
        for stmt in ctx.stmts:
            self.visit(stmt,o)

    #@ class Decl(ABC): #abstract class
    #@ class VarDecl(Decl): #name:str
    def visitVarDecl(self,ctx:VarDecl,o): 
        for i in o:
            if ctx.name == i[0]:
                raise Redeclared(ctx) 
        return [ctx.name, None]

    #@ class Stmt(ABC): #abstract class
    #@ class FuncDecl(Decl): #name:str,
    #                        @param:List[VarDecl],
    #                        @local:List[Decl],
    #                        @stmts:List[Stmt]
    def visitFuncDecl(self,ctx:FuncDecl,o): 
        for i in o:
            if ctx.name == i[0]:
                raise Redeclared(ctx) 
        o1,o2 = [],[]
        for decl in ctx.param:
            # redeclare only in the newest scope
            o1.append(self.visit(decl,o1))
        for decl in ctx.local:
            # redeclare only in the newest scope
            o2.append(self.visit(decl,o1))
        for stmt in ctx.stmts:
            # check the newest scope to old scope
            self.visit(stmt,o1 + o2 + o)
        # [name, [[param1, type], [param2. type], ...]  
        return [ctx.name, o1]

    #@ class CallStmt(Stmt): #name:str,args:List[Exp]
    def visitCallStmt(self,ctx:CallStmt,o):
        # [name, [[param1, type], [param2. type], ...]  
        call_stmt = next((i for i in o if ctx.name == i[0]), None)

        if (not call_stmt) or (type(call_stmt[1]) is not list):
            raise UndeclaredIdentifier(ctx.name)
        # check the number of parameters and arguments
        if len(ctx.args) != len(call_stmt[1]):
            raise TypeMismatchInStatement(ctx)
        
        # loop through the arguments and parameters
        o1 = call_stmt[1]
        for i in range(len(ctx.args)):
            # [param1, type]
            param = o1[i]
            # type
            param_type = param[1]
            # type of argument
            arg_type = self.visit(ctx.args[i],o)

            # case both param and arg have type
            if arg_type and param_type:
                if type(arg_type) is not type(param_type):
                    raise TypeMismatchInStatement(ctx)
            # case only param or arg has type
            elif (not arg_type) and param_type:
                # update type for Id
                o.append(param_type)
                self.visit(ctx.args[i],o)
            elif arg_type and (not param_type):
                # update type for Id in param
                o1.append(arg_type)
                for j in o1:
                    if j[0] == param[0]:
                        j[1] = arg_type
                        break
                o1.pop()
            else:
                # case both param and agr have no type
                raise TypeCannotBeInferred(ctx)
            

    #@ class Assign(Stmt): #lhs:Id,rhs:Exp
    def visitAssign(self,ctx:Assign,o): 
        rhs_type = self.visit(ctx.rhs,o)
        lhs_type = self.visit(ctx.lhs,o)
        # case both lhs and rhs have type
        if lhs_type and rhs_type:
            if type(lhs_type) is not type(rhs_type):
                raise TypeMismatchInStatement(ctx)
        # case only lhs or rhs has type
        elif (not lhs_type) and rhs_type:
            #update type for Id
            o.append(rhs_type)
            self.visit(ctx.lhs,o)
        elif lhs_type and (not rhs_type):
            o.append(lhs_type)
            self.visit(ctx.rhs,o)
        # case both lhs and rhs have no type
        else:
            raise TypeCannotBeInferred(ctx)

    #@ class Exp(ABC): #abstract class
    #@ class IntLit(Exp): #val:int
    def visitIntLit(self,ctx:IntLit,o): 
        return IntType() 

    #@ class FloatLit(Exp): #val:float
    def visitFloatLit(self,ctx,o): 
        return FloatType()

    #@ class BoolLit(Exp): #val:bool
    def visitBoolLit(self,ctx,o): 
        return BoolType()
    
    #@ class Id(Exp): #name:str
    def visitId(self,ctx:Id,o): 
        # [param1, type]
        # [name, type]
        # take the last type assign to id
        for id in o:
            if id[0] == ctx.name:
                if type(o[-1]) in (IntType,FloatType,BoolType): 
                    id[1] = o.pop()
                    return None
                else:
                    return id[1]
        raise UndeclaredIdentifier(ctx.name)