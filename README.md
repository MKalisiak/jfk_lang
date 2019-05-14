# jfk_lang

Add permissions to execute files:
1. `chmod u+x clean jfk`

Grammar compilation:
1. `antlr4 -Dlanguage=Python3 JFK.g4`
2. `python fixlexer.py` (**important!**) - fixes incorrectly generated JFKLexer.py

Running example:
1. Compile program: `./jfk example.jfk`
2. Run it: `./example.exec`

Cleaning:
1. `./clean example`
