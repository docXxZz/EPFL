
class Token:
    def __bool__(self):
        return True
    
    def setPos(self, pos, line, col):
        self.pos = pos
        self.line = line
        self.col = col

    def __str__(self):
        # List the attributes of the token
        attrs = [f"{attr}={repr(getattr(self, attr))}" for attr in dir(self) if
                 not attr.startswith('_') and
                 not callable(getattr(self, attr)) and 
                 not attr in ["line", "col", "pos"]]
        res = f"<{self.__class__.__name__}"
        if attrs:
            res += "(" + ", ".join(attrs) + ")"
        res += f" at {self.line}:{self.col}>"
        return res


class Identifier(Token):
    def __init__(self, name):
        self.name = name

class IntLiteral(Token):
    def __init__(self, value):
        self.value = int(value)

class BoolLiteral(Token):
    def __init__(self, value):
        self.value = value == "true"

class StrLiteral(Token):
    def __init__(self, value):
        # A little bit of magic to handle escape sequences
        self.value = value.encode('latin-1', 'backslashreplace').decode('unicode-escape')

class NoneLiteral(Token):
    pass

class IfKeyword(Token):
    pass

class ElseKeyword(Token):
    pass

class WhileKeyword(Token):
    pass

class LetKeyword(Token):
    pass

class DefKeyword(Token):
    pass

class FunKeyword(Token):
    pass

class OpenParenthesis(Token):
    pass

class CloseParenthesis(Token):
    pass

class OpenBrace(Token):
    pass

class CloseBrace(Token):
    pass

class ColonSymbol(Token):
    pass

class SemicolonSymbol(Token):
    pass

class CommaSymbol(Token):
    pass

class DotSymbol(Token):
    pass

class EqualSymbol(Token):
    pass

class MultiplicativeOperator(Token):
    def __init__(self, op):
        self.op = op

class AdditiveOperator(Token):
    def __init__(self, op):
        self.op = op

class ComparisonOperator(Token):
    def __init__(self, op):
        self.op = op

class AndOperator(Token):
    pass

class OrOperator(Token):
    pass

class NotOperator(Token):
    pass

