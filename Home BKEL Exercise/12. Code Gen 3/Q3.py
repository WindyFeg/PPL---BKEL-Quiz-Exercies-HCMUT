# Assume that 

#? class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '&&' or  '||' which can accept their operands in BoolType and the result type is also BoolType. 
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
#? The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (BoolType). Note that the boolean expression must be short-circuit evaluated.
#? Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, BoolType, StringType, ArrayType, MType.


#$ return value: (jasmin <str>, Type <Type object>)
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL 

def visitBinExpr(self, ctx, o):
    frame = o.frame
    
    # Visit the first expression and duplicate its value on the stack
    (code, _) = ctx.e1.accept(self, o)
    code += self.emit.emitDUP(frame)

    if ctx.op == "&&":
        # Short-circuit for logical AND
        false_label = frame.getNewLabel()
        code += self.emit.emitIFFALSE(false_label, frame)
        
        # Visit the second expression and perform logical AND
        (_code, _) = ctx.e2.accept(self, o)
        code += _code
        code += self.emit.emitANDOP(frame)

        # Jump to the end of the binary expression
        end_bin = frame.getNewLabel()
        code += self.emit.emitGOTO(end_bin, frame)

        # Emit the false label and push false onto the stack
        code += self.emit.emitLABEL(false_label, frame)
        code += self.emit.emitPOP(frame)
        code += self.emit.emitPUSHICONST("false", frame)

        # Emit the end label
        code += self.emit.emitLABEL(end_bin, frame)
    else:
        # Short-circuit for logical OR
        true_label = frame.getNewLabel()
        code += self.emit.emitIFTRUE(true_label, frame)
        
        # Visit the second expression and perform logical OR
        (_code, _) = ctx.e2.accept(self, o)
        code += _code
        code += self.emit.emitOROP(frame)

        # Jump to the end of the binary expression
        end_bin = frame.getNewLabel()
        code += self.emit.emitGOTO(end_bin, frame)

        # Emit the true label and push true onto the stack
        code += self.emit.emitLABEL(true_label, frame)
        code += self.emit.emitPOP(frame)
        code += self.emit.emitPUSHICONST("true", frame)

        # Emit the end label
        code += self.emit.emitLABEL(end_bin, frame)

    # Return the code and the Boolean type
    return code, BoolType()
