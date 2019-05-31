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
        self.will_have_else = deque()

    def exitOutput(self, ctx: JFKParser.OutputContext):
        value = self.stack.pop()  # type: Value

        if value.is_id:
            if value.type == VarType.INT:
                self.generator.output_id_i32(value.name)
            if value.type == VarType.FLOAT:
                self.generator.output_id_double(value.name)
            if value.type == VarType.STRING:
                self.generator.output_id_string(value.name)
            if value.type == VarType.BOOL:
                self.generator.output_id_bool(value.name)
        else:
            if value.type == VarType.INT:
                self.generator.output_i32(value.name)
            if value.type == VarType.FLOAT:
                self.generator.output_double(value.name)
            if value.type == VarType.STRING:
                self.generator.output_string(value.name[1:-1])
            if value.type == VarType.BOOL:
                self.generator.output_bool(value.name)

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
            elif var_type == VarType.BOOL:
                self.stack.append(Value(_id, VarType.BOOL, True))
        except KeyError:
            self.error(ctx.start.line, "Unresolved variable " + _id)

    def exitString(self, ctx: JFKParser.StringContext):
        self.stack.append(
            Value(ctx.STRING().getText(), VarType.STRING, False)
        )

    def exitAdd(self, ctx: JFKParser.AddContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, "Addition not permitted for type STRING")
        else:
            v1, v2 = self.calc('add', v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), v1.type, False))

    def exitSub(self, ctx: JFKParser.SubContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, "Subtraction not permitted for type STRING")
        else:
            v1, v2 = self.calc('sub', v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), v1.type, False))

    def exitMul(self, ctx: JFKParser.MulContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, "Multiplication not permitted for type STRING")
        else:
            v1, v2 = self.calc('mul', v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), v1.type, False))

    def exitDiv(self, ctx: JFKParser.DivContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, "Division not permitted for type STRING")
        else:
            v1, v2 = self.calc('div', v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), v1.type, False))

    def exitMod(self, ctx: JFKParser.ModContext):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, "Modulo division not permitted for type STRING")
        else:
            v1, v2 = self.calc('mod', v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), v1.type, False))

    def exitSingle(self, ctx: JFKParser.SingleContext):
        ...

    def exitAssign(self, ctx: JFKParser.AssignContext):
        ID = ctx.ID().getText()  # type: str
        value = self.stack.pop()  # type: Value
        if value.is_id:
            if value.type == VarType.INT:
                if ID not in self.variables:
                    self.generator.declare_i32(ID)
                self.generator.assign_id_i32(ID, value.name)
            elif value.type == VarType.FLOAT:
                if ID not in self.variables:
                    self.generator.declare_double(ID)
                self.generator.assign_id_double(ID, value.name)
            elif value.type == VarType.STRING:
                self.generator.assign_id_string(ID, value.name)
            elif value.type == VarType.BOOL:
                if ID not in self.variables:
                    self.generator.declare_bool(ID)
                self.generator.assign_id_bool(ID, value.name)
        else:
            if value.type == VarType.INT:
                if ID not in self.variables:
                    self.generator.declare_i32(ID)
                self.generator.assign_i32(ID, value.name)
            elif value.type == VarType.FLOAT:
                if ID not in self.variables:
                    self.generator.declare_double(ID)
                self.generator.assign_double(ID, value.name)
            elif value.type == VarType.STRING:
                self.generator.assign_string(ID, value.name[1:-1])
            elif value.type == VarType.BOOL:
                if ID not in self.variables:
                    self.generator.declare_bool(ID)
                self.generator.assign_bool(ID, value.name)

        self.variables[ID] = value.type

    def exitInput(self, ctx: JFKParser.InputContext):
        TYPE = ctx.TYPE_KEYWORD().getText()

        if TYPE == VarType.INT.value:
            self.generator.input_i32()
        elif TYPE == VarType.FLOAT.value:
            self.generator.input_double()
        elif TYPE == VarType.STRING.value:
            self.generator.input_string()

        if TYPE == VarType.STRING.value:
            self.stack.append(Value(str(self.generator.str_i - 4), VarType(TYPE), True))
        else:
            self.stack.append(Value("%" + str(self.generator.str_i - 1), VarType(TYPE), False))

    def exitTrue(self, ctx: JFKParser.TrueContext):
        self.stack.append(Value("1", VarType.BOOL, False))

    def exitFalse(self, ctx: JFKParser.FalseContext):
        self.stack.append(Value("0", VarType.BOOL, False))

    def exitEqual(self, ctx: JFKParser.EqualContext):
        self.exitComp('eq', ctx, "Equality comparision not permitted for type STRING")

    def exitNotEqual(self, ctx: JFKParser.NotEqualContext):
        self.exitComp('ne', ctx, "Inequality comparision not permitted for type STRING")

    def exitGreaterThan(self, ctx: JFKParser.GreaterThanContext):
        self.exitComp('gt', ctx, "Comparision not permitted for type STRING")

    def exitGreaterThanEqual(self, ctx: JFKParser.GreaterThanEqualContext):
        self.exitComp('ge', ctx, "Comparision not permitted for type STRING")

    def exitLessThan(self, ctx: JFKParser.LessThanContext):
        self.exitComp('lt', ctx, "Comparision not permitted for type STRING")

    def exitLessThanEqual(self, ctx: JFKParser.LessThanEqualContext):
        self.exitComp('le', ctx, "Comparision not permitted for type STRING")

    def enterIfStmt(self, ctx: JFKParser.IfStmtContext):
        self.will_have_else.append(ctx.ELSE() is not None)

    def enterIfblock(self, ctx: JFKParser.IfblockContext):
        condition = self.stack.pop()
        self.generator.start_if(condition.name, condition.is_id, self.will_have_else[-1])

    def exitIfblock(self, ctx: JFKParser.IfblockContext):
        if not self.will_have_else.pop():
            self.generator.end_if()

    def enterElseblock(self, ctx: JFKParser.ElseblockContext):
        self.generator.start_else()

    def exitElseblock(self, ctx: JFKParser.ElseblockContext):
        self.generator.end_if()

    # =============================================================================

    def error(self, line: int, msg: str):
        print("Error, line " + str(line) + ", " + msg, file=sys.stderr)
        exit(1)

    def unify_types(self, v1, v2):
        if v1.type == VarType.INT:
            if v1.is_id:
                self.generator.i32_to_double_id(v1.name)
                v1 = Value("%" + str(self.generator.str_i - 1), VarType.FLOAT, False)
            else:
                self.generator.i32_to_double(v1.name)
                v1 = Value("%" + str(self.generator.str_i - 1), VarType.FLOAT, False)
        elif v1.type == VarType.FLOAT:
            if v2.is_id:
                self.generator.i32_to_double_id(v2.name)
                v2 = Value("%" + str(self.generator.str_i - 1), VarType.FLOAT, False)
            else:
                self.generator.i32_to_double(v2.name)
                v2 = Value("%" + str(self.generator.str_i - 1), VarType.FLOAT, False)

        return v1, v2

    def calc(self, op_name, v1, v2):
        v1, v2 = v2, v1

        if v1.type != v2.type:
            v1, v2 = self.unify_types(v1, v2)

        if v1.type == VarType.INT:
            if not v1.is_id and not v2.is_id:
                getattr(self.generator, op_name + "_i32")(v1.name, v2.name)
            elif v1.is_id and v2.is_id:
                getattr(self.generator, op_name + "_id_i32")(v1.name, v2.name)
            elif v1.is_id:
                getattr(self.generator, op_name + "_hybrid_i32_id_value")(_id=v1.name, value=v2.name)
            else:
                getattr(self.generator, op_name + "_hybrid_i32_value_id")(_id=v2.name, value=v1.name)

        elif v1.type == VarType.FLOAT:
            if not v1.is_id and not v2.is_id:
                getattr(self.generator, op_name + "_double")(v1.name, v2.name)
            elif v1.is_id and v2.is_id:
                getattr(self.generator, op_name + "_id_double")(v1.name, v2.name)
            elif v1.is_id:
                getattr(self.generator, op_name + "_hybrid_double_id_value")(_id=v1.name, value=v2.name)
            else:
                getattr(self.generator, op_name + "_hybrid_double_value_id")(_id=v2.name, value=v1.name)

        return v1, v2

    def exitComp(self, op_name, ctx, string_error):
        v1 = self.stack.pop()  # type: Value
        v2 = self.stack.pop()  # type: Value

        if v1.type == VarType.STRING or v2.type == VarType.STRING:
            self.error(ctx.start.line, string_error)
        else:
            if v1.type != v2.type and (v1.type == VarType.BOOL or v2.type == VarType.BOOL):
                self.error(ctx.start.line, f"Cannot compare {v1.type} with {v2.type}")
            v1, v2 = self.comp(op_name, v1, v2)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), VarType.BOOL, False))

    def comp(self, op_name, v1, v2):
        v1, v2 = v2, v1

        if v1.type != v2.type:
            v1, v2 = self.unify_types(v1, v2)

        if v1.type == VarType.INT:
            if op_name != "eq" and op_name != "ne":
                op_name = "s" + op_name
            if not v1.is_id and not v2.is_id:
                self.generator.comp_i32(op_name, v1.name, v2.name)
            elif v1.is_id and v2.is_id:
                self.generator.comp_id_i32(op_name, v1.name, v2.name)
            elif v1.is_id:
                self.generator.comp_hybrid_i32_id_value(op_name, _id=v1.name, value=v2.name)
            else:
                self.generator.comp_hybrid_i32_value_id(op_name, _id=v2.name, value=v1.name)

        elif v1.type == VarType.FLOAT:
            op_name = "o" + op_name
            if not v1.is_id and not v2.is_id:
                self.generator.comp_double(op_name, v1.name, v2.name)
            elif v1.is_id and v2.is_id:
                self.generator.comp_id_double(op_name, v1.name, v2.name)
            elif v1.is_id:
                self.generator.comp_hybrid_double_id_value(op_name, _id=v1.name, value=v2.name)
            else:
                self.generator.comp_hybrid_double_value_id(op_name, _id=v2.name, value=v1.name)
        
        elif v1.type == VarType.BOOL:
            if op_name != "eq" and op_name != "ne":
                op_name = "u" + op_name
            if not v1.is_id and not v2.is_id:
                self.generator.comp_i1(op_name, v1.name, v2.name)
            elif v1.is_id and v2.is_id:
                self.generator.comp_id_i1(op_name, v1.name, v2.name)
            elif v1.is_id:
                self.generator.comp_hybrid_i1_id_value(op_name, _id=v1.name, value=v2.name)
            else:
                self.generator.comp_hybrid_i1_value_id(op_name, _id=v2.name, value=v1.name)

        return v1, v2
