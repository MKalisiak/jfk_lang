import sys
from antlr4 import *

from CodeGenerator import CodeGenerator
from JFKLexer import JFKLexer
from JFKParser import JFKParser
from LLVMActions import LLVMActions


def main(argv):
    file_stream = FileStream(argv[1], encoding='utf-8')
    lexer = JFKLexer(file_stream)
    tokens = CommonTokenStream(lexer)
    parser = JFKParser(tokens)
    tree = parser.program()
    walker = ParseTreeWalker()
    walker.walk(CodeGenerator(__name__), tree)


if __name__ == "__main__":
    main(sys.argv)
