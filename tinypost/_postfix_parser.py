from ._grammar import _operators, _LETTERS, _NUMBERS, _FUNCTION_MAP, _operators_grouping, _precedence

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
		if expression[i] == " " or expression[i] == "\t" or expression[i] == "\n":
			i += 1
			continue
		current_token = expression[i]

		if expression[i] in _operators:
			if previous_token is None:
				if expression[i] == "+":
					expression[i] = ">"
				elif expression[i] == "-":
					expression[i] = "<"
			elif previous_token and not (previous_token.isdigit() or previous_token.upper() in (_LETTERS + "_")) \
				 and not previous_token in [")", "]"]:
				if expression[i] == "+":
					expression[i] = ">"
				elif expression[i] == "-":
					expression[i] = "<"

		previous_token = current_token
		i += 1
	
	return "".join(expression)

def _build_number(expression: str, pos: int):
	result = []
	dot_count = 0

	while pos < len(expression) and (expression[pos].isdigit() or \
		 expression[pos] == "." and dot_count < 1):
		
		if expression[pos] == ".":
			dot_count += 1
		result.append(expression[pos])
		pos += 1

	final = "".join(result)
	if final == ".":
		raise ValueError()
	
	return final, pos

def _build_identifier(expression: str, pos: int):
	result = []
	while pos < len(expression) and expression[pos].upper() in (_LETTERS + _NUMBERS + "_"):
		result.append(expression[pos])
		pos += 1

	final = "".join(result)
	_type = "func" if final in _FUNCTION_MAP else "id"
	return final, pos, _type 

def _infix_to_postfix(expression: str):
	expression = _clean(expression)
	output = []	
	stack = []
	i = 0

	while i < len(expression):
		if expression[i].isdigit() or expression[i] == ".":
			result, i = _build_number(expression, i)
			output.append(result + " ")
			continue
		elif expression[i].upper() in _LETTERS:
			result, i, _type = _build_identifier(expression, i)
			if _type == "id":
				output.append(result + " ")
			else:
				stack.append(result)
			continue
		elif expression[i] in _operators_grouping:
			right_associative = expression[i] == "^" or expression[i] == ">" or expression[i] == "<"
			if _precedence[expression[i]] == 6 or expression[i] == ",":
				while _peek(stack) != _inverse(expression[i]):
					output.append(stack.pop())

				if expression[i] != ",":
					stack.pop()
				if _peek(stack) in _FUNCTION_MAP:
					output.append(stack.pop() + " ")
			elif len(stack) == 0 or _precedence[_peek(stack)] < _precedence[expression[i]] \
				or _precedence[expression[i]] == 0:
				stack.append(expression[i])
			else:
				while len(stack) > 0 and _precedence[_peek(stack)] >= _precedence[expression[i]] \
					and not right_associative:
					output.append(stack.pop())
				stack.append(expression[i])
		i += 1
	
	while len(stack) > 0:
		output.append(stack.pop())
	
	return "".join(output)