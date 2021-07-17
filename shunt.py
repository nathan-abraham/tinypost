import time

operators = ["+", "-", "*", "/", "^", "p", "m"]
operators_grouping = operators + ["(", "[", ")", "]"]
error = None

precedence = {
	")": 5,
	"]": 5,

	"^": 4,

	"m": 3,
	"p": 3,

	"*": 2,
	"/": 2,
	"%": 2,

	"+": 1,
	"-": 1,

	"(": 0,
	"[": 0,

	None: float("inf"),
}

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "0123456789"


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

	if operator == "+" or operator == "p":
		return left + right
	elif operator == "-" or operator == "m":
		return left - right
	elif operator == "*":
		return left * right
	elif operator == "/":
		return left / right
	elif operator == "^":
		return left ** right


def eval_postfix(expression: str):
	global error 

	stack = []
	i = 0
	error = None

	while i < len(expression):
		if expression[i].isdigit():
			result, i = build_number(expression, i)
			stack.append(result)
		elif expression[i] in operators:
			if expression[i] == "m" or expression[i] == "p":
				temp = stack.pop()
				stack.append("0")
				stack.append(temp)
			if len(stack) < 2:
				error = i
				return f"Syntax error at position {i}"
			else:
				right_operand = stack.pop()
				left_operand = stack.pop()

				temp_result = str(eval_basic(left_operand, right_operand, expression[i]))
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
		if expression[i].isdigit():
			result, i = build_number(expression, i)
			output += result + " "
			continue
		elif expression[i].upper() in LETTERS:
			result, i = build_identifier(expression, i)
			output += result + " "
			continue
		elif expression[i] in operators_grouping:
			if precedence[expression[i]] == 5:
				while peek(stack) != inverse(expression[i]):
					output += stack.pop()
				stack.pop()
			elif len(stack) == 0 or precedence[peek(stack)] < precedence[expression[i]] \
				or precedence[expression[i]] == 0:
				stack.append(expression[i])
			else:
				while len(stack) > 0 and precedence[peek(stack)] >= precedence[expression[i]]:
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
					expression[i] = "p"
				elif expression[i] == "-":
					expression[i] = "m"
			elif previous_token and not previous_token.isdigit() and not previous_token in [")", "]"]:
				if expression[i] == "+":
					expression[i] = "p"
				elif expression[i] == "-":
					expression[i] = "m"

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
	
	return result, pos

def build_identifier(expression: str, pos: int):
	result = ""
	while pos < len(expression) and expression[pos].upper() in (LETTERS + NUMBERS + "_"):
		result += expression[pos]
		pos += 1

	return result, pos

def eval_expr(expression: str):
	return eval_postfix(infix_to_postfix(expression))

if __name__ == "__main__":
	expr = "3 + x"
	expr_py = "2+2/4**2"

	print(clean(expr))
	print(infix_to_postfix(expr))
	# print(eval_postfix(infix_to_postfix(expr)))


# start = time.time()
# expr = infix_to_postfix(expr)
# for i in range(100000):
# 	eval_postfix(expr)
# end = time.time()

# print("My eval took took " + str(end-start))

# start = time.time()
# for i in range(100000):
# 	eval(expr_py)
# end = time.time()
# print("Python eval took " + str(end-start))



