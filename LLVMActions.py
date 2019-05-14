from JFKListener import JFKListener
from JFKParser import JFKParser
from LLVMGenerator import LLVMGenerator


class LLVMActions(JFKListener):
    generator = LLVMGenerator()

    def exitOutput(self, ctx:JFKParser.OutputContext):
        if ctx.STRING() is not None:
            tmp = ctx.STRING().getText()
            tmp = tmp[1:-1]
            self.generator.output(tmp)

    def exitProgram(self, ctx:JFKParser.ProgramContext):
        print(self.generator.generate())
