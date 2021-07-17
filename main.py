import shunt

while True:
	expr = input("math shell > ") 
	if expr == "exit" or expr == "quit":
		break
	
	result = shunt.eval_expr(expr)
	if shunt.error:
		print(expr)
		print(" " * shunt.error + "^")
		print("SyntaxError: invalid syntax")
	else:
		print(result)