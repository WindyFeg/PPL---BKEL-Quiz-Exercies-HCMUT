# Assume that 

 

# class For(Stmt) in AST is declared with fields idx in Id, ini, end, upd  in Expr type; stmt in Stmt type. \
# The visitor CodeGeneration has field emit keeping an object of Emitter 
# Object is passed to the parameter o of visitId has 2 fields:
# Field frame keeps object Frame. 
# Field sym of the argument keeps a list of Symbol which has three fields: name (str type), mtype (Type type) and value (Val type). The Val type has two concrete classes: Index with field value in int type and CName with field value in str type. An Index object keeps the index of the variable while a CName keeps the name of the class name (used for global variable). The first element of sym contains the identifier which belongs to the innermost referencing environment while the last element of sym contains one in the outermost referencing environment (global).
# When visiting the expression of the if statement, object Access must be passed to parameter o where Access has 3 fields:
# frame and sym are similar to the object passed to parameter o 
# Field isLeft in boolean type indicates the identifier in the left (isLeft true) or in the right (isLeft false).
# The method visitFor must print out the code of the for statement (use method printout of Emitter).Note generating labels for break and continue statements inside the for statement 
# Based on the above assumption, write method visitFor(self,ctx,o) of visitor CodeGeneration? Your code is at line 280 .

# #$ return value: (jasmin <str>, Type <Type object>)
# #! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL
# {
#   "idx": { /* content of Expr object representing initialization expression */ },
#   "ini": { /* content of Expr object representing initial value */ },
#   "end": { /* content of Expr object representing termination condition */ },
#   "upd": { /* content of Expr object representing update expression */ },
#   "stmt": { /* content of Stmt object representing loop body */ }
# }
    
def visitFor(self,ctx,o):
    o.frame.enterLoop()

    frame = o.frame
    labelBreak = frame.getBreakLabel()
    labelContinue = frame.getContinueLabel()
    labelFor = frame.getNewLabel()
    idx = ctx.idx

    #% visit(exp1)
    init_code, _ = self.visit(ctx.ini, Access(frame, o.sym, False))
    self.emit.printout(init_code)
    #% Assign value to index
    idx_code, _ = self.visit(idx, Access(frame, o.sym, True))
    self.emit.printout(idx_code)
    #* _______________________FOR_LOOP_______________________
    #% emitLABEL(LabelFor)
    self.emit.printout(self.emit.emitLABEL(labelFor, frame))

    #% Check index
    idx_code, _ = self.visit(idx, Access(frame, o.sym, False))
    self.emit.printout(idx_code)
    #% visit(exp2)
    cond_code, _ = self.visit(ctx.end, Access(frame, o.sym, False))
    self.emit.printout(cond_code)
    #% If Index <= exp2
    compare_code = self.emit.emitREOP('<=', IntType(), frame)
    self.emit.printout(compare_code)
    
    #% emitIFFALSE(LabelExit)
    self.emit.printout(self.emit.emitIFFALSE(labelBreak, frame))

    #% visit(stmt)
    self.visit(ctx.stmt, o)

    #% emitLABEL(LabelContinue)
    self.emit.printout(self.emit.emitLABEL(labelContinue, frame))

    #% visit(exp3)
    update_code, _ = self.visit(ctx.upd, Access(frame, o.sym, False))
    self.emit.printout(update_code)

    #% Take Index
    idx_code, _ = self.visit(idx, Access(frame, o.sym, False))
    self.emit.printout(idx_code)

    #% +
    add_code = self.emit.emitADDOP('+', IntType(), frame)
    self.emit.printout(add_code)

    #% Assign value to index
    idx_code, _ = self.visit(idx, Access(frame, o.sym, True))
    self.emit.printout(idx_code)

    #% emitGOTO(LabelFor)
    self.emit.printout(self.emit.emitGOTO(labelFor, frame))
    #* _______________________FOR_LOOP_______________________
    
    #% emitLABEL(LabelExit)
    self.emit.printout(self.emit.emitLABEL(labelBreak, frame))
    
    o.frame.exitLoop()
    return None, None
