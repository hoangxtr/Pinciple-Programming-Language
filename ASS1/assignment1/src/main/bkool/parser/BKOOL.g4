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
program: class_dec+;

class_dec: 'class' ID ('extends' ID)? LP member* RP;

member: attribute_dec | method_dec;

attribute_dec: ( STATIC? FINAL? | FINAL STATIC ) (without_void_data_type | VOID) variable_init (COMMA variable_init)* SEMI;

variable_init: ID ( EQ exp )?;


// có thể có hoặc không type, do có thể là constructor
method_dec: normal_method | special_method;

normal_method: STATIC? (without_void_data_type | VOID) ID LB ( param_dec (SEMI param_dec)* )? RB block_stmt;

special_method: STATIC? ID LB ( param_dec (SEMI param_dec)* )? RB block_stmt; // constructor có static không ?

param_dec: (without_void_data_type | VOID) ID (COMMA ID)*;

block_stmt: LP var_dec* stmt* RP;

var_dec: FINAL? (without_void_data_type | VOID) variable_init (COMMA variable_init)*SEMI;

stmt: assign_stmt | if_stmt | for_stmt | break_stmt | continue_stmt | return_stmt | medthod_invocation_stmt;

assign_stmt: lhs ASSIGN_OP exp SEMI;

lhs: ID | mutable_attr | array_element;

mutable_attr: ID (DOT ID)+;

array_element: exp LB exp RB;

// mutable_attr_component: ID DOT ID;

exp: exp1 (GT_OP | GE_OP | LT_OP | LE_OP) exp1 | exp1;
exp1: exp2 (EQUAL_OP | NOT_EQUAL_OP) exp2 | exp2;
exp2: exp2 (AND_OP | OR_OP) exp3 | exp3;
exp3: exp3 (ADD_OP | SUB_OP) exp4 | exp4;
exp4: exp4 (MUL_OP | INT_DIV_OP | FLOAT_DIV_OP | MOD_OP) exp5 | exp5;
exp5: exp5 CONCAT_OP exp6;
exp6: NOT_OP exp7 | exp7;
exp7: (ADD_OP | SUB_OP) exp8 | exp8;
exp8: exp9 LB exp RB | exp9;
exp9: exp10 DOT | exp10;
exp10: NEW exp11 | exp11;
exp11: LB operand RB | operand;
operand: ID | FLOATLIT | INTLIT | STRINGLIT | BOOLEAN | ARRAYLIT | exp;

without_void_data_type: INT | FLOAT | BOOLEAN | VOID | array_type; // missing class type

array_type: (INT | FLOAT | STRING | BOOLEAN) LSB DIGIT+ RSB;


// array_lit: LP array_lit_element RP;
// array_lit_element: 	INTLIT (COMMA INTLIT)* | 
// 					FLOATLIT (COMMA FLOATLIT)* | 
// 					STRINGLIT (COMMA STRINGLIT)* | 
// 					BOOLEANLIT (COMMA BOOLEANLIT)*;

/*
	*****************************************************************************************
									Lexer
*/

COMMENT_BLOCK: '/*' .*? '*/';
COMMENT_LINE: '#' ~[\n]*;

INTLIT: '-'? DIGIT+;
FLOATLIT: '-'? DIGIT+  ( FLOATLIT_DECIMAL_PART FLOATLIT_EXPONENT_PART? | FLOATLIT_EXPONENT_PART)  ;
BOOLEANLIT: 'true' | 'false';
STRINGLIT: DB STRING_CHAR* DB;
ARRAYLIT: LP SPACE* ARRAYLIT_ELEMENTS SPACE* RP;

// ARRAY: (INT | FLOAT | STRING | BOOLEAN) LSB DIGIT+ RSB;
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
STRING: 'string';
VOID: 'void';

STATIC: 'static';
FINAL: 'final';

REMAIN_KEYWORD: 	'boolean' | 'break' | 'class' | 'continue' | 'do' | 'else' |
			'extends' | 'float' | 'if' | 'int' | 'string' |
			'then' | 'for' | 'return' | 'void' |
			'nil' | 'this' | 'final' | 'static' | 'to' | 'downto';

ID: [a-zA-Z_] [a-zA-Z_0-9]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
FLOAT_DIV_OP: '/';
INT_DIV_OP: '\\';
MOD_OP: '%';
NOT_EQUAL_OP: '!=';
EQUAL_OP: '==';
LT_OP: '<';
GT_OP: '>';
LE_OP: '<=';
GE_OP: '>=';
OR_OP: '||';
AND_OP: '&&';
NOT_OP: '!';
CONCAT_OP: '^';
NEW: 'new';

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

LSB: '[';

RSB: ']';

SEMI: ';' ;

COLON: ':';

DOT: '.';

COMMA: ',';

DB: '"';

EQ: '=';

ASSIGN_OP: ':=';

ERROR_CHAR: .
	{
		raise ErrorToken(self.text)
	};
UNCLOSE_STRING: DB STRING_CHAR* ('\n' | EOF)
	{
		y = str(self.text)
		raise UncloseString(y[1:-1])
	};
ILLEGAL_ESCAPE: DB STRING_CHAR* ~[btnfr"'\\]
	{
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};

fragment DIGIT: [0-9];
fragment E: [eE];
fragment FLOATLIT_DECIMAL_PART: DOT DIGIT*;
fragment FLOATLIT_EXPONENT_PART: E [+-]? DIGIT+;
fragment STRING_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ ;
fragment ARRAYLIT_ELEMENTS: INTLIT SPACE* (COMMA SPACE* INTLIT)* | FLOATLIT SPACE* (COMMA SPACE* FLOATLIT)* | 
							STRINGLIT SPACE* (COMMA SPACE* STRINGLIT)* | BOOLEANLIT SPACE* (COMMA SPACE* BOOLEANLIT)*;

fragment ESC_SEQ: '\\' [btnfr"'\\] ;
fragment SPACE: ' ';
