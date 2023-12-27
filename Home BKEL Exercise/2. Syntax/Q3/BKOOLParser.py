# Generated from main/mt22/parser/BKOOL.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("v\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\3\3\3")
        buf.write("\7\3(\n\3\f\3\16\3+\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5")
        buf.write("\5\64\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6=\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\tJ\n\t\3\n\3\n")
        buf.write("\3\n\7\nO\n\n\f\n\16\nR\13\n\3\n\3\n\3\13\3\13\3\13\5")
        buf.write("\13Y\n\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\5\rd\n")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\5\17")
        buf.write("p\n\17\3\20\3\20\3\21\3\21\3\21\2\2\22\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \2\3\3\2\f\r\2p\2\"\3\2\2\2\4")
        buf.write(")\3\2\2\2\6,\3\2\2\2\b\61\3\2\2\2\n<\3\2\2\2\f>\3\2\2")
        buf.write("\2\16A\3\2\2\2\20I\3\2\2\2\22K\3\2\2\2\24X\3\2\2\2\26")
        buf.write("\\\3\2\2\2\30`\3\2\2\2\32g\3\2\2\2\34o\3\2\2\2\36q\3\2")
        buf.write("\2\2 s\3\2\2\2\"#\5\4\3\2#$\7\2\2\3$\3\3\2\2\2%(\5\16")
        buf.write("\b\2&(\5\6\4\2\'%\3\2\2\2\'&\3\2\2\2(+\3\2\2\2)\'\3\2")
        buf.write("\2\2)*\3\2\2\2*\5\3\2\2\2+)\3\2\2\2,-\5 \21\2-.\7\16\2")
        buf.write("\2./\5\b\5\2/\60\5\22\n\2\60\7\3\2\2\2\61\63\7\3\2\2\62")
        buf.write("\64\5\n\6\2\63\62\3\2\2\2\63\64\3\2\2\2\64\65\3\2\2\2")
        buf.write("\65\66\7\4\2\2\66\t\3\2\2\2\678\5\f\7\289\7\n\2\29:\5")
        buf.write("\n\6\2:=\3\2\2\2;=\5\f\7\2<\67\3\2\2\2<;\3\2\2\2=\13\3")
        buf.write("\2\2\2>?\5 \21\2?@\5\20\t\2@\r\3\2\2\2AB\5 \21\2BC\5\20")
        buf.write("\t\2CD\7\n\2\2D\17\3\2\2\2EF\7\16\2\2FG\7\13\2\2GJ\5\20")
        buf.write("\t\2HJ\7\16\2\2IE\3\2\2\2IH\3\2\2\2J\21\3\2\2\2KP\7\5")
        buf.write("\2\2LO\5\24\13\2MO\5\16\b\2NL\3\2\2\2NM\3\2\2\2OR\3\2")
        buf.write("\2\2PN\3\2\2\2PQ\3\2\2\2QS\3\2\2\2RP\3\2\2\2ST\7\6\2\2")
        buf.write("T\23\3\2\2\2UY\5\26\f\2VY\5\30\r\2WY\5\32\16\2XU\3\2\2")
        buf.write("\2XV\3\2\2\2XW\3\2\2\2YZ\3\2\2\2Z[\7\n\2\2[\25\3\2\2\2")
        buf.write("\\]\7\16\2\2]^\7\7\2\2^_\5\36\20\2_\27\3\2\2\2`a\7\16")
        buf.write("\2\2ac\7\3\2\2bd\5\34\17\2cb\3\2\2\2cd\3\2\2\2de\3\2\2")
        buf.write("\2ef\7\4\2\2f\31\3\2\2\2gh\7\b\2\2hi\5\36\20\2i\33\3\2")
        buf.write("\2\2jk\5\36\20\2kl\7\13\2\2lm\5\34\17\2mp\3\2\2\2np\5")
        buf.write("\36\20\2oj\3\2\2\2on\3\2\2\2p\35\3\2\2\2qr\7\t\2\2r\37")
        buf.write("\3\2\2\2st\t\2\2\2t!\3\2\2\2\f\')\63<INPXco")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "'return'", 
                     "'expr'", "';'", "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "SM", "CM", "INT", "FLOAT", "ID", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_declares = 1
    RULE_fundel = 2
    RULE_param = 3
    RULE_paramlist = 4
    RULE_vardel = 5
    RULE_vardel2 = 6
    RULE_idlist = 7
    RULE_body = 8
    RULE_statements = 9
    RULE_stateassign = 10
    RULE_statecall = 11
    RULE_statereturn = 12
    RULE_exprlist = 13
    RULE_expr = 14
    RULE_typ = 15

    ruleNames =  [ "program", "declares", "fundel", "param", "paramlist", 
                   "vardel", "vardel2", "idlist", "body", "statements", 
                   "stateassign", "statecall", "statereturn", "exprlist", 
                   "expr", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    SM=8
    CM=9
    INT=10
    FLOAT=11
    ID=12
    WS=13
    ERROR_CHAR=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declares(self):
            return self.getTypedRuleContext(BKOOLParser.DeclaresContext,0)


        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.declares()
            self.state = 33
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardel2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Vardel2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Vardel2Context,i)


        def fundel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FundelContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FundelContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_declares

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclares" ):
                return visitor.visitDeclares(self)
            else:
                return visitor.visitChildren(self)




    def declares(self):

        localctx = BKOOLParser.DeclaresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declares)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 37
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 35
                    self.vardel2()
                    pass

                elif la_ == 2:
                    self.state = 36
                    self.fundel()
                    pass


                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FundelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_fundel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFundel" ):
                return visitor.visitFundel(self)
            else:
                return visitor.visitChildren(self)




    def fundel(self):

        localctx = BKOOLParser.FundelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_fundel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.typ()
            self.state = 43
            self.match(BKOOLParser.ID)
            self.state = 44
            self.param()
            self.state = 45
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKOOLParser.T__0)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 48
                self.paramlist()


            self.state = 51
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardel(self):
            return self.getTypedRuleContext(BKOOLParser.VardelContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def paramlist(self):
            return self.getTypedRuleContext(BKOOLParser.ParamlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = BKOOLParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramlist)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 53
                self.vardel()
                self.state = 54
                self.match(BKOOLParser.SM)
                self.state = 55
                self.paramlist()
                pass

            elif la_ == 2:
                self.state = 57
                self.vardel()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardel" ):
                return visitor.visitVardel(self)
            else:
                return visitor.visitChildren(self)




    def vardel(self):

        localctx = BKOOLParser.VardelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.typ()
            self.state = 61
            self.idlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardel2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardel2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardel2" ):
                return visitor.visitVardel2(self)
            else:
                return visitor.visitChildren(self)




    def vardel2(self):

        localctx = BKOOLParser.Vardel2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_vardel2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.typ()
            self.state = 64
            self.idlist()
            self.state = 65
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def idlist(self):
            return self.getTypedRuleContext(BKOOLParser.IdlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = BKOOLParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_idlist)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(BKOOLParser.ID)
                self.state = 68
                self.match(BKOOLParser.CM)
                self.state = 69
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(BKOOLParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.StatementsContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.StatementsContext,i)


        def vardel2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Vardel2Context)
            else:
                return self.getTypedRuleContext(BKOOLParser.Vardel2Context,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(BKOOLParser.T__2)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKOOLParser.T__5) | (1 << BKOOLParser.INT) | (1 << BKOOLParser.FLOAT) | (1 << BKOOLParser.ID))) != 0):
                self.state = 76
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKOOLParser.T__5, BKOOLParser.ID]:
                    self.state = 74
                    self.statements()
                    pass
                elif token in [BKOOLParser.INT, BKOOLParser.FLOAT]:
                    self.state = 75
                    self.vardel2()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 80
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self.match(BKOOLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(BKOOLParser.SM, 0)

        def stateassign(self):
            return self.getTypedRuleContext(BKOOLParser.StateassignContext,0)


        def statecall(self):
            return self.getTypedRuleContext(BKOOLParser.StatecallContext,0)


        def statereturn(self):
            return self.getTypedRuleContext(BKOOLParser.StatereturnContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = BKOOLParser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 83
                self.stateassign()
                pass

            elif la_ == 2:
                self.state = 84
                self.statecall()
                pass

            elif la_ == 3:
                self.state = 85
                self.statereturn()
                pass


            self.state = 88
            self.match(BKOOLParser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateassignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_stateassign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateassign" ):
                return visitor.visitStateassign(self)
            else:
                return visitor.visitChildren(self)




    def stateassign(self):

        localctx = BKOOLParser.StateassignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_stateassign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(BKOOLParser.ID)
            self.state = 91
            self.match(BKOOLParser.T__4)
            self.state = 92
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatecallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statecall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatecall" ):
                return visitor.visitStatecall(self)
            else:
                return visitor.visitChildren(self)




    def statecall(self):

        localctx = BKOOLParser.StatecallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_statecall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(BKOOLParser.ID)
            self.state = 95
            self.match(BKOOLParser.T__0)
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.T__6:
                self.state = 96
                self.exprlist()


            self.state = 99
            self.match(BKOOLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatereturnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statereturn

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatereturn" ):
                return visitor.visitStatereturn(self)
            else:
                return visitor.visitChildren(self)




    def statereturn(self):

        localctx = BKOOLParser.StatereturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_statereturn)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(BKOOLParser.T__5)
            self.state = 102
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def CM(self):
            return self.getToken(BKOOLParser.CM, 0)

        def exprlist(self):
            return self.getTypedRuleContext(BKOOLParser.ExprlistContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = BKOOLParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprlist)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.expr()
                self.state = 105
                self.match(BKOOLParser.CM)
                self.state = 106
                self.exprlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 108
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(BKOOLParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





