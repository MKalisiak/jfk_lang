class LLVMGenerator:
    header_text = ""
    main_text = ""
    str_i = 0

    def output(self, text):
        str_len = len(text)
        str_type = "[" + str(str_len + 2) + " x i8]"
        self.header_text += "@str" + str(self.str_i) + " = constant" + str_type + " c\"" + text + "\\0A\\00\"\n"
        self.main_text += ("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ( " + str_type + ", " + str_type +
                           "* @str" + str(self.str_i) + ", i32 0, i32 0))\n")
        self.str_i += 1

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text
