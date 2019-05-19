# Generated from JFK.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("O\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\3\5\3\26\n\3\3\3\5\3\31")
        buf.write("\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\5\4)\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5@\n")
        buf.write("\5\3\6\3\6\7\6D\n\6\f\6\16\6G\13\6\3\7\3\7\3\7\3\7\5\7")
        buf.write("M\n\7\3\7\2\2\b\2\4\6\b\n\f\2\3\3\2\23\23\2V\2\21\3\2")
        buf.write("\2\2\4\25\3\2\2\2\6(\3\2\2\2\b?\3\2\2\2\nA\3\2\2\2\fL")
        buf.write("\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\23\3\2\2\2\21")
        buf.write("\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\21\3\2\2\2\24")
        buf.write("\26\5\6\4\2\25\24\3\2\2\2\25\26\3\2\2\2\26\30\3\2\2\2")
        buf.write("\27\31\5\n\6\2\30\27\3\2\2\2\30\31\3\2\2\2\31\32\3\2\2")
        buf.write("\2\32\33\7\23\2\2\33\5\3\2\2\2\34\35\7\20\2\2\35\36\7")
        buf.write("\3\2\2\36\37\7\b\2\2\37)\7\4\2\2 !\7\t\2\2!\"\7\5\2\2")
        buf.write("\"#\5\b\5\2#$\7\6\2\2$)\3\2\2\2%&\7\20\2\2&\'\7\3\2\2")
        buf.write("\')\5\b\5\2(\34\3\2\2\2( \3\2\2\2(%\3\2\2\2)\7\3\2\2\2")
        buf.write("*+\5\f\7\2+,\7\n\2\2,-\5\b\5\2-@\3\2\2\2./\5\f\7\2/\60")
        buf.write("\7\13\2\2\60\61\5\b\5\2\61@\3\2\2\2\62\63\5\f\7\2\63\64")
        buf.write("\7\f\2\2\64\65\5\b\5\2\65@\3\2\2\2\66\67\5\f\7\2\678\7")
        buf.write("\r\2\289\5\b\5\29@\3\2\2\2:;\5\f\7\2;<\7\16\2\2<=\5\b")
        buf.write("\5\2=@\3\2\2\2>@\5\f\7\2?*\3\2\2\2?.\3\2\2\2?\62\3\2\2")
        buf.write("\2?\66\3\2\2\2?:\3\2\2\2?>\3\2\2\2@\t\3\2\2\2AE\7\7\2")
        buf.write("\2BD\n\2\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2\2F")
        buf.write("\13\3\2\2\2GE\3\2\2\2HM\7\20\2\2IM\7\22\2\2JM\7\21\2\2")
        buf.write("KM\7\17\2\2LH\3\2\2\2LI\3\2\2\2LJ\3\2\2\2LK\3\2\2\2M\r")
        buf.write("\3\2\2\2\t\21\25\30(?EL")
        return buf.getvalue()


