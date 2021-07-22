import tinypost as tp

while True:
    expr = input("math shell > ")
    if expr == "exit" or expr == "quit":
        break

    try:
        result = tp.eval_expr(expr)
        print(result)
    except Exception as e:
        print(e)

# x = 0.32

# tp.add_var("x", x)
# expr = tp.compile_expr("sin(x) + 3 / ln(max(x + 4, 0.2))")
# tp.update_var("x", 0.892)

# print(tp.eval_compiled(expr))
# print(tp.eval_expr("3 + 12 / 2"))


# def my_weird_sum(a, b):
#     weird_num = 2.3551
#     return (a / weird_num) ** 2 + b


# tp.add_func("my_weird_sum", my_weird_sum)
# expr = tp.compile_expr("my_weird_sum(3, 9.2) + 3")
# print(tp.eval_compiled(expr))
# print(my_weird_sum(3, 9.2) + 3)
