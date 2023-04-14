# Assume that 

#? class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '>','<','>=','<=','!=','==' which can accept their operands in IntType or FloatType.  The result type of '+', '-', '*' is IntType if both operands are in IntType otherwise FloatType. The result type of '/' is FloatType and other relational operators are BoolType. Class Expr is the superclass of BinExpr, IntLiteral, FloatLiteral, BoolLiteral.
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
#? The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
#? Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.

# op: str, e1: Expr, e2: Expr
#! ALL OF CODE BELOW NEED TO BE TABBED WHEN SUBMITTING TO BKEL

def visitBinExpr(self, ctx, o):
    op = ctx.op
    exp1, typ1 = self.visit(ctx.e1, o)
    exp2, typ2 = self.visit(ctx.e2, o)

    # Check mtype
    if isinstance(typ1, FloatType) or isinstance(typ2, FloatType):
        mType = FloatType()
    else:
        mType = IntType()
    if op is '/':
        mType = FloatType()
    if type(typ1) is IntType and type(mType) != type(typ1):
        exp1 = exp1 + self.emit.emitI2F(o.frame)
    if type(typ2) is IntType and type(mType) != type(typ2):
        exp2 = exp2 + self.emit.emitI2F(o.frame)

    # Check op
    #@ emitREOP(self, op, inType, frame)
    #@ emitADDOP(self,lexeme, inType, frame)
    if op in ['>','<','>=','<=','!=','==']:
        return exp1 + exp2 + self.emit.emitREOP(op, mType, o.frame), BoolType()
    elif op in ['+', '-']:
        return exp1 + exp2 + self.emit.emitADDOP(op, mType, o.frame), mType
    elif op in ['*', '/']:
        return exp1 + exp2 + self.emit.emitMULOP(op, mType, o.frame), mType
