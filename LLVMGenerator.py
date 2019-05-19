class LLVMGenerator:
    header_text = ""
    main_text = ""
    str_i = 1
    strings_declared = {}

    def output_string(self, text):
        str_len = len(text)
        str_type = "[" + str(str_len + 2) + " x i8]"
        self.header_text += "@str" + self.reg + " = constant" + str_type + " c\"" + text + "\\0A\\00\"\n"
        self.main_text += ("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ( " + str_type + ", " + str_type +
                           "* @str" + self.reg + ", i32 0, i32 0))\n")
        self.str_i += 1
        
    @property
    def reg(self):
        return str(self.str_i)

    def output_id_i32(self, _id: str):
        self.main_text += "%"+self.reg+" = load i32, i32* %"+_id+"\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %" + str(self.str_i - 1) + ")\n"
        self.str_i += 1
        
    def output_id_double(self, _id: str):
        self.main_text += "%" + self.reg + " = load double, double* %" + _id + "\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double %" + str(self.str_i - 1) + ")\n"
        self.str_i += 1

    def output_id_string(self, _id: str):
        self.main_text += "%" + self.reg + " = load i8*, i8** %" + _id + ", align 8\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i8* %" + str(self.str_i - 1) +")\n"
        self.str_i += 1

    def output_i32(self, value: str):
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 " + value + ")\n"
        self.str_i += 1

    def output_double(self, value: str):
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double " + value + ")\n"
        self.str_i += 1

    def declare_i32(self, _id: str):
        self.main_text += "%"+_id+" = alloca i32\n"

    def declare_double(self, _id: str):
        self.main_text += "%" + _id + " = alloca double\n"

    def assign_i32(self, _id: str, value: str):
        self.main_text += "store i32 " + value + ", i32* %" + _id + "\n"

    def assign_double(self, _id: str, value: str):
        self.main_text += "store double " + value + ", double* %" + _id + "\n"

    def assign_string(self, _id: str, value: str):
        str_len = len(value) + 2
        str_type = "[" + str(str_len) + " x i8]"
        if _id not in self.strings_declared:
            self.strings_declared[_id] = 0

        n = self.strings_declared[_id]
        self.header_text += "@" + _id + "." + str(n) + " = constant" + str_type + " c\"" + value + "\\0A\\00\"\n"

        if self.strings_declared[_id] == 0:
            self.main_text += "%" + _id + " = alloca i8*, align 8\n"

        self.strings_declared[_id] += 1
        self.main_text += "store i8* getelementptr inbounds ([" + str(str_len) + " x i8], [" + str(str_len) + " x i8]* @" + _id + "." + str(n) + ", i32 0, i32 0), i8** %" + _id +", align 8\n"

    def add_i32(self, val1: str, val2: str):
        self.main_text += "%" + self.reg + " = add i32 " + val1 + ", " + val2 + "\n"
        self.str_i += 1

    def add_double(self, val1: str, val2: str):
        self.main_text += "%"+self.reg+" = fadd double " + val1 + ", " + val2 + "\n"
        self.str_i += 1

    def load_i32(self, _id: str):
        self.main_text += "%" + self.reg + " = load i32, i32* %" + _id + "\n"
        self.str_i += 1

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [4 x i8] c\"%f\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%s\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text
