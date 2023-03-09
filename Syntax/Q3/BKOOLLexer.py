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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("O\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\6\rE\n\r\r\r\16\rF\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\2\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\3\2\4\5\2\62;C\\c|\5\2\13")
        buf.write("\f\17\17\"\"\2O\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17\60")
        buf.write("\3\2\2\2\21\65\3\2\2\2\23\67\3\2\2\2\259\3\2\2\2\27=\3")
        buf.write("\2\2\2\31D\3\2\2\2\33H\3\2\2\2\35L\3\2\2\2\37 \7*\2\2")
        buf.write(" \4\3\2\2\2!\"\7+\2\2\"\6\3\2\2\2#$\7}\2\2$\b\3\2\2\2")
        buf.write("%&\7\177\2\2&\n\3\2\2\2\'(\7?\2\2(\f\3\2\2\2)*\7t\2\2")
        buf.write("*+\7g\2\2+,\7v\2\2,-\7w\2\2-.\7t\2\2./\7p\2\2/\16\3\2")
        buf.write("\2\2\60\61\7g\2\2\61\62\7z\2\2\62\63\7r\2\2\63\64\7t\2")
        buf.write("\2\64\20\3\2\2\2\65\66\7=\2\2\66\22\3\2\2\2\678\7.\2\2")
        buf.write("8\24\3\2\2\29:\7k\2\2:;\7p\2\2;<\7v\2\2<\26\3\2\2\2=>")
        buf.write("\7h\2\2>?\7n\2\2?@\7q\2\2@A\7c\2\2AB\7v\2\2B\30\3\2\2")
        buf.write("\2CE\t\2\2\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3\2\2\2G")
        buf.write("\32\3\2\2\2HI\t\3\2\2IJ\3\2\2\2JK\b\16\2\2K\34\3\2\2\2")
        buf.write("LM\13\2\2\2MN\b\17\3\2N\36\3\2\2\2\4\2F\4\b\2\2\3\17\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    SM = 8
    CM = 9
    INT = 10
    FLOAT = 11
    ID = 12
    WS = 13
    ERROR_CHAR = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'='", "'return'", "'expr'", "';'", 
            "','", "'int'", "'float'" ]

    symbolicNames = [ "<INVALID>",
            "SM", "CM", "INT", "FLOAT", "ID", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "SM", "CM", "INT", "FLOAT", "ID", "WS", "ERROR_CHAR" ]

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
            actions[13] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


