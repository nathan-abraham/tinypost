import math
import time
from inspect import signature

from .postfix_parser import _build_number, _build_identifier, _infix_to_postfix, _clean
from .grammar import operators, LETTERS, FUNCTION_MAP, symbol_table

error = None

def _eval_func(func_name, params):
	return FUNCTION_MAP[func_name](*params)

def _eval_basic(left_operand, right_operand, operator):
	left = float(left_operand)
	right = float(right_operand)

	if operator == "+" or operator == ">":
		return left + right
	elif operator == "-" or operator == "<":
		return left - right
	elif operator == "*":
		return left * right
	elif operator == "/":
		return left / right
	elif operator == "^":
		return left ** right

def _eval_postfix(expression: str):
	global error, symbol_table 

	stack = []
	i = 0
	error = None

	current_token = None

	while i < len(expression):
		current_token = expression[i]
		if expression[i].isdigit() or expression[i] == ".":
			current_token, i = _build_number(expression, i)
			stack.append(current_token)
			continue
		elif expression[i].upper() in LETTERS:
			current_token, i, _type = _build_identifier(expression, i)
			if _type == "id":
				if current_token in symbol_table:
					stack.append(str(symbol_table[current_token]))
				else:
					return "Variable not found"
				continue
		if current_token in FUNCTION_MAP or current_token in operators:
			if expression[i] == ">" or expression[i] == "<":
				temp = stack.pop()
				stack.append("0")
				stack.append(temp)
			if len(stack) < 2 and current_token in operators:
				error = i
				return f"Syntax error at position {i}"
			else:
				if current_token in FUNCTION_MAP:
					num_params = len(signature(FUNCTION_MAP[current_token]).parameters)
					params = []
					for _ in range(num_params):
						params.append(float(stack.pop()))
					temp_result = str(_eval_func(current_token, params))
				else:
					right_operand = stack.pop()
					left_operand = stack.pop()
					current_token = expression[i]
					temp_result = str(_eval_basic(left_operand, right_operand, current_token))

				stack.append(temp_result)

		i += 1

	if len(stack) != 1:
		return "Invalid Expression"
	else:
		return float(stack[0])

if __name__ == "__main__":
	expr = "3 / 2"
	expr2 = "3*2+4*5"

	print(_clean(expr))
	print(_infix_to_postfix(expr))

	start = time.time()
	print(_eval_postfix(_infix_to_postfix(expr)))
	end = time.time()
	print(f"Took {end-start} seconds")

	# print(clean(expr2))
	# print(infix_to_postfix(expr2))
	# print(eval_expr(expr2))




