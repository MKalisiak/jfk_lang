class LLVMGenerator:
    header_text = ""
    main_text = ""
    str_i = 1
    strings_declared = {}

    def output_string(self, text):
        str_len = len(text.encode('utf-8'))
        str_type = "[" + str(str_len + 2) + " x i8]"
        self.header_text += "@str" + self.reg + " = constant" + str_type + " c\"" + text + "\\0A\\00\"\n"
        self.main_text += ("call i32 (i8*, ...) @printf(i8* getelementptr inbounds ( " + str_type + ", " + str_type +
                           "* @str" + self.reg + ", i32 0, i32 0))\n")
        self.str_i += 1

    @property
    def reg(self):
        return str(self.str_i)

    def prev_str(self, sub=1):
        return str(self.str_i - sub)

    def output_id_i32(self, _id: str):
        self.main_text += "%"+self.reg+" = load i32, i32* %"+_id+"\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 %" + str(self.str_i - 1) + ")\n"
        self.str_i += 1

    def output_id_double(self, _id: str):
        self.main_text += "%" + self.reg + " = load double, double* %" + _id + "\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strpd, i32 0, i32 0), double %" + str(self.str_i - 1) + ")\n"
        self.str_i += 1

    def output_id_string(self, _id: str):
        self.main_text += "%" + self.reg + " = load i8*, i8** %" + _id + ", align 8\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strs, i32 0, i32 0), i8* %" + str(self.str_i - 1) +")\n"
        self.str_i += 1

    def output_i32(self, value: str):
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32 " + value + ")\n"
        self.str_i += 1

    def output_double(self, value: str):
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strpd, i32 0, i32 0), double " + value + ")\n"
        self.str_i += 1

    def declare_i32(self, _id: str):
        self.main_text += "%"+_id+" = alloca i32\n"

    def declare_double(self, _id: str):
        self.main_text += "%" + _id + " = alloca double\n"

    def assign_i32(self, _id: str, value: str):
        self.main_text += "store i32 " + value + ", i32* %" + _id + "\n"

    def assign_double(self, _id: str, value: str):
        self.main_text += "store double " + value + ", double* %" + _id + "\n"

    def assign_id_i32(self, target, source):
        self.load_i32(source)
        self.main_text += "store i32 %" + str(self.str_i - 1) + ", i32* %" + target + "\n"

    def assign_id_double(self, target, source):
        self.load_double(source)
        self.main_text += "store double %" + str(self.str_i - 1) + ", double* %" + target + "\n"

    def assign_string(self, _id: str, value: str):
        str_len = len(value.encode('utf-8')) + 2
        str_type = "[" + str(str_len) + " x i8]"
        if _id not in self.strings_declared:
            self.strings_declared[_id] = 0

        n = self.strings_declared[_id]
        self.header_text += "@" + _id + "." + str(n) + " = constant" + str_type + " c\"" + value + "\\0A\\00\"\n"

        if self.strings_declared[_id] == 0:
            self.main_text += "%" + _id + " = alloca i8*, align 8\n"

        self.strings_declared[_id] += 1
        self.main_text += "store i8* getelementptr inbounds ([" + str(str_len) + " x i8], [" + str(str_len) + " x i8]* @" + _id + "." + str(n) + ", i32 0, i32 0), i8** %" + _id +", align 8\n"

    def assign_id_string(self, target, source):
        self.main_text += f"%{target} = alloca i8*, align 8\n"
        self.main_text += f"%{self.reg} = load i8*, i8** %{source}, align 8\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = call i64 @strlen(i8* %{self.prev_str()})\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = call noalias i8* @malloc(i64 %{self.prev_str()})\n"
        self.str_i += 1
        self.main_text += f"store i8* %{self.prev_str()}, i8** %{target}, align 8\n"
        self.main_text += f"%{self.reg} = load i8*, i8** %{target}, align 8\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = load i8*, i8** %{source}, align 8\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = call i8* @strcpy(i8* %{self.prev_str(2)}, i8* %{self.prev_str()})\n"
        self.str_i += 1

    def load_i32(self, _id: str):
        self.main_text += "%" + self.reg + " = load i32, i32* %" + _id + "\n"
        self.str_i += 1

    def load_double(self, _id):
        self.main_text += "%" + self.reg + " = load double, double* %" + _id + "\n"
        self.str_i += 1

    def i32_to_double(self, value: str):
        self.main_text += "%" + self.reg + " = sitofp i32 " + value + " to double\n"
        self.str_i += 1

    def i32_to_double_id(self, _id: str):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = sitofp i32 %" + self.prev_str() + " to double\n"
        self.str_i += 1

    def mul_i32(self, value1, value2):
        self.main_text += "%"+self.reg+" = mul i32 "+value1+", "+value2+"\n"
        self.str_i += 1

    def mul_id_i32(self, _id1, _id2):
        self.load_i32(_id1)
        self.load_i32(_id2)
        self.main_text += "%" + self.reg + " = mul i32 %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mul_hybrid_i32_value_id(self, value, _id):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = mul i32 " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mul_hybrid_i32_id_value(self, _id, value):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = mul i32 %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def mul_double(self, value1, value2):
        self.main_text += "%" + self.reg + " = fmul double " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def mul_id_double(self, _id1, _id2):
        self.load_double(_id1)
        self.load_double(_id2)
        self.main_text += "%" + self.reg + " = fmul double %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mul_hybrid_double_value_id(self, value, _id):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fmul double " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1
        
    def mul_hybrid_double_id_value(self, _id, value):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fmul double %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1
    ###################################################################################################################

    def add_i32(self, value1, value2):
        self.main_text += "%"+self.reg+" = add i32 "+value1+", "+value2+"\n"
        self.str_i += 1

    def add_id_i32(self, _id1, _id2):
        self.load_i32(_id1)
        self.load_i32(_id2)
        self.main_text += "%" + self.reg + " = add i32 %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def add_hybrid_i32_value_id(self, value, _id):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = add i32 " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def add_hybrid_i32_id_value(self, _id, value):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = add i32 %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def add_double(self, value1, value2):
        self.main_text += "%" + self.reg + " = fadd double " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def add_id_double(self, _id1, _id2):
        self.load_double(_id1)
        self.load_double(_id2)
        self.main_text += "%" + self.reg + " = fadd double %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def add_hybrid_double_value_id(self, value, _id):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fadd double " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def add_hybrid_double_id_value(self, _id, value):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fadd double %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1
    # ##################################################################################################################

    def sub_i32(self, value1, value2):
        self.main_text += "%" + self.reg + " = sub nsw i32 " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def sub_id_i32(self, _id1, _id2):
        self.load_i32(_id1)
        self.load_i32(_id2)
        self.main_text += "%" + self.reg + " = sub nsw i32 %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def sub_hybrid_i32_value_id(self, value, _id):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = sub nsw i32 " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def sub_hybrid_i32_id_value(self, _id, value):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = sub nsw i32 %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def sub_double(self, value1, value2):
        self.main_text += "%" + self.reg + " = fsub double " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def sub_id_double(self, _id1, _id2):
        self.load_double(_id1)
        self.load_double(_id2)
        self.main_text += "%" + self.reg + " = fsub double %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def sub_hybrid_double_value_id(self, value, _id):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fsub double " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def sub_hybrid_double_id_value(self, _id, value):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fsub double %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1
    # ##################################################################################################################

    def div_i32(self, value1, value2):
        self.main_text += "%" + self.reg + " = sdiv i32 " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def div_id_i32(self, _id1, _id2):
        self.load_i32(_id1)
        self.load_i32(_id2)
        self.main_text += "%" + self.reg + " = sdiv i32 %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def div_hybrid_i32_value_id(self, value, _id):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = sdiv i32 " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def div_hybrid_i32_id_value(self, _id, value):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = sdiv i32 %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def div_double(self, value1, value2):
        self.main_text += "%" + self.reg + " = fdiv double " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def div_id_double(self, _id1, _id2):
        self.load_double(_id1)
        self.load_double(_id2)
        self.main_text += "%" + self.reg + " = fdiv double %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def div_hybrid_double_value_id(self, value, _id):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fdiv double " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def div_hybrid_double_id_value(self, _id, value):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = fdiv double %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1
    # ##################################################################################################################

    def mod_i32(self, value1, value2):
        self.main_text += "%" + self.reg + " = srem i32 " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def mod_id_i32(self, _id1, _id2):
        self.load_i32(_id1)
        self.load_i32(_id2)
        self.main_text += "%" + self.reg + " = srem i32 %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mod_hybrid_i32_value_id(self, value, _id):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = srem i32 " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mod_hybrid_i32_id_value(self, _id, value):
        self.load_i32(_id)
        self.main_text += "%" + self.reg + " = srem i32 %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def mod_double(self, value1, value2):
        self.main_text += "%" + self.reg + " = frem double " + value1 + ", " + value2 + "\n"
        self.str_i += 1

    def mod_id_double(self, _id1, _id2):
        self.load_double(_id1)
        self.load_double(_id2)
        self.main_text += "%" + self.reg + " = frem double %" + self.prev_str(2) + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mod_hybrid_double_value_id(self, value, _id):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = frem double " + value + ", %" + self.prev_str() + "\n"
        self.str_i += 1

    def mod_hybrid_double_id_value(self, _id, value):
        self.load_double(_id)
        self.main_text += "%" + self.reg + " = frem double %" + self.prev_str() + ", " + value + "\n"
        self.str_i += 1

    def input_i32(self):
        self.declare_i32(self.reg)
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32* %" + self.prev_str() + ")\n"
        self.str_i += 1
        self.load_i32(self.prev_str(2))

    def input_double(self):
        self.declare_double(self.reg)
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strpd, i32 0, i32 0), double* %" + self.prev_str() + ")\n"
        self.str_i += 1
        self.load_double(self.prev_str(2))

    # TODO: assign id string
    # Znaki specjalne w stringu

    def input_string(self, max_length=256):
        self.main_text += "%" + self.reg + " = alloca i8*\n"
        self.str_i += 1
        self.main_text += "%" + self.reg + " = call noalias i8* @malloc(i64 " + str(max_length) + ")\n"
        self.main_text += f"store i8* %{self.reg}, i8** %{self.prev_str()}\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = load i8*, i8** %{self.prev_str(2)}\n"
        self.str_i += 1
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strs, i32 0, i32 0), i8* %{self.prev_str()})\n"
        self.str_i += 1

    """
    mamy zapisanego consta, wiec wystarczy go załadować to nowej zmiennej. Mozna wyrzucic strcpy - może XD
    """

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "declare noalias i8* @malloc(i64)\n"
        text += "declare i64 @strlen(i8*)\n"
        text += "declare i8* @strcpy(i8*, i8*)\n"
        text += "@strpi = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strpd = constant [5 x i8] c\"%lf\\0A\\00\"\n"
        text += "@strs = constant [4 x i8] c\"%s\\0A\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text
