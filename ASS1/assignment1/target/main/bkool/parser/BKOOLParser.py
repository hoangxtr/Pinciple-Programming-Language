# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3,")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\7\5\36\n\5\f\5\16\5!\13\5\3\5\3\5\3\5\7\5&\n\5")
        buf.write("\f\5\16\5)\13\5\3\5\3\5\3\5\7\5.\n\5\f\5\16\5\61\13\5")
        buf.write("\3\5\3\5\3\5\7\5\66\n\5\f\5\16\59\13\5\5\5;\n\5\3\5\2")
        buf.write("\2\6\2\4\6\b\2\2\2@\2\13\3\2\2\2\4\17\3\2\2\2\6\26\3\2")
        buf.write("\2\2\b:\3\2\2\2\n\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r")
        buf.write("\13\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\20\7\3\2\2\20")
        buf.write("\21\7\13\2\2\21\22\7\16\2\2\22\23\7\4\2\2\23\24\7\13\2")
        buf.write("\2\24\25\7\17\2\2\25\5\3\2\2\2\26\27\7\16\2\2\27\30\5")
        buf.write("\b\5\2\30\31\7\17\2\2\31\7\3\2\2\2\32\37\7\7\2\2\33\34")
        buf.write("\7\25\2\2\34\36\7\7\2\2\35\33\3\2\2\2\36!\3\2\2\2\37\35")
        buf.write("\3\2\2\2\37 \3\2\2\2 ;\3\2\2\2!\37\3\2\2\2\"\'\7\b\2\2")
        buf.write("#$\7\25\2\2$&\7\b\2\2%#\3\2\2\2&)\3\2\2\2\'%\3\2\2\2\'")
        buf.write("(\3\2\2\2(;\3\2\2\2)\'\3\2\2\2*/\7\n\2\2+,\7\25\2\2,.")
        buf.write("\7\n\2\2-+\3\2\2\2.\61\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60")
        buf.write(";\3\2\2\2\61/\3\2\2\2\62\67\7\t\2\2\63\64\7\25\2\2\64")
        buf.write("\66\7\t\2\2\65\63\3\2\2\2\669\3\2\2\2\67\65\3\2\2\2\67")
        buf.write("8\3\2\2\28;\3\2\2\29\67\3\2\2\2:\32\3\2\2\2:\"\3\2\2\2")
        buf.write(":*\3\2\2\2:\62\3\2\2\2;\t\3\2\2\2\b\r\37\'/\67:")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'extends'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "':'", "'.'", "','", "'\"'", "<INVALID>", "<INVALID>", 
                     "'+'", "'-'", "'*'", "'/'", "'\\'", "'%'", "'!='", 
                     "'=='", "'<'", "'>'", "'<='", "'>='", "'||'", "'&&'", 
                     "'!'", "'^'", "'new'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "COMMENT_BLOCK", 
                      "COMMENT_LINE", "INTLIT", "FLOATLIT", "BOOLEANLIT", 
                      "STRINGLIT", "ID", "LB", "RB", "LP", "RP", "LSB", 
                      "RSB", "SEMI", "COLON", "DOT", "COMMA", "DB", "REMAIN_KEYWORD", 
                      "WS", "ADD_OP", "SUB_OP", "MUL_OP", "FLOAT_DIV_OP", 
                      "INT_DIV_OP", "MOD_OP", "NOT_EQUAL_OP", "EQUAL_OP", 
                      "LT_OP", "GT_OP", "LE_OP", "GE_OP", "OR_OP", "AND_OP", 
                      "NOT_OP", "CONCAT_OP", "NEW", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_class_dec = 1
    RULE_array_lit = 2
    RULE_array_lit_element = 3

    ruleNames =  [ "program", "class_dec", "array_lit", "array_lit_element" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    COMMENT_BLOCK=3
    COMMENT_LINE=4
    INTLIT=5
    FLOATLIT=6
    BOOLEANLIT=7
    STRINGLIT=8
    ID=9
    LB=10
    RB=11
    LP=12
    RP=13
    LSB=14
    RSB=15
    SEMI=16
    COLON=17
    DOT=18
    COMMA=19
    DB=20
    REMAIN_KEYWORD=21
    WS=22
    ADD_OP=23
    SUB_OP=24
    MUL_OP=25
    FLOAT_DIV_OP=26
    INT_DIV_OP=27
    MOD_OP=28
    NOT_EQUAL_OP=29
    EQUAL_OP=30
    LT_OP=31
    GT_OP=32
    LE_OP=33
    GE_OP=34
    OR_OP=35
    AND_OP=36
    NOT_OP=37
    CONCAT_OP=38
    NEW=39
    ERROR_CHAR=40
    UNCLOSE_STRING=41
    ILLEGAL_ESCAPE=42

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_dec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Class_decContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Class_decContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.class_dec()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.T__0):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_decContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_class_dec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_dec" ):
                return visitor.visitClass_dec(self)
            else:
                return visitor.visitChildren(self)




    def class_dec(self):

        localctx = BKOOLParser.Class_decContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_dec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self.match(BKOOLParser.T__0)
            self.state = 14
            self.match(BKOOLParser.ID)
            self.state = 15
            self.match(BKOOLParser.LP)

            self.state = 16
            self.match(BKOOLParser.T__1)
            self.state = 17
            self.match(BKOOLParser.ID)
            self.state = 18
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(BKOOLParser.LP, 0)

        def array_lit_element(self):
            return self.getTypedRuleContext(BKOOLParser.Array_lit_elementContext,0)


        def RP(self):
            return self.getToken(BKOOLParser.RP, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = BKOOLParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(BKOOLParser.LP)
            self.state = 21
            self.array_lit_element()
            self.state = 22
            self.match(BKOOLParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_lit_elementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.INTLIT)
            else:
                return self.getToken(BKOOLParser.INTLIT, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COMMA)
            else:
                return self.getToken(BKOOLParser.COMMA, i)

        def FLOATLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.FLOATLIT)
            else:
                return self.getToken(BKOOLParser.FLOATLIT, i)

        def STRINGLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.STRINGLIT)
            else:
                return self.getToken(BKOOLParser.STRINGLIT, i)

        def BOOLEANLIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.BOOLEANLIT)
            else:
                return self.getToken(BKOOLParser.BOOLEANLIT, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_array_lit_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit_element" ):
                return visitor.visitArray_lit_element(self)
            else:
                return visitor.visitChildren(self)




    def array_lit_element(self):

        localctx = BKOOLParser.Array_lit_elementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_array_lit_element)
        self._la = 0 # Token type
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(BKOOLParser.INTLIT)
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 25
                    self.match(BKOOLParser.COMMA)
                    self.state = 26
                    self.match(BKOOLParser.INTLIT)
                    self.state = 31
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKOOLParser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32
                self.match(BKOOLParser.FLOATLIT)
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 33
                    self.match(BKOOLParser.COMMA)
                    self.state = 34
                    self.match(BKOOLParser.FLOATLIT)
                    self.state = 39
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKOOLParser.STRINGLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.match(BKOOLParser.STRINGLIT)
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 41
                    self.match(BKOOLParser.COMMA)
                    self.state = 42
                    self.match(BKOOLParser.STRINGLIT)
                    self.state = 47
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BKOOLParser.BOOLEANLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.match(BKOOLParser.BOOLEANLIT)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.COMMA:
                    self.state = 49
                    self.match(BKOOLParser.COMMA)
                    self.state = 50
                    self.match(BKOOLParser.BOOLEANLIT)
                    self.state = 55
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





