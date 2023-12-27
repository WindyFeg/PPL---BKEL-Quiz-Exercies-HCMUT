# Generated from main/mt22/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#declares.
    def visitDeclares(self, ctx:BKOOLParser.DeclaresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#fundel.
    def visitFundel(self, ctx:BKOOLParser.FundelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#param.
    def visitParam(self, ctx:BKOOLParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#paramlist.
    def visitParamlist(self, ctx:BKOOLParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardel.
    def visitVardel(self, ctx:BKOOLParser.VardelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#vardel2.
    def visitVardel2(self, ctx:BKOOLParser.Vardel2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#idlist.
    def visitIdlist(self, ctx:BKOOLParser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#body.
    def visitBody(self, ctx:BKOOLParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statements.
    def visitStatements(self, ctx:BKOOLParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#stateassign.
    def visitStateassign(self, ctx:BKOOLParser.StateassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statecall.
    def visitStatecall(self, ctx:BKOOLParser.StatecallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#statereturn.
    def visitStatereturn(self, ctx:BKOOLParser.StatereturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#exprlist.
    def visitExprlist(self, ctx:BKOOLParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#expr.
    def visitExpr(self, ctx:BKOOLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#typ.
    def visitTyp(self, ctx:BKOOLParser.TypContext):
        return self.visitChildren(ctx)



del BKOOLParser