# Generated from c:\Users\pc\Downloads\cslang-initial\cslang-initial\src\main\CSlang\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\7")
        buf.write("\"\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\3\6\3\26\n\3\r\3\16\3\27")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\2\2\7\3\3\5\4\7\5")
        buf.write("\t\6\13\7\3\2\5\3\2c|\4\2\63;c|\5\2\13\f\17\17\"\"\2#")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\3\r\3\2\2\2\5\25\3\2\2\2\7\33\3\2\2\2\t\36\3")
        buf.write("\2\2\2\13 \3\2\2\2\r\21\t\2\2\2\16\20\t\3\2\2\17\16\3")
        buf.write("\2\2\2\20\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\4")
        buf.write("\3\2\2\2\23\21\3\2\2\2\24\26\t\4\2\2\25\24\3\2\2\2\26")
        buf.write("\27\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2")
        buf.write("\31\32\b\3\2\2\32\6\3\2\2\2\33\34\13\2\2\2\34\35\b\4\3")
        buf.write("\2\35\b\3\2\2\2\36\37\13\2\2\2\37\n\3\2\2\2 !\13\2\2\2")
        buf.write("!\f\3\2\2\2\6\2\17\21\27\4\b\2\2\3\4\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    WS = 2
    ERROR_CHAR = 3
    UNCLOSE_STRING = 4
    ILLEGAL_ESCAPE = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


