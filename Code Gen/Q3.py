# Assume that 

# class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '+.', '-.', '*.', '/.' where '+', '-', '*', '/' accept 2 operands e1, e2 in IntType and the others accept their operands in FloatType. No Type Error happens. Class Expr is the superclass of BinExpr, IntLiteral and FloatLiteral.
# The visitor CodeGeneration has field emit keeping an object of Emitter 
# Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
# The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
# Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
# Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.

# Test	Expected	Got	
# CallExpr(Id("putInt"),[BinExpr("+",IntLiteral(5),IntLiteral(3))])
# b'8'
# b'8'
# CallExpr(Id("putInt"),[BinExpr("*",BinExpr("-",IntLiteral(5),IntLiteral(3)),IntLiteral(3))])
# b'6'
# b'6'
# CallExpr(Id("putFloat"),[BinExpr("+.",FloatLiteral(-1.0),FloatLiteral(1.0))])
# b'0.0'
# b'0.0'
# CallExpr(Id("putFloat"),[BinExpr("*.",FloatLiteral(1.0),BinExpr("-.",FloatLiteral(10.0),FloatLiteral(2.0)))])
# b'8.0'
# b'8.0'
# CallExpr(Id("putInt"),[BinExpr("/",BinExpr("-",IntLiteral(5),IntLiteral(3)),IntLiteral(3))])
# b'0'
# b'0'

    def visitBinExpr(self,ctx,o):
        expr1, expr1_type = self.visit(ctx.e1,o)
        expr2, expr2_type = self.visit(ctx.e2,o)
        if ctx.op in ['+', '-']: 
            codegen =expr1 + expr2 + self.emit.emitADDOP(ctx.op, IntType(), o.frame)
            return codegen, IntType()
        if ctx.op in ['*', '/']: 
            codegen =expr1 + expr2 + self.emit.emitMULOP(ctx.op, IntType(), o.frame)
            return codegen, IntType()
        if ctx.op in ['+.', '-.']:
            codegen = expr1 + expr2 + self.emit.emitADDOP(ctx.op[0], FloatType(), o.frame)
            return codegen, FloatType()
        if ctx.op in ['*.', '/.']:
            codegen = expr1 + expr2 + self.emit.emitMULOP(ctx.op[0], FloatType(), o.frame)
            return codegen, FloatType()