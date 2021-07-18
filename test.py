import unittest
import shunt
import math

class ExprTest(unittest.TestCase):

	def test_add(self):
		expr = "3 + 4"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_sub(self):
		expr = "6 - 2"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_div(self):
		expr = "9.32 / 2"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_mul(self):
		expr = "3.1415 * 7.2"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_expr(self):
		expr = "-3.21^5.6"
		expr_py = "-3.21**5.6"
		self.assertEquals(shunt.eval_expr(expr), eval(expr_py))

	def test_float(self):
		expr = "31.415"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_paren(self):
		expr = "(3 + 4 - 2 + 6.2) / 2"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_one_arg_func(self):
		expr = "sin(3 + 4 / 2)"
		expr_py = expr.replace("sin", "math.sin")
		self.assertEquals(shunt.eval_expr(expr), eval(expr_py))

	def test_mult_arg_func(self):
		expr = "max(3 + 4 / 4, 7)"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_var(self):
		x = 2.32
		shunt.symbol_table["x"] = 2.32
		expr = "3 + x / 4"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def test_standalone_var(self):
		x = 2.32
		shunt.symbol_table["x"] = 2.32
		expr = "x"
		self.assertEquals(shunt.eval_expr(expr), eval(expr))

	def neg_exp(self):
		x = 5.32
		expr = "-x^4.90"
		expr_py = "-x ** 4.90"
		self.assertEquals(shunt.eval_expr(expr), eval(expr_py))
