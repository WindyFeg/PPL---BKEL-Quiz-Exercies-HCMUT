# Assume that 

#? class While(Stmt) in AST is declared with fields expr  in Expr type; stmt in Stmt type. \
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object is passed to the parameter o of visitId has 2 fields:
#? Field frame keeps object Frame. 
#? Field sym of the argument keeps a list of Symbol which has three fields: name (str type), mtype (Type type) and value (Val type). The Val type has two concrete classes: Index with field value in int type and CName with field value in str type. An Index object keeps the index of the variable while a CName keeps the name of the class name (used for global variable). The first element of sym contains the identifier which belongs to the innermost referencing environment while the last element of sym contains one in the outermost referencing environment (global).
#? When visiting the expression of the if statement, object Access must be passed to parameter o where Access has 3 fields:
#? frame and sym are similar to the object passed to parameter o 
#? Field isLeft in boolean type indicates the identifier in the left (isLeft true) or in the right (isLeft false).
#? The method visitWhile must print out the code of the while statement (use method printout of Emitter).Note generating labels for break and continue statements inside the while statement 
#? Based on the above assumption, write method visitWhile(self,ctx,o) of visitor CodeGeneration? Your code is at line 265 .

#$ return value: (jasmin <str>, Type <Type object>)
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL 

def visitWhile(self,ctx,o):
    # Enter the loop and get the label for breaking out of it
    o.frame.enterLoop()
    labelExit = o.frame.getBreakLabel()

    # Emit a label for continuing the loop
    self.emit.printout(self.emit.emitLABEL(o.frame.getContinueLabel(),o.frame))

    # Evaluate the loop condition and jump to the end if false
    if_exprCode, if_exprType = ctx.expr.accept(self, Access(o.frame, o.sym, False))
    self.emit.printout(if_exprCode)
    self.emit.printout(self.emit.emitIFFALSE(labelExit,o.frame))

    # Visit the statement inside the loop and jump back to the beginning
    ctx.stmt.accept(self,o)
    self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(),o.frame))

    # Emit a label for exiting the loop and exit the frame
    self.emit.printout(self.emit.emitLABEL(labelExit,o.frame))
    o.frame.exitLoop()
