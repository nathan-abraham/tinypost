from .grammar import operators, LETTERS, NUMBERS, FUNCTION_MAP, operators_grouping, precedence

def _peek(stack: list):
	if stack:
		return stack[len(stack)-1]

def _inverse(char: str):
	return "(" if char == ")" or char == "," else "["

def _clean(expression: str):
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

def _build_number(expression: str, pos: int):
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

def _build_identifier(expression: str, pos: int):
	result = ""
	while pos < len(expression) and expression[pos].upper() in (LETTERS + NUMBERS + "_"):
		result += expression[pos]
		pos += 1

	_type = "func" if result in FUNCTION_MAP else "id"
	return result, pos, _type 

def _infix_to_postfix(expression: str):
	expression = _clean(expression)
	output = ""	
	stack = []
	i = 0

	while i < len(expression):
		if expression[i].isdigit() or expression[i] == ".":
			result, i = _build_number(expression, i)
			output += result + " "
			continue
		elif expression[i].upper() in LETTERS:
			result, i, _type = _build_identifier(expression, i)
			if _type == "id":
				output += result + " "
			else:
				stack.append(result)
			continue
		elif expression[i] in operators_grouping:
			right_associative = expression[i] == "^" or expression[i] == ">" or expression[i] == "<"
			if precedence[expression[i]] == 6 or expression[i] == ",":
				while _peek(stack) != _inverse(expression[i]):
					output += stack.pop()

				if expression[i] != ",":
					stack.pop()
				if _peek(stack) in FUNCTION_MAP:
					output += stack.pop() + " "
			elif len(stack) == 0 or precedence[_peek(stack)] < precedence[expression[i]] \
				or precedence[expression[i]] == 0:
				stack.append(expression[i])
			else:
				while len(stack) > 0 and precedence[_peek(stack)] >= precedence[expression[i]] \
					and not right_associative:
					output += stack.pop()
				stack.append(expression[i])
		i += 1
	
	while len(stack) > 0:
		output += stack.pop()
	
	return output