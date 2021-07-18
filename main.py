import tinypost as tp

while True:
	expr = input("math shell > ") 
	if expr == "exit" or expr == "quit":
		break
	
	result = tp.eval_expr(expr)
	print(result)