class JFKParser ( Parser ):

    grammarFileName = "JFK.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'()'", "'('", "')'", "'#'", "'input'", 
                     "'output'", "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INPUT", "OUTPUT", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "STRING", "ID", "FLOAT", 
                      "INT", "NEWLINE", "WS" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_expression = 3
    RULE_comment = 4
    RULE_value = 5

    ruleNames =  [ "program", "line", "statement", "expression", "comment", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    INPUT=6
    OUTPUT=7
    ADD=8
    SUB=9
    MUL=10
    DIV=11
    MOD=12
    STRING=13
    ID=14
    FLOAT=15
    INT=16
    NEWLINE=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(JFKParser.LineContext)
            else:
                return self.getTypedRuleContext(JFKParser.LineContext,i)


        def getRuleIndex(self):
            return JFKParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = JFKParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKParser.T__4) | (1 << JFKParser.OUTPUT) | (1 << JFKParser.ID) | (1 << JFKParser.NEWLINE))) != 0):
                self.state = 12
                self.line()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(JFKParser.NEWLINE, 0)

        def statement(self):
            return self.getTypedRuleContext(JFKParser.StatementContext,0)


        def comment(self):
            return self.getTypedRuleContext(JFKParser.CommentContext,0)


        def getRuleIndex(self):
            return JFKParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = JFKParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JFKParser.OUTPUT or _la==JFKParser.ID:
                self.state = 18
                self.statement()


            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==JFKParser.T__4:
                self.state = 21
                self.comment()


            self.state = 24
            self.match(JFKParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class OutputContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def OUTPUT(self):
            return self.getToken(JFKParser.OUTPUT, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOutput" ):
                listener.enterOutput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOutput" ):
                listener.exitOutput(self)


    class InputContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKParser.ID, 0)
        def INPUT(self):
            return self.getToken(JFKParser.INPUT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInput" ):
                listener.enterInput(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInput" ):
                listener.exitInput(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def statement(self):

        localctx = JFKParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 38
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = JFKParser.InputContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(JFKParser.ID)
                self.state = 27
                self.match(JFKParser.T__0)
                self.state = 28
                self.match(JFKParser.INPUT)
                self.state = 29
                self.match(JFKParser.T__1)
                pass

            elif la_ == 2:
                localctx = JFKParser.OutputContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(JFKParser.OUTPUT)
                self.state = 31
                self.match(JFKParser.T__2)
                self.state = 32
                self.expression()
                self.state = 33
                self.match(JFKParser.T__3)
                pass

            elif la_ == 3:
                localctx = JFKParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 35
                self.match(JFKParser.ID)
                self.state = 36
                self.match(JFKParser.T__0)
                self.state = 37
                self.expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)

        def ADD(self):
            return self.getToken(JFKParser.ADD, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)


    class DivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)

        def DIV(self):
            return self.getToken(JFKParser.DIV, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class SingleContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle" ):
                listener.enterSingle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle" ):
                listener.exitSingle(self)


    class SubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)

        def SUB(self):
            return self.getToken(JFKParser.SUB, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)


    class ModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)

        def MOD(self):
            return self.getToken(JFKParser.MOD, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)


    class MulContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(JFKParser.ValueContext,0)

        def MUL(self):
            return self.getToken(JFKParser.MUL, 0)
        def expression(self):
            return self.getTypedRuleContext(JFKParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)



    def expression(self):

        localctx = JFKParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = JFKParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.value()
                self.state = 41
                self.match(JFKParser.ADD)
                self.state = 42
                self.expression()
                pass

            elif la_ == 2:
                localctx = JFKParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.value()
                self.state = 45
                self.match(JFKParser.SUB)
                self.state = 46
                self.expression()
                pass

            elif la_ == 3:
                localctx = JFKParser.MulContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.value()
                self.state = 49
                self.match(JFKParser.MUL)
                self.state = 50
                self.expression()
                pass

            elif la_ == 4:
                localctx = JFKParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.value()
                self.state = 53
                self.match(JFKParser.DIV)
                self.state = 54
                self.expression()
                pass

            elif la_ == 5:
                localctx = JFKParser.ModContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.value()
                self.state = 57
                self.match(JFKParser.MOD)
                self.state = 58
                self.expression()
                pass

            elif la_ == 6:
                localctx = JFKParser.SingleContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 60
                self.value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(JFKParser.NEWLINE)
            else:
                return self.getToken(JFKParser.NEWLINE, i)

        def getRuleIndex(self):
            return JFKParser.RULE_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComment" ):
                listener.enterComment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComment" ):
                listener.exitComment(self)




    def comment(self):

        localctx = JFKParser.CommentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(JFKParser.T__4)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << JFKParser.T__0) | (1 << JFKParser.T__1) | (1 << JFKParser.T__2) | (1 << JFKParser.T__3) | (1 << JFKParser.T__4) | (1 << JFKParser.INPUT) | (1 << JFKParser.OUTPUT) | (1 << JFKParser.ADD) | (1 << JFKParser.SUB) | (1 << JFKParser.MUL) | (1 << JFKParser.DIV) | (1 << JFKParser.MOD) | (1 << JFKParser.STRING) | (1 << JFKParser.ID) | (1 << JFKParser.FLOAT) | (1 << JFKParser.INT) | (1 << JFKParser.WS))) != 0):
                self.state = 64
                _la = self._input.LA(1)
                if _la <= 0 or _la==JFKParser.NEWLINE:
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return JFKParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(JFKParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class IdContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(JFKParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class FloatContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(JFKParser.FLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat" ):
                listener.enterFloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat" ):
                listener.exitFloat(self)


    class IntContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a JFKParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(JFKParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def value(self):

        localctx = JFKParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_value)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [JFKParser.ID]:
                localctx = JFKParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(JFKParser.ID)
                pass
            elif token in [JFKParser.INT]:
                localctx = JFKParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(JFKParser.INT)
                pass
            elif token in [JFKParser.FLOAT]:
                localctx = JFKParser.FloatContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(JFKParser.FLOAT)
                pass
            elif token in [JFKParser.STRING]:
                localctx = JFKParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(JFKParser.STRING)
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





