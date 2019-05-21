import sys
from collections import deque

from JFKListener import JFKListener
from JFKParser import JFKParser
from LLVMGenerator import LLVMGenerator
from llvm_types import *
from utils import Value, VarType
from llvmlite import ir
import llvmlite.binding as llvm

voidptr_ty = ir.IntType(8).as_pointer()
printf_ty = ir.FunctionType(ir.IntType(32), [voidptr_ty], var_arg=True)


def to_c_str(val: str):
    return ir.Constant(ir.ArrayType(ir.IntType(8), len(val)), bytearray(val.encode("utf8")))


class CodeGenerator(JFKListener):
    def __init__(self, name):
        self.module = ir.Module(name)
        main_func_type = ir.FunctionType(int32, [])
        main_func = ir.Function(self.module, main_func_type, "main")
        main_block = main_func.append_basic_block(name='.body')
        self.main_builder = ir.IRBuilder(main_block)

        self.stack = deque()

    def exitOutput(self, ctx: JFKParser.OutputContext):
        value = self.stack.pop()

        if not value.is_id:
            self.output_value(value)

    def exitProgram(self, ctx: JFKParser.ProgramContext):
        self.main_builder.ret(int32(0))
        self.module.triple = llvm.get_default_triple()
        print(self.module)

    def exitString(self, ctx: JFKParser.StringContext):
        self.stack.append(
            Value(ctx.STRING().getText(), VarType.STRING, False)
        )

    def output_value(self, value: Value):
        fmt = f"{value.name[1:-1]}\0"
        c_fmt = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt)),
                            bytearray(fmt.encode("utf8")))
        global_fmt = ir.GlobalVariable(self.module, c_fmt.type, name="fstr")
        global_fmt.linkage = 'internal'
        global_fmt.global_constant = True

        global_fmt.initializer = c_fmt
        fmt_arg = self.main_builder.bitcast(global_fmt, voidptr_ty)
        printf = ir.Function(self.module, printf_ty, name="printf")
        self.main_builder.call(printf, [fmt_arg])
