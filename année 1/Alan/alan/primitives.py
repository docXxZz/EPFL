
# Primitive values of the language.
PRIM_VALS = {
    "PLUS": lambda x, y: x + y,
    "MINUS": lambda x, y: x - y,
    "TIMES": lambda x, y: x * y,
    "DIV": lambda x, y: x // y,
    "MOD": lambda x, y: x % y,
    "LT": lambda x, y: x < y,
    "GT": lambda x, y: x > y,
    "LTE": lambda x, y: x <= y,
    "GTE": lambda x, y: x >= y,
    "EQ": lambda x, y: x == y,
    "NEQ": lambda x, y: x != y,
    "NOT": lambda x: not x,
    "CONCAT": lambda x, y: x + y,
    "PRINT": lambda x: print(x),
    "INPUT": lambda x: input(x),
    "STR_TO_INT": lambda x: int(x),
    "INT_TO_STR": lambda x: str(x),
}