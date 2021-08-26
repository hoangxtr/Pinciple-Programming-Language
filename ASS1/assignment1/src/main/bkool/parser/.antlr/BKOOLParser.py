# Generated from /home/hoang_pc/Desktop/PPL/ASS1/assignment1/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\33\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\5\4\22\n\4\3\5\3\5\3\5\5\5\27\n\5\3\5\3\5\3")
        buf.write("\5\2\2\6\2\4\6\b\2\3\3\2\5\6\2\30\2\n\3\2\2\2\4\f\3\2")
        buf.write("\2\2\6\21\3\2\2\2\b\23\3\2\2\2\n\13\t\2\2\2\13\3\3\2\2")
        buf.write("\2\f\r\5\b\5\2\r\16\7\r\2\2\16\5\3\2\2\2\17\22\5\b\5\2")
        buf.write("\20\22\7\b\2\2\21\17\3\2\2\2\21\20\3\2\2\2\22\7\3\2\2")
        buf.write("\2\23\24\7\7\2\2\24\26\7\t\2\2\25\27\5\6\4\2\26\25\3\2")
        buf.write("\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30\31\7\n\2\2\31\t\3")
        buf.write("\2\2\2\4\21\26")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'int'", "'void'", 
                     "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "';'" ]

    symbolicNames = [ "<INVALID>", "COMMENT_BLOCK", "COMMENT_LINE", "INTTYPE", 
                      "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
                      "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_mptype = 0
    RULE_body = 1
    RULE_exp = 2
    RULE_funcall = 3

    ruleNames =  [ "mptype", "body", "exp", "funcall" ]

    EOF = Token.EOF
    COMMENT_BLOCK=1
    COMMENT_LINE=2
    INTTYPE=3
    VOIDTYPE=4
    ID=5
    INTLIT=6
    LB=7
    RB=8
    LP=9
    RP=10
    SEMI=11
    WS=12
    ERROR_CHAR=13
    UNCLOSE_STRING=14
    ILLEGAL_ESCAPE=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTTYPE(self):
            return self.getToken(BKOOLParser.INTTYPE, 0)

        def VOIDTYPE(self):
            return self.getToken(BKOOLParser.VOIDTYPE, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mptype




    def mptype(self):

        localctx = BKOOLParser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mptype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INTTYPE or _la==BKOOLParser.VOIDTYPE):
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


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(BKOOLParser.FuncallContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.funcall()
            self.state = 11
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(BKOOLParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.funcall()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(BKOOLParser.INTLIT)
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


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcall




    def funcall(self):

        localctx = BKOOLParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(BKOOLParser.ID)
            self.state = 18
            self.match(BKOOLParser.LB)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID or _la==BKOOLParser.INTLIT:
                self.state = 19
                self.exp()


            self.state = 22
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





