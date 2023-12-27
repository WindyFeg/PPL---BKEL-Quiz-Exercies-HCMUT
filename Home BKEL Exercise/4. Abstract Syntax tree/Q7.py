# Given the grammar of MP as follows:

#* INTLIT: [0-9]+ ;

#* BOOLIT: 'True' | 'False' ;

#* ANDOR: 'and' | 'or' ;

#* ASSIGN: '+=' | '-=' | '&=' | '|=' | ':=' ;

#* COMPARE: '=' | '<>' | '>=' | '<=' | '<' | '>' ;

#* ID: [a-z]+ ;

# ?and AST classes as follows:

# @class Expr(ABC):

# $class Binary(Expr):  #op:string;left:Expr;right:Expr

# $class Id(Expr): #value:string

# $class IntLiteral(Expr): #value:int

# $class BooleanLiteral(Expr): #value:boolean

# ?Please copy the following class into your answer and modify the bodies of its methods to generate the AST of a MP input?

from functools import reduce
class ASTGeneration(MPVisitor):

    # program: exp EOF;
    def visitProgram(self,ctx:MPParser.ProgramContext):
        return self.visit(ctx.exp())

    # exp: (term ASSIGN)* term;
    # a := b := 4 : Binary(:=, a, Binary(:=, b, 4)
    #* (term ASSIGN 1) (term ASSIGN 2) (term 3)
    #* (term 3 ASSIGN) (term 2 ASSIGN) (term 1)
    def visitExp(self,ctx:MPParser.ExpContext):
        return reduce(
            lambda prev, curr: Binary(curr[1].getText(),
                        self.visit(curr[0]), # term
                        prev # 4
                        ),
            zip(ctx.term()[::-1][1::],
                ctx.ASSIGN()[::-1]), 
            # (b ASSIGN) (a ASSIGN)
            self.visit(ctx.term()[-1]) # 4
        )

    # term: factor COMPARE factor | factor;
    def visitTerm(self,ctx:MPParser.TermContext): 
        if ctx.COMPARE():
            return Binary(ctx.COMPARE().getText(),
                    self.visit(ctx.factor(0)),
                    self.visit(ctx.factor(1)))
        return self.visit(ctx.factor(0))

    # factor: operand (ANDOR operand)*; 
    # * a and (b and (c and d))
    def visitFactor(self,ctx:MPParser.FactorContext):
        return reduce(
            lambda prev, curr: Binary(curr[1].getText(), 
                                      prev, 
                                      self.visit(curr[0])),
            zip(ctx.operand()[1::], ctx.ANDOR()),
            self.visit(ctx.operand(0))
        )
        

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