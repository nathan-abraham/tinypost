import time
import math

operators = ["+", "-", "*", "/", "^", ">", "<"]
operators_grouping = operators + ["(", "[", ")", "]"]
error = None

precedence = {
	")": 6,
	"]": 6,

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

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"
ONE_ARG_FUNCTIONS = ["abs", "sqrt", "sin", "cos", "tan", "ln", "acos", "asin", "atan", "atan2", "exp", "log", "sinh", "cosh", "tanh"]
MULT_ARG_FUNCTIONS = ["max", "pow"]
FUNCTION_NAMES = ONE_ARG_FUNCTIONS + MULT_ARG_FUNCTIONS

for function in FUNCTION_NAMES:
	precedence[function] = 1

symbol_table = {
	"nice_var_name": 10,
	"x": 5,
	"pi": math.pi,
	"e": math.e,
}

def peek(stack: list):
	if stack:
		return stack[len(stack)-1]

def inverse(char: str):
	return "(" if char == ")" else "["

def is_balanced(expression: str):
	open_group_symbols = ["[", "("]
	close_group_symbols = ["]", ")"]

	stack = []

	for i in range(len(expression)):
		if expression[i] not in open_group_symbols and expression[i] not in close_group_symbols:
			continue

		if expression[i] in open_group_symbols:
			stack.append(expression[i])
		elif expression[i] in close_group_symbols:
			if (peek(stack) == inverse(expression[i])):
				stack.pop()
			else:
				return False

	return len(stack) == 0

def eval_basic(left_operand, right_operand, operator):
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
	elif operator == "abs":
		return abs(right)
	elif operator == "sqrt":
		return math.sqrt(right)
	elif operator == "sin":
		return math.sin(right)
	elif operator == "cos":
		return math.cos(right)
	elif operator == "tan":
		return math.tan(right)
	elif operator == "max":
		return max(left, right)
	elif operator == "ln":
		return math.log(right)
	elif operator == "asin":
		return math.asin(right)
	elif operator == "acos":
		return math.acos(right)
	elif operator == "atan":
		return math.atan(right)
	elif operator == "atan2":
		return math.atan2(right)
	elif operator == "exp":
		return math.exp(right)
	elif operator == "log":
		return math.log10(right)
	elif operator == "pow":
		return math.pow(left, right)
	elif operator == "sinh":
		return math.sinh(right)
	elif operator == "cosh":
		return math.cosh(right)
	elif operator == "tanh":
		return math.tanh(right)

def eval_postfix(expression: str):
	global error, symbol_table 

	stack = []
	i = 0
	error = None

	func_flag = False
	current_token = None

	while i < len(expression):
		current_token = expression[i]
		if expression[i].isdigit() or expression[i] == ".":
			current_token, i = build_number(expression, i)
			stack.append(current_token)
			continue
		elif expression[i].upper() in LETTERS:
			current_token, i, _type = build_identifier(expression, i)
			if _type == "id":
				stack.append(current_token)
				continue
		if current_token in FUNCTION_NAMES or current_token in operators:
			if current_token not in MULT_ARG_FUNCTIONS and \
				(current_token in FUNCTION_NAMES or expression[i] == ">" or expression[i] == "<"):
				temp = stack.pop()
				stack.append("0")
				stack.append(temp)
			if len(stack) < 2:
				error = i
				return f"Syntax error at position {i}"
			else:
				right_operand = stack.pop()
				left_operand = stack.pop()

				if right_operand in symbol_table:
					right_operand = symbol_table[right_operand]
				elif right_operand[0].upper() in (LETTERS + "_"):
					return f"Syntax error at position {i}"
					
				if left_operand in symbol_table:
					left_operand = symbol_table[left_operand]
				elif left_operand[0].upper() in (LETTERS + "_"):
					return f"Syntax error at position {i}"

				if current_token not in FUNCTION_NAMES:
					current_token = expression[i]

				temp_result = str(eval_basic(left_operand, right_operand, current_token))
				stack.append(temp_result)

		i += 1

	if len(stack) != 1:
		return "Invalid Expression"
	else:
		return float(stack[0])

def infix_to_postfix(expression: str):
	expression = clean(expression)
	output = ""	
	stack = []
	i = 0

	while i < len(expression):
		if expression[i].isdigit() or expression[i] == ".":
			result, i = build_number(expression, i)
			output += result + " "
			continue
		elif expression[i].upper() in LETTERS:
			result, i, _type = build_identifier(expression, i)
			if _type == "id":
				output += result + " "
			else:
				stack.append(result)
			continue
		elif expression[i] in operators_grouping:
			right_associative = expression[i] == "^" or expression[i] == ">" or expression[i] == "<"
			if precedence[expression[i]] == 6:
				while peek(stack) != inverse(expression[i]):
					output += stack.pop()
				stack.pop()
				if peek(stack) in FUNCTION_NAMES:
					output += stack.pop() + " "
			elif len(stack) == 0 or precedence[peek(stack)] < precedence[expression[i]] \
				or precedence[expression[i]] == 0:
				stack.append(expression[i])
			else:
				while len(stack) > 0 and precedence[peek(stack)] >= precedence[expression[i]] \
					and not right_associative:
					output += stack.pop()
				stack.append(expression[i])
		i += 1
	
	while len(stack) > 0:
		output += stack.pop()
	
	return output

def insert(expression: str, chars: str, pos: int):
	return expression[:pos] + chars + expression[pos:]

def clean_old(expression: str):
	i = 0;
	expression = list(expression.replace(" ", ""))

	while i < len(expression):
		if expression[i] in operators:
			if i == 0:
				if expression[i] == "+":
					expression[i] = "p"
				elif expression[i] == "-":
					expression[i] = "m"
			elif not expression[i-1].isdigit() and not expression[i-1] in [")", "]"]:
				if expression[i] == "+":
					expression[i] = "p"
				elif expression[i] == "-":
					expression[i] = "m"

		i += 1
	
	return "".join(expression)

def clean(expression: str):
	i = 0;
	expression = list(expression)

	current_token = None
	previous_token = None

	while i < len(expression):
		if expression[i] == " " or expression[i] == "\t":
			i += 1
			continue
		current_token = expression[i]

		if expression[i] in operators:
			if previous_token is None:
				if expression[i] == "+":
					expression[i] = ">"
				elif expression[i] == "-":
					expression[i] = "<"
			elif previous_token and not (previous_token.isdigit() or previous_token.upper() in (LETTERS + "_")) \
				 and not previous_token in [")", "]"]:
				if expression[i] == "+":
					expression[i] = ">"
				elif expression[i] == "-":
					expression[i] = "<"

		previous_token = current_token
		i += 1
	
	return "".join(expression)

def build_number(expression: str, pos: int):
	result = ""
	dot_count = 0

	while pos < len(expression) and (expression[pos].isdigit() or \
		 expression[pos] == "." and dot_count < 1):
		
		if expression[pos] == ".":
			dot_count += 1
		result += expression[pos]
		pos += 1

	if result == ".":
		raise ValueError()
	
	return result, pos

def build_identifier(expression: str, pos: int):
	result = ""
	while pos < len(expression) and expression[pos].upper() in (LETTERS + NUMBERS + "_"):
		result += expression[pos]
		pos += 1

	_type = "func" if result in FUNCTION_NAMES else "id"
	return result, pos, _type 

def eval_expr(expression: str):
	return eval_postfix(infix_to_postfix(expression))

if __name__ == "__main__":
	expr = "max(pi+3, 4)"
	expr2 = "3*2+4*5"

	print(clean(expr))
	print(infix_to_postfix(expr))

	start = time.time()
	print(eval_expr(expr))
	end = time.time()
	print(f"Took {end-start} seconds")

	# print(clean(expr2))
	# print(infix_to_postfix(expr2))
	# print(eval_expr(expr2))




