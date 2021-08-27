import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_1(self):
        self.assertTrue(TestLexer.test("1.333","1.333,<EOF>",1))
    def test_2(self):
        self.assertTrue(TestLexer.test("1.e6","1.e6,<EOF>",2))
    def test_3(self):
        self.assertTrue(TestLexer.test("1e+7e","1e+7,e,<EOF>",3))
    def test_4(self):
        self.assertTrue(TestLexer.test("9.0","9.0,<EOF>",4))
    def test_5(self):
        self.assertTrue(TestLexer.test("0.33E-3","0.33E-3,<EOF>",5))
    def test_6(self):
        self.assertTrue(TestLexer.test("128e+42","128e+42,<EOF>",6))
    def test_7(self):
        self.assertTrue(TestLexer.test("153620 12","153620,12,<EOF>",7))
    def test_8(self):
        self.assertTrue(TestLexer.test(".12",".,12,<EOF>",8))
    def test_9(self):
        self.assertTrue(TestLexer.test("143e","143,e,<EOF>",9))
    def test_10(self):
        self.assertTrue(TestLexer.test("\"This is a string containing tab \\t\"","\"This is a string containing tab \\t\",<EOF>",10))
    def test_11(self):
        self.assertTrue(TestLexer.test("\"He asked me: \\\"Where is John? \\\"\"","\"He asked me: \\\"Where is John? \\\"\",<EOF>",11))
    def test_12(self):
        self.assertTrue(TestLexer.test("{1, 2, 3}","{1, 2, 3},<EOF>",12))
    def test_13(self):
        self.assertTrue(TestLexer.test("{2.3, 4.2, 102e3}","{2.3, 4.2, 102e3},<EOF>",13))
    def test_14(self):
        self.assertTrue(TestLexer.test("{1, 2, 3.4}","{,1,,,2,,,3.4,},<EOF>",14))
    def test_15(self):
        self.assertTrue(TestLexer.test("{1, \"Hello\", 1}","{,1,,,\"Hello\",,,1,},<EOF>",15))
    def test_16(self):
        self.assertTrue(TestLexer.test("/* Hello world, i'm a dev */","/* Hello world, i'm a dev */,<EOF>",16))
    def test_17(self):
        self.assertTrue(TestLexer.test("/* Baby \n can you here me*/","/* Baby \n can you here me*/,<EOF>",17))
    def test_18(self):
        self.assertTrue(TestLexer.test("/* \" Playing games\" */","/* \" Playing games\" */,<EOF>",18))
    def test_19(self):
        self.assertTrue(TestLexer.test("# \" Playing games\" */","# \" Playing games\" */,<EOF>",19))
    def test_20(self):
        self.assertTrue(TestLexer.test("# Comment 1 /*Comment 2*/","# Comment 1 /*Comment 2*/,<EOF>",20))
    def test_21(self):
        self.assertTrue(TestLexer.test("text1\\ text2","text1,\,text2,<EOF>",21))
    def test_22(self):
        self.assertTrue(TestLexer.test("hello 3rs","hello,3,rs,<EOF>",22))
    def test_23(self):
        self.assertTrue(TestLexer.test("\"Hello","Unclosed String: Hell",23))
    # def test_22(self):
    #     self.assertTrue(TestLexer.test("hello 3rs","hello,3,rs,<EOF>",22))
    # def test_22(self):
    #     self.assertTrue(TestLexer.test("hello 3rs","hello,3,rs,<EOF>",22))
    