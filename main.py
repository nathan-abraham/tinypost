import tinypost as tp

# while True:
# 	expr = input("math shell > ") 
# 	if expr == "exit" or expr == "quit":
# 		break
	
# 	result = tp.eval_expr(expr)
# 	print(result)

x = 0.32

tp.add_var("x", x)
expr = tp.compile_expr("sin(x) + 3 / ln(max(x + 4, 0.2))")
tp.update_var("x", 0.892)

print(tp.eval_compiled(expr))