grammar JFK;

program: (line | func)*
    ;

func: params '->' ID ':' TYPE_KEYWORD '->' block
    ;

params: param (',' param)*
        |
    ;

param: ID ':' TYPE_KEYWORD
    ;

block: '{' line* '}'
    ;

ifblock: block
    ;

elseblock: block
    ;

loopblock: block
    ;

line:   statement? comment? NEWLINE 
    ;

statement:	  OUTPUT '(' expression ')'                 #output
	        | ID '=' expression		                    #assign
	        | IF expression ifblock (ELSE elseblock)?   #ifStmt
	        | WHILE expression loopblock                #while
	        | RETURN expression                         #return
   ;

expression:   value			             #single
            | expression ADD value       #add
            | expression SUB value 	     #sub
            | expression MUL value       #mul
            | expression DIV value       #div
            | expression MOD value	     #mod
            | expression EQ  value       #equal
            | expression NEQ value       #notEqual
            | expression GT  value       #greaterThan
            | expression GTE value       #greaterThanEqual
            | expression LT  value       #lessThan
            | expression LTE value       #lessThanEqual
   ;

comment:    '#' (~(NEWLINE))*
    ;

value:   ID                         #id
       | INT                        #int
       | FLOAT                      #float
       | STRING                     #string
       | INPUT '(' TYPE_KEYWORD ')' #input
       | TRUE                       #true
       | FALSE                      #false
   ;

RETURN: 'return'
    ;

WHILE: 'while'
    ;

ELSE: 'else'
    ;

IF: 'if'
    ;

EQ: '=='
    ;

NEQ: '!='
    ;

GT: '>'
    ;

GTE: '>='
    ;

LT: '<'
    ;

LTE: '<='
    ;

TRUE: 'True'
    ;

FALSE: 'False'
    ;

TYPE_KEYWORD: 'int' | 'float' | 'string' | 'bool'
    ;

INPUT:  'input'
    ;

OUTPUT: 'output'
    ;

ADD:    '+'
    ;

SUB:    '-'
    ;

MUL:    '*'
    ;

DIV:    '/'
    ;

MOD:    '%'
    ;

STRING :  '"' ( ~('"') )* '"'
    ;

ID:   ('a'..'z'|'A'..'Z'|'_')+ ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
    ;

FLOAT: '-'? DIGIT+ '.' DIGIT*
    ;

INT:   '-'? DIGIT+
    ;

NEWLINE:	'\r'? '\n'
    ;

WS:   (' '|'\t')+ -> skip
    ;

fragment DIGIT: '0'..'9' ;
fragment LOWERCASE: 'a'..'z' ;
fragment UPPERCASE: 'A'..'Z' ;
fragment LETTER: ( 'a'..'z' | 'A'..'Z' ) ;
