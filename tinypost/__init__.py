from .shunt import _eval_postfix
from .postfix_parser import _infix_to_postfix

def eval_expr(expression: str):
	return _eval_postfix(_infix_to_postfix(expression))