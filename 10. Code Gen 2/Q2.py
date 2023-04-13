# Assume that 

#? class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '>','<','>=','<=','!=','==' which can accept their operands in IntType or FloatType.  The result type of '+', '-', '*' is IntType if both operands are in IntType otherwise FloatType. The result type of '/' is FloatType and other relational operators are BoolType. Class Expr is the superclass of BinExpr, IntLiteral, FloatLiteral, BoolLiteral.
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
#? The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
#? Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.

def visitBinExpr(self, ctx, o):
    expr1, expr1_type = self.visit(ctx.e1, o)
    expr2, expr2_type = self.visit(ctx.e2, o)
    if ctx.op in ['+', '-', '*', '/']:
        if expr1_type == IntType() and expr2_type == IntType():
            result_type = IntType()
        else:
            result_type = FloatType()
        op = ctx.op
        emit_code = expr1 + expr2
        if op == '+':
            emit_code += self.emit.emitADDOP(op, result_type, o.frame)
        elif op == '-':
            emit_code += self.emit.emitSUBOP(op, result_type, o.frame)
        elif op == '*':
            emit_code += self.emit.emitMULOP(op, result_type, o.frame)
        elif op == '/':
            emit_code += self.emit.emitDIV(op, result_type, o.frame)
    elif ctx.op in ['>', '<', '>=', '<=', '==', '!=']:
        result_type = BoolType()
        op = ctx.op
        if expr1_type == FloatType() or expr2_type == FloatType():
            emit_code = expr1 + expr2 + self.emit.emitREOP(op, FloatType(), o.frame)
        else:
            emit_code = expr1 + expr2 + self.emit.emitREOP(op, IntType(), o.frame)
    return emit_code, result_type
