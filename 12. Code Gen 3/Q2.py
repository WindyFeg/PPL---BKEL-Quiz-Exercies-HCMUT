# Assume that 

#? class FuncDecl in AST is declared with field name in str type, param in List[VarDecl], returnType in Type type and body in Tuple[List[Type],List[Stmt]] where VarDecl has 2 fields: name in str type and typ in Type type. 
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Parameter o of method visitFuncDecl is passed an object whose field sym keeps a list of Symbol corresponding to the declarations visited.
#? When visiting the declarations and statements in parameter and body, the method visitFuncDecl must pass object SubBody which has two fields: frame containing the object Frame of this function declaration and sym containing the list of Symbol corresponding to the declarations from global (in o.sym) and the declaraions in this function in reverse order.
#? The method visitFuncDecl must print out a directive declarations  (use method printout(str) of Emitter), visit declarations and statement code and returns an object of Symbol which has field name in str type, mtype in Type type and value in Val type. The mtype field must contain a MType object and the value field must contain a CName object whose value contains self.className.
#? Based on the above assumption, write method visitFuncDecl(self,ctx,o) of visitor CodeGeneration? Your code is at line 85.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType which has field partype in List[Type] and field rettype in Type.


#$ return value: (jasmin <str>, Type <Type object>)
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL 

def visitFuncDecl(self, ctx, o):
    o.frame = Frame(ctx.name, ctx.returnType)
    o.frame.enterScope(True)

    InType = [x.typ for x in ctx.param]
    self.emit.printout(self.emit.emitMETHOD(ctx.name, MType(InType, ctx.returnType), True))

    LocalScope = []
    for pr in ctx.param:
        prSym = self.visit(pr, SubBody(o.frame, LocalScope))
        LocalScope += [prSym]

    for decl in ctx.body[0]:
        declSym = self.visit(decl, SubBody(o.frame, LocalScope))
        LocalScope += [declSym]

    self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))  # Function body begin here

    for stm in ctx.body[1]:
        self.visit(stm, o)

    self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))  # Function body end here

    self.emit.printout(self.emit.emitENDMETHOD(o.frame))
    o.frame.exitScope()

    return Symbol(ctx.name, MType(InType, ctx.returnType), CName(self.className))
