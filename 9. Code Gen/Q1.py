# Assume that 

#? class IntLiteral in AST is declared with field value in int type. 
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object Frame is kept in field frame of the argument passed to parameter o of visitIntLiteral
#? The method visitIntLiteral must return a pair of jasmin code of loading an int constant into operand stack and the type of the constant (one object of a subclass of class Type)
#? Based on the above assumption, write method visitIntLiteral(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL

def visitIntLiteral(self, ctx, o):
    codegen = self.emit.emitPUSHICONST(ctx.value, o.frame)
    return codegen, IntType()
