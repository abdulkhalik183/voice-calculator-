"""Safe expression evaluator using AST.
Supports: + - * / ** % parentheses, unary +/-, numeric literals, and selected math functions.
"""
import ast
import operator as op
import math

# Allowed operators mapping
ALLOWED_OPERATORS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}

# Whitelisted math functions
ALLOWED_FUNCTIONS = {name: getattr(math, name) for name in (
    'sin', 'cos', 'tan', 'asin', 'acos', 'atan',
    'sqrt', 'log', 'log10', 'exp', 'degrees', 'radians',
    'floor', 'ceil', 'fabs'
)}

# Add constants
CONSTANTS = {'pi': math.pi, 'e': math.e}


def evaluate(expression: str) -> float:
    """Safely evaluate a math expression provided as a string.
    Raises ValueError on invalid input.
    """
    try:
        node = ast.parse(expression, mode='eval')
        return _eval_node(node.body)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def _eval_node(node):
    if isinstance(node, ast.Num):  # < Py3.8
        return node.n
    if isinstance(node, ast.Constant):  # Py3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only numeric constants are allowed")

    if isinstance(node, ast.BinOp):
        if type(node.op) not in ALLOWED_OPERATORS:
            raise ValueError(f"Operator {type(node.op)} not allowed")
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        return ALLOWED_OPERATORS[type(node.op)](left, right)

    if isinstance(node, ast.UnaryOp):
        if type(node.op) not in ALLOWED_OPERATORS:
            raise ValueError(f"Unary operator {type(node.op)} not allowed")
        operand = _eval_node(node.operand)
        return ALLOWED_OPERATORS[type(node.op)](operand)

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Only simple function calls allowed")
        func_name = node.func.id
        if func_name not in ALLOWED_FUNCTIONS:
            raise ValueError(f"Function '{func_name}' is not allowed")
        args = [_eval_node(arg) for arg in node.args]
        return ALLOWED_FUNCTIONS[func_name](*args)

    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]
        raise ValueError(f"Unknown identifier: {node.id}")

    raise ValueError(f"Unsupported expression: {ast.dump(node)}")
