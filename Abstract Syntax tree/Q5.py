# Given the grammar of MP as follows:

# INTLIT: [0-9]+ ;

# BOOLIT: 'True' | 'False' ;

# ANDOR: 'and' | 'or' ;

# ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

# COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

# ID: [a-z]+ ;

# ?and AST classes as follows:

# @class Expr(ABC):

# $class Binary(Expr):  #op:string;left:Expr;right:Expr

# $class Id(Expr): #value:string

# $class IntLiteral(Expr): #value:int

# $class BooleanLiteral(Expr): #value:boolean

#? Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

class ASTGeneration(MPVisitor):

    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    # exp: term ASSIGN exp | term;
    def visitExp(self,ctx:MPParser.ExpContext):
        if ctx.ASSIGN():
            return Binary(ctx.ASSIGN().getText(), self.visit(ctx.term()), self.visit(ctx.exp()))
        return self.visit(ctx.term())

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(), self.visit(ctx.factor(0)), self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    # factor: factor ANDOR operand | operand; 
    def visitFactor(self,ctx:MPParser.FactorContext):
        if ctx.ANDOR():
            return Binary(ctx.ANDOR().getText(), self.visit(ctx.factor()), self.visit(ctx.operand()))
        return self.visit(ctx.operand())

    # operand: ID | INTLIT | BOOLIT | '(' exp ')';
    def visitOperand(self,ctx:MPParser.OperandContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.BOOLIT():
            return BooleanLiteral(ctx.BOOLIT().getText() == "True")
        else:
            return self.visit(ctx.exp())