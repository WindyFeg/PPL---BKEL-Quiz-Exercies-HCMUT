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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("D\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\3\3\7\3")
        buf.write("\34\n\3\f\3\16\3\37\13\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\5")
        buf.write("\5(\n\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\61\n\6\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\5\t>\n\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3\3\2")
        buf.write("\b\t\2>\2\26\3\2\2\2\4\35\3\2\2\2\6 \3\2\2\2\b%\3\2\2")
        buf.write("\2\n\60\3\2\2\2\f\62\3\2\2\2\16\65\3\2\2\2\20=\3\2\2\2")
        buf.write("\22?\3\2\2\2\24A\3\2\2\2\26\27\5\4\3\2\27\30\7\2\2\3\30")
        buf.write("\3\3\2\2\2\31\34\5\16\b\2\32\34\5\6\4\2\33\31\3\2\2\2")
        buf.write("\33\32\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2")
        buf.write("\2\36\5\3\2\2\2\37\35\3\2\2\2 !\5\24\13\2!\"\7\n\2\2\"")
        buf.write("#\5\b\5\2#$\5\22\n\2$\7\3\2\2\2%\'\7\3\2\2&(\5\n\6\2\'")
        buf.write("&\3\2\2\2\'(\3\2\2\2()\3\2\2\2)*\7\4\2\2*\t\3\2\2\2+,")
        buf.write("\5\f\7\2,-\7\6\2\2-.\5\n\6\2.\61\3\2\2\2/\61\5\f\7\2\60")
        buf.write("+\3\2\2\2\60/\3\2\2\2\61\13\3\2\2\2\62\63\5\24\13\2\63")
        buf.write("\64\5\20\t\2\64\r\3\2\2\2\65\66\5\24\13\2\66\67\5\20\t")
        buf.write("\2\678\7\6\2\28\17\3\2\2\29:\7\n\2\2:;\7\7\2\2;>\5\20")
        buf.write("\t\2<>\7\n\2\2=9\3\2\2\2=<\3\2\2\2>\21\3\2\2\2?@\7\5\2")
        buf.write("\2@\23\3\2\2\2AB\t\2\2\2B\25\3\2\2\2\7\33\35\'\60=")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'body'", "';'", "','", 
                     "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
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
    RULE_typ = 9

    ruleNames =  [ "program", "declares", "fundel", "param", "paramlist", 
                   "vardel", "vardel2", "idlist", "body", "typ" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    SM=4
    CM=5
    INT=6
    FLOAT=7
    ID=8
    WS=9
    ERROR_CHAR=10

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
            self.state = 20
            self.declares()
            self.state = 21
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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 23
                    self.vardel2()
                    pass

                elif la_ == 2:
                    self.state = 24
                    self.fundel()
                    pass


                self.state = 29
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
            self.state = 30
            self.typ()
            self.state = 31
            self.match(BKOOLParser.ID)
            self.state = 32
            self.param()
            self.state = 33
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
            self.state = 35
            self.match(BKOOLParser.T__0)
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 36
                self.paramlist()


            self.state = 39
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
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 41
                self.vardel()
                self.state = 42
                self.match(BKOOLParser.SM)
                self.state = 43
                self.paramlist()
                pass

            elif la_ == 2:
                self.state = 45
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
            self.state = 48
            self.typ()
            self.state = 49
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
            self.state = 51
            self.typ()
            self.state = 52
            self.idlist()
            self.state = 53
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
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                self.match(BKOOLParser.ID)
                self.state = 56
                self.match(BKOOLParser.CM)
                self.state = 57
                self.idlist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(BKOOLParser.T__2)
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
        self.enterRule(localctx, 18, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
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





