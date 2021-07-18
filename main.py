from tinypost.shunt import eval_expr

while True:
	expr = input("math shell > ") 
	if expr == "exit" or expr == "quit":
		break
	
	result = eval_expr(expr)
	# if tinypost.shunt.error:
	# 	print(expr)
	# 	print(" " * tinypost.shunt.error + "^")
	# 	print("SyntaxError: invalid syntax")
	print(result)