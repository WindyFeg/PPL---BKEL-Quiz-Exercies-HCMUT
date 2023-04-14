
#* class If(Stmt) in AST is declared with fields expr  in Expr type; tstmt and estmt in Stmt type.  In case the if statement has no else, the estmt gets None value. 
# The visitor CodeGeneration has field emit keeping an object of Emitter 
# Object is passed to the parameter o of visitId has 2 fields:
# Field frame keeps object Frame. 
# Field sym of the argument keeps a list of Symbol which has three fields: name (str type), mtype (Type type) and value (Val type). The Val type has two concrete classes: Index with field value in int type and CName with field value in str type. An Index object keeps the index of the variable while a CName keeps the name of the class name (used for global variable). The first element of sym contains the identifier which belongs to the innermost referencing environment while the last element of sym contains one in the outermost referencing environment (global).
# When visiting the expression of the if statement, object Access must be passed to parameter o where Access has 3 fields:
# frame and sym are similar to the object passed to parameter o 
# Field isLeft in boolean type indicates the identifier in the left (isLeft true) or in the right (isLeft false).
# The method visitIf must print out the code of the if statement (use method printout of Emitter)

#$ Object o:
# o = {
#     "frame": <Frame object>,
#     "sym": [
#         {
#             "name": "x",
#             "mtype": <Type object>,
#             "value": <Index or CName object> {value: <int or str>}
#         },
#         ...
#     ]
# }

#$ Object Access:
# Access = {
#     "frame": <Frame object>,
#     "sym": [
#         {
#             "name": "x",
#             "mtype": <Type object>,
#             "value": <Index or CName object> {value: <int or str>}
#         },
#         ...
#     ],
#     "isLeft": <boolean>
# }

# expr: Expr, tstmt: Stmt, estmt: Stmt
def visitIf(self,ctx,o):
    if_exprCode, if_exprType = ctx.expr.accept(self, Access(o.frame, o.sym, False))
    if ctx.estmt:
        labelElse = o.frame.getNewLabel()
        labelExit = o.frame.getNewLabel()
        self.emit.printout(if_exprCode)
        self.emit.printout(self.emit.emitIFFALSE(labelElse, o.frame))
        ctx.tstmt.accept(self, o)
        self.emit.printout(self.emit.emitGOTO(labelExit, o.frame))
        self.emit.printout(self.emit.emitLABEL(labelElse, o.frame))
        ctx.estmt.accept(self, o)
        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))
    else:
        labelExit = o.frame.getNewLabel()
        self.emit.printout(if_exprCode)
        self.emit.printout(self.emit.emitIFFALSE(labelExit, o.frame))
        ctx.tstmt.accept(self, o)
        self.emit.printout(self.emit.emitLABEL(labelExit, o.frame))