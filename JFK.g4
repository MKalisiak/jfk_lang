grammar JFK;

program: line*
    ;

line:   statement? comment? NEWLINE 
    ;

statement:	  OUTPUT '(' expression ')'         #output
	        | ID '=' expression		            #assign
   ;

expression:   value			             #single
            | expression ADD value       #add
            | expression SUB value 	     #sub
            | expression MUL value       #mul
            | expression DIV value       #div
            | expression MOD value	     #mod
   ;

comment:    '#' (~(NEWLINE))*
    ;

value:   ID                         #id
       | INT                        #int
       | FLOAT                      #float
       | STRING                     #string
       | INPUT '(' TYPE_KEYWORD ')' #input
   ;

TYPE_KEYWORD: 'int' | 'float' | 'string'
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
