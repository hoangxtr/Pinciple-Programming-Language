# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKOOLParser import BKOOLParser
else:
    from BKOOLParser import BKOOLParser

# This class defines a complete generic visitor for a parse tree produced by BKOOLParser.

class BKOOLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKOOLParser#program.
    def visitProgram(self, ctx:BKOOLParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#class_dec.
    def visitClass_dec(self, ctx:BKOOLParser.Class_decContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit.
    def visitArray_lit(self, ctx:BKOOLParser.Array_litContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKOOLParser#array_lit_element.
    def visitArray_lit_element(self, ctx:BKOOLParser.Array_lit_elementContext):
        return self.visitChildren(ctx)



del BKOOLParser