// 1812302

grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

/*
	*****************************************************************************************
									Parser
*/

mptype: INTTYPE | VOIDTYPE ;

body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;


/*
	*****************************************************************************************
									Lexer
*/

COMMENT_BLOCK: '/*' .*? '*/';
COMMENT_LINE: '#' ~[\n];

INTTYPE: 'int' ;

VOIDTYPE: 'void'  ;

ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;