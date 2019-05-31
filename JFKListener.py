# Generated from JFK.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .JFKParser import JFKParser
else:
    from JFKParser import JFKParser

# This class defines a complete listener for a parse tree produced by JFKParser.
class JFKListener(ParseTreeListener):

    # Enter a parse tree produced by JFKParser#program.
    def enterProgram(self, ctx:JFKParser.ProgramContext):
        pass

    # Exit a parse tree produced by JFKParser#program.
    def exitProgram(self, ctx:JFKParser.ProgramContext):
        pass


    # Enter a parse tree produced by JFKParser#func.
    def enterFunc(self, ctx:JFKParser.FuncContext):
        pass

    # Exit a parse tree produced by JFKParser#func.
    def exitFunc(self, ctx:JFKParser.FuncContext):
        pass


    # Enter a parse tree produced by JFKParser#params.
    def enterParams(self, ctx:JFKParser.ParamsContext):
        pass

    # Exit a parse tree produced by JFKParser#params.
    def exitParams(self, ctx:JFKParser.ParamsContext):
        pass


    # Enter a parse tree produced by JFKParser#block.
    def enterBlock(self, ctx:JFKParser.BlockContext):
        pass

    # Exit a parse tree produced by JFKParser#block.
    def exitBlock(self, ctx:JFKParser.BlockContext):
        pass


    # Enter a parse tree produced by JFKParser#ifblock.
    def enterIfblock(self, ctx:JFKParser.IfblockContext):
        pass

    # Exit a parse tree produced by JFKParser#ifblock.
    def exitIfblock(self, ctx:JFKParser.IfblockContext):
        pass


    # Enter a parse tree produced by JFKParser#elseblock.
    def enterElseblock(self, ctx:JFKParser.ElseblockContext):
        pass

    # Exit a parse tree produced by JFKParser#elseblock.
    def exitElseblock(self, ctx:JFKParser.ElseblockContext):
        pass


    # Enter a parse tree produced by JFKParser#line.
    def enterLine(self, ctx:JFKParser.LineContext):
        pass

    # Exit a parse tree produced by JFKParser#line.
    def exitLine(self, ctx:JFKParser.LineContext):
        pass


    # Enter a parse tree produced by JFKParser#output.
    def enterOutput(self, ctx:JFKParser.OutputContext):
        pass

    # Exit a parse tree produced by JFKParser#output.
    def exitOutput(self, ctx:JFKParser.OutputContext):
        pass


    # Enter a parse tree produced by JFKParser#assign.
    def enterAssign(self, ctx:JFKParser.AssignContext):
        pass

    # Exit a parse tree produced by JFKParser#assign.
    def exitAssign(self, ctx:JFKParser.AssignContext):
        pass


    # Enter a parse tree produced by JFKParser#ifStmt.
    def enterIfStmt(self, ctx:JFKParser.IfStmtContext):
        pass

    # Exit a parse tree produced by JFKParser#ifStmt.
    def exitIfStmt(self, ctx:JFKParser.IfStmtContext):
        pass


    # Enter a parse tree produced by JFKParser#single.
    def enterSingle(self, ctx:JFKParser.SingleContext):
        pass

    # Exit a parse tree produced by JFKParser#single.
    def exitSingle(self, ctx:JFKParser.SingleContext):
        pass


    # Enter a parse tree produced by JFKParser#add.
    def enterAdd(self, ctx:JFKParser.AddContext):
        pass

    # Exit a parse tree produced by JFKParser#add.
    def exitAdd(self, ctx:JFKParser.AddContext):
        pass


    # Enter a parse tree produced by JFKParser#div.
    def enterDiv(self, ctx:JFKParser.DivContext):
        pass

    # Exit a parse tree produced by JFKParser#div.
    def exitDiv(self, ctx:JFKParser.DivContext):
        pass


    # Enter a parse tree produced by JFKParser#equal.
    def enterEqual(self, ctx:JFKParser.EqualContext):
        pass

    # Exit a parse tree produced by JFKParser#equal.
    def exitEqual(self, ctx:JFKParser.EqualContext):
        pass


    # Enter a parse tree produced by JFKParser#sub.
    def enterSub(self, ctx:JFKParser.SubContext):
        pass

    # Exit a parse tree produced by JFKParser#sub.
    def exitSub(self, ctx:JFKParser.SubContext):
        pass


    # Enter a parse tree produced by JFKParser#greaterThanEqual.
    def enterGreaterThanEqual(self, ctx:JFKParser.GreaterThanEqualContext):
        pass

    # Exit a parse tree produced by JFKParser#greaterThanEqual.
    def exitGreaterThanEqual(self, ctx:JFKParser.GreaterThanEqualContext):
        pass


    # Enter a parse tree produced by JFKParser#lessThanEqual.
    def enterLessThanEqual(self, ctx:JFKParser.LessThanEqualContext):
        pass

    # Exit a parse tree produced by JFKParser#lessThanEqual.
    def exitLessThanEqual(self, ctx:JFKParser.LessThanEqualContext):
        pass


    # Enter a parse tree produced by JFKParser#mod.
    def enterMod(self, ctx:JFKParser.ModContext):
        pass

    # Exit a parse tree produced by JFKParser#mod.
    def exitMod(self, ctx:JFKParser.ModContext):
        pass


    # Enter a parse tree produced by JFKParser#mul.
    def enterMul(self, ctx:JFKParser.MulContext):
        pass

    # Exit a parse tree produced by JFKParser#mul.
    def exitMul(self, ctx:JFKParser.MulContext):
        pass


    # Enter a parse tree produced by JFKParser#lessThan.
    def enterLessThan(self, ctx:JFKParser.LessThanContext):
        pass

    # Exit a parse tree produced by JFKParser#lessThan.
    def exitLessThan(self, ctx:JFKParser.LessThanContext):
        pass


    # Enter a parse tree produced by JFKParser#notEqual.
    def enterNotEqual(self, ctx:JFKParser.NotEqualContext):
        pass

    # Exit a parse tree produced by JFKParser#notEqual.
    def exitNotEqual(self, ctx:JFKParser.NotEqualContext):
        pass


    # Enter a parse tree produced by JFKParser#greaterThan.
    def enterGreaterThan(self, ctx:JFKParser.GreaterThanContext):
        pass

    # Exit a parse tree produced by JFKParser#greaterThan.
    def exitGreaterThan(self, ctx:JFKParser.GreaterThanContext):
        pass


    # Enter a parse tree produced by JFKParser#comment.
    def enterComment(self, ctx:JFKParser.CommentContext):
        pass

    # Exit a parse tree produced by JFKParser#comment.
    def exitComment(self, ctx:JFKParser.CommentContext):
        pass


    # Enter a parse tree produced by JFKParser#id.
    def enterId(self, ctx:JFKParser.IdContext):
        pass

    # Exit a parse tree produced by JFKParser#id.
    def exitId(self, ctx:JFKParser.IdContext):
        pass


    # Enter a parse tree produced by JFKParser#int.
    def enterInt(self, ctx:JFKParser.IntContext):
        pass

    # Exit a parse tree produced by JFKParser#int.
    def exitInt(self, ctx:JFKParser.IntContext):
        pass


    # Enter a parse tree produced by JFKParser#float.
    def enterFloat(self, ctx:JFKParser.FloatContext):
        pass

    # Exit a parse tree produced by JFKParser#float.
    def exitFloat(self, ctx:JFKParser.FloatContext):
        pass


    # Enter a parse tree produced by JFKParser#string.
    def enterString(self, ctx:JFKParser.StringContext):
        pass

    # Exit a parse tree produced by JFKParser#string.
    def exitString(self, ctx:JFKParser.StringContext):
        pass


    # Enter a parse tree produced by JFKParser#input.
    def enterInput(self, ctx:JFKParser.InputContext):
        pass

    # Exit a parse tree produced by JFKParser#input.
    def exitInput(self, ctx:JFKParser.InputContext):
        pass


    # Enter a parse tree produced by JFKParser#true.
    def enterTrue(self, ctx:JFKParser.TrueContext):
        pass

    # Exit a parse tree produced by JFKParser#true.
    def exitTrue(self, ctx:JFKParser.TrueContext):
        pass


    # Enter a parse tree produced by JFKParser#false.
    def enterFalse(self, ctx:JFKParser.FalseContext):
        pass

    # Exit a parse tree produced by JFKParser#false.
    def exitFalse(self, ctx:JFKParser.FalseContext):
        pass


