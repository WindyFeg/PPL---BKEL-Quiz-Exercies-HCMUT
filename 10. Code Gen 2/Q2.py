# Assume that 

#? class BinExpr in AST is declared with field op in str type, e1 and e2 in Expr type. op can be '+', '-', '*', '/', '>','<','>=','<=','!=','==' which can accept their operands in IntType or FloatType.  The result type of '+', '-', '*' is IntType if both operands are in IntType otherwise FloatType. The result type of '/' is FloatType and other relational operators are BoolType. Class Expr is the superclass of BinExpr, IntLiteral, FloatLiteral, BoolLiteral.
#? The visitor CodeGeneration has field emit keeping an object of Emitter 
#? Object Frame is kept in field frame of the argument passed to parameter o of visitBinExpr
#? The method visitBinExpr must return a pair of jasmin code of a binary expression and the type of the result (one object of a subclass of class Type)
#? Based on the above assumption, write method visitBinExpr(self,ctx,o) of visitor CodeGeneration? Your code is at line 160.
#? Remind that class Type has subclasses: IntType, FloatType, VoidType, StringType, ArrayType, MType.

