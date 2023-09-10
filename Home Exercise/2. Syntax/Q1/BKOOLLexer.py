# Generated from main/mt22/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("A\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\7\4")
        buf.write("*\n\4\f\4\16\4-\13\4\3\4\3\4\3\4\3\4\5\4\63\n\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\2\2\n\3")
        buf.write("\3\5\4\7\5\t\2\13\2\r\2\17\6\21\7\3\2\5\3\2\63;\3\2\62")
        buf.write(";\5\2\13\f\17\17\"\"\2@\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\3\23\3\2\2\2\5\33\3\2")
        buf.write("\2\2\7\62\3\2\2\2\t\64\3\2\2\2\13\66\3\2\2\2\r8\3\2\2")
        buf.write("\2\17:\3\2\2\2\21>\3\2\2\2\23\24\7x\2\2\24\25\7c\2\2\25")
        buf.write("\26\7t\2\2\26\27\7f\2\2\27\30\7g\2\2\30\31\7e\2\2\31\32")
        buf.write("\7n\2\2\32\4\3\2\2\2\33\34\7h\2\2\34\35\7w\2\2\35\36\7")
        buf.write("p\2\2\36\37\7e\2\2\37 \7f\2\2 !\7g\2\2!\"\7e\2\2\"#\7")
        buf.write("n\2\2#\6\3\2\2\2$+\t\2\2\2%&\5\13\6\2&\'\5\t\5\2\'*\3")
        buf.write("\2\2\2(*\5\t\5\2)%\3\2\2\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2")
        buf.write("\2+,\3\2\2\2,\63\3\2\2\2-+\3\2\2\2./\5\r\7\2/\60\7\"\2")
        buf.write("\2\60\61\b\4\2\2\61\63\3\2\2\2\62$\3\2\2\2\62.\3\2\2\2")
        buf.write("\63\b\3\2\2\2\64\65\t\3\2\2\65\n\3\2\2\2\66\67\7a\2\2")
        buf.write("\67\f\3\2\2\289\7\62\2\29\16\3\2\2\2:;\t\4\2\2;<\3\2\2")
        buf.write("\2<=\b\b\3\2=\20\3\2\2\2>?\13\2\2\2?@\b\t\4\2@\22\3\2")
        buf.write("\2\2\6\2)+\62\5\3\4\2\b\2\2\3\t\3")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    INT = 3
    WS = 4
    ERROR_CHAR = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "INT", "DIGIT", "UNDERLINE", "ZERO", "WS", 
                  "ERROR_CHAR" ]

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
            actions[2] = self.INT_action 
            actions[7] = self.ERROR_CHAR_action 
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
     


