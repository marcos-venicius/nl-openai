#!/usr/bin/env python3

from code_reader import CodeReader
from syntax_checker import SyntaxChecker
from compiler import Compiler
import argparse
import os

program_name = os.path.basename(__file__)

parser = argparse.ArgumentParser(program_name, description='Write code with natural language', usage=f'{program_name} code.nl')

parser.add_argument('code', help='Code')

args = parser.parse_args()

code_reader = CodeReader(args.code)

code = code_reader.read()

syntax_checker = SyntaxChecker(code)

syntax_checker.check_syntax()

code_as_string = ''.join(code)

compiler = Compiler(code_as_string)

code = compiler.compile()

eval(code)