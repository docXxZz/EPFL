from trees import *
from tokens import *
from lexing import lex
from typechecking import *

class ParseError(Exception):
    def __init__(self, message):
        super().__init__(message)


class TokenStream:
    def __init__(self, text):
        self.text = text
        self.tokens = lex(text)
        self.buffer = None

    def has_next(self):
        if self.buffer is None:
            try:
                self.buffer = next(self.tokens)
            except StopIteration:
                return False
        return True

    def _lookahead(self):
        if self.buffer is None:
            try:
                self.buffer = next(self.tokens)
            except StopIteration:
                return None
        return self.buffer

    def has(self, token_class):
        token = self._lookahead()
        if token is None:
            return False
        return isinstance(token, token_class)

    def consume(self, token_class):
        if not self.has(token_class):
            return False
        token = self._lookahead()
        self.buffer = None
        return token

    def require(self, token_class):
        if not self.has(token_class):
            next_token = self._lookahead()
            if next_token is None:
                raise ParseError(f'Expected {token_class.__name__}, got the end of the file.')
            else:
                raise ParseError(f'Expected {token_class.__name__}, got {next_token.__class__.__name__} at position {next_token.line}:{next_token.col}')
        return self.consume(token_class)
    
    def position(self):
        if token := self._lookahead():
            return token.line, token.col
        else:
            return None
        

def parse_expression(tokens):
    if token := tokens.consume(OpenBrace):
        
        first_statement = parse_statement(tokens)
        statements = [first_statement]
        while tokens.consume(SemicolonSymbol):
            statement = parse_statement(tokens)
            statements.append(statement)

        decls = [statement.decl
                    for statement in statements
                    if statement.decl is not None]

        exprs = [statement.expr
                    for statement in statements
                    if statement.expr is not None]
        
        if len(exprs) == 0:
            raise ParseError(f'Expected an expression inside the block at position {token.line}:{token.col}')

        tokens.require(CloseBrace)
        return Block(decls, exprs)
    
    else:
        return None

        
class Statement:
    def __init__(self, decl, expr):
        self.decl = decl
        self.expr = expr


def parse_statement(tokens):
    if let_token := tokens.consume(LetKeyword):
        decl = parse_declaration(tokens)
        if decl is None:
            raise ParseError(f'Expected a declaration after the "let" keyword at position {let_token.line}:{let_token.col}')
        
        name = decl.name

        if eq_token := tokens.consume(EqualSymbol):
            expr = parse_expression(tokens)
            if expr is None:
                raise ParseError(f'Expected an expression after the "=" symbol at position {eq_token.line}:{eq_token.col}')
            return Statement(decl, Assignment(name, expr))
        else:
            return Statement(decl, None)
    elif tokens.consume(DefKeyword):
        id = tokens.require(Identifier).name
        tokens.require(OpenParenthesis)
        params = []
        if not tokens.consume(CloseParenthesis):
            first_decl = parse_declaration(tokens)
            params.append(first_decl)
            while tokens.consume(CommaSymbol):
                extra_decl = parse_declaration(tokens)
                params.append(extra_decl)
            tokens.require(CloseParenthesis)
        colon_token = tokens.require(ColonSymbol)
        ret_type = parse_type(tokens)
        if ret_type is None:
            raise ParseError(f'Expected a type after the colon at position {colon_token.line}:{colon_token.col}')
        tokens.require(EqualSymbol)
        body = parse_expression(tokens)
        fun_type = FunctionType([decl.type for decl in params], ret_type)
        return Statement(Declaration(id, fun_type), Assignment(id, Abstraction(params, body)))
    else:
        expr = parse_expression(tokens)
        if expr is None:
            return None
        return Statement(None, expr)


def parse_declaration(tokens):
    return None


def parse_assignment(tokens):
    expr = parse_disjunction(tokens)
    if expr is None:
        return None
    
    if token := tokens.consume(EqualSymbol):
        if not isinstance(expr, Variable):
            raise ParseError(f'Expected a variable on the left side of the assignment at position {token.line}:{token.col}')
        
        right = parse_expression(tokens)

        if right is None:
            raise ParseError(f'Expected an expression on the right side of the assignment at position {token.line}:{token.col}')
        
        return Assignment(expr.name, right)
    
    else:
        return expr


def parse_disjunction(tokens):
    return None


def parse_conjunction(tokens):
    return None


def parse_negation(tokens):
    return None


def parse_comparison(tokens):
    return None


def parse_sum(tokens):
    return None


def parse_product(tokens):
    return None


def parse_application(tokens):
    return None


def parse_base(tokens):
    return None


def parse_type(tokens):
    """Parse un type."""

    if open_token := tokens.consume(OpenParenthesis):
        # Type de fonction
        args = []
        if not (close_token := tokens.consume(CloseParenthesis)):
            first_arg = parse_type(tokens)
            if first_arg is None:
                raise ParseError(f'Expected an argument type after the open parenthesis at position {open_token.line}:{open_token.col}')
            args.append(first_arg)
            while comma_token := tokens.consume(CommaSymbol):
                extra_arg = parse_type(tokens)
                if extra_arg is None:
                    raise ParseError(f'Expected an argument type after the comma at position {comma_token.line}:{comma_token.col}')
                args.append(extra_arg)
            close_token = tokens.require(CloseParenthesis)
        ret_type = parse_type(tokens)
        if ret_type is None:
            raise ParseError(f'Expected a return type after the close parenthesis at position {close_token.line}:{close_token.col}')

        return FunctionType(args, ret_type)

    elif token := tokens.consume(Identifier):
        # Type simple
        return SimpleType(token.name)

    else:
        return None

    
if __name__ == "__main__":
    from display import show_tree

    text = r'hello_world'
    tokens = list(lex(text))
    expr = parse_expression(TokenStream(text))
    print(show_tree(expr))