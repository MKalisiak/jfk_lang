import sys
from collections import deque

from JFKListener import JFKListener
from JFKParser import JFKParser
from LLVMGenerator import LLVMGenerator
from utils import Value, VarType


class LLVMActions(JFKListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = LLVMGenerator()
        self.stack = deque()
        self.variables = dict()

    def exitOutput(self, ctx: JFKParser.OutputContext):
        print(self.stack, file=sys.stderr)
        value = self.stack.pop()  # type: Value

        if value.is_id:
            if value.type == VarType.INT:
                self.generator.output_id_i32(value.name)
            if value.type == VarType.FLOAT:
                self.generator.output_id_double(value.name)
            if value.type == VarType.STRING:
                self.generator.output_id_string(value.name)
        else:
            if value.type == VarType.INT:
                self.generator.output_i32(value.name)
            if value.type == VarType.FLOAT:
                self.generator.output_double(value.name)
            if value.type == VarType.STRING:
                self.generator.output_string(value.name[1:-1])

    def exitProgram(self, ctx: JFKParser.ProgramContext):
        print(self.generator.generate())

    def exitInt(self, ctx: JFKParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT, False))

    def exitFloat(self, ctx: JFKParser.FloatContext):
        self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT, False))

    def exitId(self, ctx: JFKParser.IdContext):
        _id = ctx.ID().getText()
        try:
            var_type = self.variables[_id]
            if var_type == VarType.INT:
                self.stack.append(Value(_id, VarType.INT, True))
            elif var_type == VarType.FLOAT:
                self.stack.append(Value(_id, VarType.FLOAT, True))
            elif var_type == VarType.STRING:
                self.stack.append(Value(_id, VarType.STRING, True))
        except KeyError:
            self.error(ctx.start.line, "Unresolved variable " + _id)

    def exitString(self, ctx: JFKParser.StringContext):
        self.stack.append(
            Value(ctx.STRING().getText(), VarType.STRING, False)
        )

    def exitAdd(self, ctx: JFKParser.AddContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

    def exitSub(self, ctx: JFKParser.SubContext):
        ...

    def exitMul(self, ctx: JFKParser.MulContext):
        ...

    def exitDiv(self, ctx: JFKParser.DivContext):
        ...

    def exitMod(self, ctx: JFKParser.ModContext):
        ...

    def exitSingle(self, ctx: JFKParser.SingleContext):
        ...

    def exitAssign(self, ctx: JFKParser.AssignContext):
        ID = ctx.ID().getText()  # type: str
        value = self.stack.pop()  # type: Value
        self.variables[ID] = value.type
        if value.type == VarType.INT:
            self.generator.declare_i32(ID)
            self.generator.assign_i32(ID, value.name)
        elif value.type == VarType.FLOAT:
            self.generator.declare_double(ID)
            self.generator.assign_double(ID, value.name)
        elif value.type == VarType.STRING:
            self.generator.assign_string(ID, value.name[1:-1])

    # def exitAdd(self, ctx: JFKParser.AddContext):
    #     v1 = self.stack.pop()  # type: Value
    #     v2 = self.stack.pop()  # type: Value
    #     if v1.type == v2.type:
    #         if v1.type == VarType.INT:
    #             self.generator.add_i32(v1.name, v2.name)
    #             self.stack.append(Value("%" + str(self.generator.str_i - 1), VarType.INT))
    #         elif v1.type == VarType.FLOAT:
    #             self.generator.add_double(v1.name, v2.name)
    #             self.stack.append(Value("%" + str(self.generator.str_i - 1), VarType.FLOAT))
    #     else:
    #         self.error(ctx.start.line, "add type mismatch")

    def error(self, line: int, msg: str):
        print("Error, line " + str(line) + ", " + msg, file=sys.stderr)
        exit(1)
