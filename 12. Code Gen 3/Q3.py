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
    (code, _) = ctx.e1.accept(self, o)
    code += self.emit.emitDUP(frame)
    if ctx.op == "&&":
        false_label = frame.getNewLabel()
        code += self.emit.emitIFFALSE(false_label, frame)
        (_code, _) = ctx.e2.accept(self, o)
        code += _code
        code += self.emit.emitANDOP(frame)
        end_bin = frame.getNewLabel()
        code += self.emit.emitGOTO(end_bin, frame)
        code += self.emit.emitLABEL(false_label, frame)
        code += self.emit.emitPOP(frame)
        code += self.emit.emitPUSHICONST("false", frame)
        code += self.emit.emitLABEL(end_bin, frame)
    else:
        true_label = frame.getNewLabel()
        code += self.emit.emitIFTRUE(true_label, frame)
        (_code, _) = ctx.e2.accept(self, o)
        code += _code
        code += self.emit.emitOROP(frame)
        end_bin = frame.getNewLabel()
        code += self.emit.emitGOTO(end_bin, frame)
        code += self.emit.emitLABEL(true_label, frame)
        code += self.emit.emitPOP(frame)
        code += self.emit.emitPUSHICONST("true", frame)
        code += self.emit.emitLABEL(end_bin, frame)
    return code, BoolType()