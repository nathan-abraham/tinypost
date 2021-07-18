import math
from .functions import log, max_two

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
operators = ["+", "-", "*", "/", "^", ">", "<", ","]
operators_grouping = operators + ["(", "[", ")", "]"]

precedence = {
	")": 6,
	"]": 6,
	",": 6,

	"^": 4,

	"<": 4,
	">": 4,

	"*": 3,
	"/": 3,
	"%": 3,

	"+": 2,
	"-": 2, 

	"(": 0,
	"[": 0,

	None: float("inf"),
}

FUNCTION_MAP = {
	"abs": abs,
	"sqrt": math.sqrt,
	"sin": math.sin, 
	"cos": math.cos, 
	"tan": math.tan, 
	"ln": log, 
	"acos": math.acos, 
	"asin": math.asin, 
	"atan": math.atan, 
	"exp": math.exp, 
	"log": math.log10, 
	"sinh": math.sinh, 
	"cosh": math.cosh, 
	"tanh": math.tanh,

	"atan2": math.atan2, 
	"max": max_two,
	"pow": math.pow,
}

for function in FUNCTION_MAP:
	precedence[function] = 1

symbol_table = {
	"nice_var_name": 10,
	"x": 5,
	"pi": math.pi,
	"e": math.e,
}