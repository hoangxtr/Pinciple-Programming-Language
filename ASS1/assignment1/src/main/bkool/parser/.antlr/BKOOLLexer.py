# Generated from /home/hoang_pc/Desktop/PPL/ASS1/assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("Z\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\2\3\2\7\2&\n\2\f\2")
        buf.write("\16\2)\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\6\6;\n\6\r\6\16\6<\3\7\6\7@\n\7")
        buf.write("\r\7\16\7A\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\6\rO\n\r\r\r\16\rP\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\'\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\37\21\3\2\6\3\2\f\f\4\2C")
        buf.write("\\c|\3\2\62;\5\2\13\f\17\17\"\"\2]\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\3!\3\2\2\2\5-\3\2\2\2\7\60\3\2\2\2\t\64\3\2\2")
        buf.write("\2\13:\3\2\2\2\r?\3\2\2\2\17C\3\2\2\2\21E\3\2\2\2\23G")
        buf.write("\3\2\2\2\25I\3\2\2\2\27K\3\2\2\2\31N\3\2\2\2\33T\3\2\2")
        buf.write("\2\35V\3\2\2\2\37X\3\2\2\2!\"\7\61\2\2\"#\7,\2\2#\'\3")
        buf.write("\2\2\2$&\13\2\2\2%$\3\2\2\2&)\3\2\2\2\'(\3\2\2\2\'%\3")
        buf.write("\2\2\2(*\3\2\2\2)\'\3\2\2\2*+\7,\2\2+,\7\61\2\2,\4\3\2")
        buf.write("\2\2-.\7%\2\2./\n\2\2\2/\6\3\2\2\2\60\61\7k\2\2\61\62")
        buf.write("\7p\2\2\62\63\7v\2\2\63\b\3\2\2\2\64\65\7x\2\2\65\66\7")
        buf.write("q\2\2\66\67\7k\2\2\678\7f\2\28\n\3\2\2\29;\t\3\2\2:9\3")
        buf.write("\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2\2=\f\3\2\2\2>@\t\4")
        buf.write("\2\2?>\3\2\2\2@A\3\2\2\2A?\3\2\2\2AB\3\2\2\2B\16\3\2\2")
        buf.write("\2CD\7*\2\2D\20\3\2\2\2EF\7+\2\2F\22\3\2\2\2GH\7}\2\2")
        buf.write("H\24\3\2\2\2IJ\7\177\2\2J\26\3\2\2\2KL\7=\2\2L\30\3\2")
        buf.write("\2\2MO\t\5\2\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2")
        buf.write("QR\3\2\2\2RS\b\r\2\2S\32\3\2\2\2TU\13\2\2\2U\34\3\2\2")
        buf.write("\2VW\13\2\2\2W\36\3\2\2\2XY\13\2\2\2Y \3\2\2\2\7\2\'<")
        buf.write("AP\3\b\2\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMENT_BLOCK = 1
    COMMENT_LINE = 2
    INTTYPE = 3
    VOIDTYPE = 4
    ID = 5
    INTLIT = 6
    LB = 7
    RB = 8
    LP = 9
    RP = 10
    SEMI = 11
    WS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "COMMENT_BLOCK", "COMMENT_LINE", "INTTYPE", "VOIDTYPE", "ID", 
            "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "COMMENT_BLOCK", "COMMENT_LINE", "INTTYPE", "VOIDTYPE", 
                  "ID", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


