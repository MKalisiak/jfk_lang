grammar JFK;

program: line*
    ;

line:   statement? comment? NEWLINE 
    ;

statement:	  ID '=' INPUT '()'              #input
	        | OUTPUT '(' expression ')'      #output
	        | ID '=' expression		         #assign
   ;

expression:   value ADD expression	#add
            | value SUB expression	#sub
            | value MUL expression	#mul
            | value DIV expression	#div
            | value MOD expression	#mod
	        | value			        #single
   ;

comment:    '#' (~(NEWLINE))*
    ;

value:   ID     #id
       | INT    #int
       | FLOAT  #float
       | STRING #string
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

STRING :  '"' ( ~('\\'|'"') )* '"'
    ;

ID:   ('a'..'z'|'A'..'Z'|'_')+ ('a'..'z'|'A'..'Z'|'_'|'0'..'9')*
    ;

FLOAT: DIGIT+ '.' DIGIT*
    ;

INT:   DIGIT+
    ;

NEWLINE:	'\r'? '\n'
    ;

WS:   (' '|'\t')+ -> skip
    ;

fragment DIGIT: '0'..'9' ;
fragment LOWERCASE: 'a'..'z' ;
fragment UPPERCASE: 'A'..'Z' ;
fragment LETTER: ( 'a'..'z' | 'A'..'Z' ) ;
