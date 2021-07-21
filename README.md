<img alt="Tinypost logo" src="static/logo.png" align="right"/>


# Tinypost

Tinypost is a tiny **infix-to-postfix** expression parser and interpreter for
math expressions. Quickly evaluate math expressions quickly with just a few lines of
code. Tinypost supports many of the functions in the
python ```math``` module.

## Features

- No external dependencies
- Fast performance
- Abides by standard operator precedence
- Implements many mathematical functions in the ```math``` module
- Easily bind custom variables and functions
- MIT License
- Local stacks
- No recursion

## Install

Install easily using the following command.

```
pip install tinypost
```

## Simple Example

The following code evaluates an expression at runtime.

```python
import tinypost as tp
print(tp.eval_expr("3 + 12 / 4")) # Prints 6.0
```

## Binding Variables

Setting and updating your own custom variables is simple.

```python
import tinypost as tp

x = 5.5
tp.add_var("x", x)
print(tp.eval_expr("(x + 4) / 2"))) # Prints 4.75

x = 3.7
tp.update_var("x", x)
print(tp.eval_expr("(x + 4) / 2"))) # Prints 3.85

long_var_name = 5.5
tp.add_var("long_var_name", long_var_name)
print(tp.eval_expr("long_var_name * 3 / 6.23"))) # Prints 2.648...
```
Variable names must start with letter and can only contain letters, underscores,
and numbers. You can also use multiple variables in a single expression.

### Optimizing Variable Usage

If you find yourself evalulating the same expression over and over again
but just updating the value of the variable, you can try the following:

```python
import tinypost as tp

x = 3
tp.update_var("x", x)

expr = tp.compile_expr("x^2 + 4")

for i in range(3):
	x = i
	tp.update_var("x", i)
	print(tp.eval_compiled(expr), end=" ") # Prints 4 5 8
```

This will run faster than if you were to call ```tp.eval_expr()``` for each
iteration of the loop.

## Mathematical Functions

Tinypost support many mathematical functions, including abs, sqrt, sin, cos,
tan, ln, acos, asin, atan, atan2, exp, log, sinh, cosh, tanh, max, and pow.
When calling a function, make sure to put a pair of parentheses around its
arguments, and if it has multiple arguments, separate each argument with a comma.

```python
import tinypost as tp
expr = "max(sin(3 + 4 / 3.5), 0.6)"
print(tp.eval_expr(expr)) # Prints 0.6
```

If a function you would like to use is not supported by Tinypost or you would
like to bind your own functions, you can do the following.

```python
import tinypost as tp

def my_weird_sum(a, b):
    weird_num = 2.3551
    return (a / weird_num) ** 2 + b

# Functions cannot have optional parameters, they 
# must have a constant number of arguments.
# Functions must return a singular int or float.

tp.add_func("my_weird_sum", my_weird_sum)
expr = "my_weird_sum(3, 9.2) + 3" 
print(tp.eval_expr(expr)) # Prints 13.822...
```

Also, the constants ```pi``` and ```e``` are available for your use.

## How This Works
Tinypost uses Dijkstra's Shunting Yard Algorithm to convert infix expressions
to postfix expressions (Tinypost uses right postfix notation). Afterwards, Tinypost
uses a postfix expressions evaluation algorithm to evaluate the compiled expression.
Both algorithms make extensive use of stacks, meaning that popping and pushing to the
stack is an ```O(1)``` process. The entire algorithm runs in about ```O(n)``` time
because it has to loop through every token in the expression.

## Notes
Tinypost raises python ```SyntaxError```s if it finds an error in an expresion
you passed in. Variables, functions, and modules prefixed by an ```_``` are 
meant for **internal use** only. Using these incorrectly could result in
unpredictable behavior.

