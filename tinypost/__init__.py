from . import _shunting_yard as shunt 
from . import _postfix_parser as postfix_parser
from . import _grammar as grammar

class TPExpr:
	def __init__(self, expr: str):
		self.__expr = expr

	def get_expr(self):
		return self.__expr

	def __repr__(self):
		return self.__expr

	def __str__(self):
		return self.__expr

def eval_expr(expression: str):
	return shunt._eval_postfix(postfix_parser._infix_to_postfix(expression))

def compile_expr(expression: str):
	return TPExpr(postfix_parser._infix_to_postfix(expression))

def eval_compiled(expression: TPExpr):
	return shunt._eval_postfix(expression.get_expr())

def add_var(var_name: str, var: float):
	grammar._symbol_table[var_name] = var

def update_var(var_name: str, var: float):
	grammar._symbol_table[var_name] = var

def add_func(func_name: str, func):
	grammar._FUNCTION_MAP[func_name] = func

def update_func(func_name: str, func):
	grammar._FUNCTION_MAP[func_name] = func