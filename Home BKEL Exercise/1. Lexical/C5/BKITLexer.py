# Generated from c:\Users\pc\Downloads\cslang-initial\cslang-initial\src\main\CSlang\parser\BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\b")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\3\2\3\2\7\2\22\n\2\f\2\16\2\25\13\2\3\3\3\3\3\3\5\3")
        buf.write("\32\n\3\3\3\7\3\35\n\3\f\3\16\3 \13\3\5\3\"\n\3\3\3\3")
        buf.write("\3\3\4\6\4\'\n\4\r\4\16\4(\3\4\3\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\7\3\7\2\2\b\3\3\5\4\7\5\t\6\13\7\r\b\3\2\7\3\2c|\4")
        buf.write("\2\63;c|\3\2\63;\3\2\62;\5\2\13\f\17\17\"\"\2\67\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\3\17\3\2\2\2\5!\3\2\2\2\7&\3\2\2\2\t,\3")
        buf.write("\2\2\2\13/\3\2\2\2\r\61\3\2\2\2\17\23\t\2\2\2\20\22\t")
        buf.write("\3\2\2\21\20\3\2\2\2\22\25\3\2\2\2\23\21\3\2\2\2\23\24")
        buf.write("\3\2\2\2\24\4\3\2\2\2\25\23\3\2\2\2\26\"\7\62\2\2\27\36")
        buf.write("\t\4\2\2\30\32\7a\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33")
        buf.write("\3\2\2\2\33\35\t\5\2\2\34\31\3\2\2\2\35 \3\2\2\2\36\34")
        buf.write("\3\2\2\2\36\37\3\2\2\2\37\"\3\2\2\2 \36\3\2\2\2!\26\3")
        buf.write("\2\2\2!\27\3\2\2\2\"#\3\2\2\2#$\b\3\2\2$\6\3\2\2\2%\'")
        buf.write("\t\6\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()\3\2\2\2)*\3")
        buf.write("\2\2\2*+\b\4\3\2+\b\3\2\2\2,-\13\2\2\2-.\b\5\4\2.\n\3")
        buf.write("\2\2\2/\60\13\2\2\2\60\f\3\2\2\2\61\62\13\2\2\2\62\16")
        buf.write("\3\2\2\2\t\2\21\23\31\36!(\5\3\3\2\b\2\2\3\5\3")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    INT = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "INT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[1] = self.INT_action 
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     


