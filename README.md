# Tinypost

Tinypost is a tiny infix-to-postfix expression parser and interpreter for
math expressions. Quickly evaluate math expressions with just a view lines of
code and fast performance. Tinypost supports many of the functions in the
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
print(tp.eval_expr("3 + 12 / 4"))
```
