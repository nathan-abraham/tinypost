import math
from ._functions import _log, _max_two

_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
_NUMBERS = "0123456789"
_operators = ["+", "-", "*", "/", "^", ">", "<", ","]
_operators_grouping = _operators + ["(", "[", ")", "]"]

_precedence = {
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

_BUILTIN_FUNCTION_MAP = {
	"abs": abs,
	"sqrt": math.sqrt,
	"sin": math.sin, 
	"cos": math.cos, 
	"tan": math.tan, 
	"ln": _log, 
	"acos": math.acos, 
	"asin": math.asin, 
	"atan": math.atan, 
	"exp": math.exp, 
	"log": math.log10, 
	"sinh": math.sinh, 
	"cosh": math.cosh, 
	"tanh": math.tanh,

	"atan2": math.atan2, 
	"max": _max_two,
	"pow": math.pow,
}

_FUNCTION_MAP = {
	**_BUILTIN_FUNCTION_MAP,
}

for function in _FUNCTION_MAP:
	_precedence[function] = 1

_symbol_table = {
	"nice_var_name": 10,
	"x": 5,
	"pi": math.pi,
	"e": math.e,
}

if __name__ == "__main__":
	print(_FUNCTION_MAP)