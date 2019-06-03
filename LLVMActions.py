import sys
from collections import deque
from copy import copy

from JFKListener import JFKListener
from JFKParser import JFKParser
from LLVMGenerator import LLVMGenerator
from utils import Value, VarType, Param


class LLVMActions(JFKListener):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generator = LLVMGenerator()
        self.stack = deque()
        self.variables = dict()
        self.will_have_else = deque()
        self.has_return = (False, None)
        self.function_variables = {}
        self.in_function = False
        self.functions = {}
        self.in_loop = False

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
        self.generator.close_main()
        print(self.generator.generate())

    def exitInt(self, ctx: JFKParser.IntContext):
        self.stack.append(Value(ctx.INT().getText(), VarType.INT, False))

    def exitFloat(self, ctx: JFKParser.FloatContext):
        self.stack.append(Value(ctx.FLOAT().getText(), VarType.FLOAT, False))

    def exitId(self, ctx: JFKParser.IdContext):
        _id = ctx.ID().getText()
        try:
            if self.in_function:
                var_type = self.function_variables[_id]
            else:
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
        
        current_variables = copy(self.variables) if not self.in_function else copy(self.function_variables)
        
        if value.is_id:
            if value.type == VarType.INT:
                if ID not in current_variables:
                    self.generator.declare_i32(ID)
                self.generator.assign_id_i32(ID, value.name)
            elif value.type == VarType.FLOAT:
                if ID not in current_variables:
                    self.generator.declare_double(ID)
                self.generator.assign_id_double(ID, value.name)
            elif value.type == VarType.STRING:
                self.generator.assign_id_string(ID, value.name)
            elif value.type == VarType.BOOL:
                if ID not in current_variables:
                    self.generator.declare_bool(ID)
                self.generator.assign_id_bool(ID, value.name)
        else:
            if value.type == VarType.INT:
                if ID not in current_variables:
                    self.generator.declare_i32(ID)
                self.generator.assign_i32(ID, value.name)
            elif value.type == VarType.FLOAT:
                if ID not in current_variables:
                    self.generator.declare_double(ID)
                self.generator.assign_double(ID, value.name)
            elif value.type == VarType.STRING:
                self.generator.assign_string(ID, value.name[1:-1])
            elif value.type == VarType.BOOL:
                if ID not in current_variables:
                    self.generator.declare_bool(ID)
                self.generator.assign_bool(ID, value.name)

        if self.in_function:
            self.function_variables[ID] = value.type
        else:
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

    def enterWhile(self, ctx: JFKParser.WhileContext):
        self.generator.start_while()
        self.in_loop = True

    def enterLoopblock(self, ctx: JFKParser.LoopblockContext):
        condition = self.stack.pop()
        self.generator.start_while_block(condition.name, condition.is_id)

    def exitLoopblock(self, ctx: JFKParser.LoopblockContext):
        self.generator.back_to_while()

    def exitWhile(self, ctx: JFKParser.WhileContext):
        self.generator.end_while()
        self.in_loop = False

    def enterFunc(self, ctx: JFKParser.FuncContext):
        name = ctx.ID().getText()
        params = [Param(p.ID().getText(), p.TYPE_KEYWORD().getText()) for p in ctx.params().param()]
        return_type = ctx.TYPE_KEYWORD().getText()
        if name in self.functions:
            self.error(ctx.start.line, f"Function '{name}' already defined")
        else:
            self.functions[name] = [VarType(p.type) for p in params], return_type

        self.function_variables = {p.name: VarType(p.type) for p in params}

        self.has_return = (False, return_type)
        self.in_function = True
        self.generator.start_func(name, params, return_type)

    def exitReturn(self, ctx: JFKParser.ReturnContext):
        return_value = self.stack.pop()
        if return_value.type.value != self.has_return[1]:
            self.error(ctx.start.line, f"Expected return type {self.has_return[1]} but got {return_value.type.value}")
        else:
            self.generator.return_func(*return_value)

        self.has_return = (True, self.has_return[1])

    def exitFunc(self, ctx: JFKParser.FuncContext):
        self.generator.exit_func(ctx.TYPE_KEYWORD().getText(), self.has_return[0])
        self.in_function = False

    def exitFuncCall(self, ctx: JFKParser.FuncCallContext):
        fname = ctx.ID().getText()
        try:
            fparams, return_type = self.functions[fname]
            given_args = list(reversed([self.stack.pop() for i in range(len(ctx.args().expression()))]))
            given_args_types = [arg.type for arg in given_args]

            if not (len(fparams) == len(given_args) and fparams == given_args_types):
                self.error(ctx.start.line, f"Arguments do not match function definition. \n"
                                           f"Expected: {[p.value for p in fparams]}, "
                                           f"given: {[a.value for a in given_args_types]}")
            self.generator.func_call(fname, given_args, return_type)
            self.stack.append(Value("%" + str(self.generator.str_i - 1), VarType(return_type), False))
        except KeyError:
            self.error(ctx.start.line, f"Unresolved function name '{fname}'")

    def exitBreak(self, ctx: JFKParser.BreakContext):
        if self.in_loop:
            self.generator.break_loop()
        else:
            self.error(ctx.start.line, f"Cannot use {ctx.BREAK().getText()} keyword outside of loop")

    def exitContinue(self, ctx: JFKParser.ContinueContext):
        if self.in_loop:
            self.generator.continue_loop()
        else:
            self.error(ctx.start.line, f"Cannot use {ctx.CONTINUE().getText()} keyword outside of loop")

    def exitExit(self, ctx: JFKParser.ExitContext):
        if not self.in_function:
            self.generator.exit()
        else:
            self.error(ctx.start.line, "Cannot exit program while in function")
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
