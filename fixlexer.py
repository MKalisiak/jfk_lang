filename = "JFKLexer.py"
fr = open(filename)
content = fr.readlines()
fr.close()

text = "\n\ndef skip(): pass\n"
line_idx = content.index("import sys\n")

content[line_idx+1] = text

fw = open(filename, "w")
fw.writelines(content)
fw.close()
