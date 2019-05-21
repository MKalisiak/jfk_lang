from ctypes import CFUNCTYPE, c_int
import sys

import llvmlite.ir as ll
import llvmlite.binding as llvm

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

module = ll.Module()

main_ty = ll.FunctionType(ll.IntType(32), [])
func = ll.Function(module, main_ty, 'main')
block = func.append_basic_block('entry')
builder = ll.IRBuilder(block)

int32 = ll.IntType(32)

c = int32(44)

ptr = builder.alloca(int32, name="a")

builder.store(c, ptr)

str_type = ll.ArrayType(ll.IntType(8), 2)

ptr2 = builder.alloca(str_type, name="xd")

int8 = ll.IntType(8)
d = str_type([int8(65), int8(66)])
builder.store(d, ptr2)

# voidptr_ty = ll.IntType(8).as_pointer()
# printf_ty = ll.FunctionType(ll.IntType(32), [voidptr_ty], var_arg=True)
# printf = ll.Function(module, printf_ty, name="printf")
# builder.call(printf, [ptr])

print(module)
